import { submitIndexNow, DEFAULT_ENDPOINT } from './lib/indexnow-client.mjs';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

const DEFAULT_HOST = 'budgetholidayshub.com';
const DEFAULT_SITEMAP = 'sitemap.xml';
const KEY_PATTERN = /^[A-Za-z0-9-]{8,128}$/;

function getArgValue(name, fallback) {
  const prefix = `--${name}=`;
  const arg = process.argv.find((item) => item.startsWith(prefix));
  return arg ? arg.slice(prefix.length) : fallback;
}

function hasFlag(name) {
  return process.argv.includes(`--${name}`);
}

function toIsoDate(date) {
  return date.toISOString().slice(0, 10);
}

function decodeXml(value) {
  return value
    .replaceAll('&amp;', '&')
    .replaceAll('&lt;', '<')
    .replaceAll('&gt;', '>')
    .replaceAll('&quot;', '"')
    .replaceAll('&apos;', "'");
}

async function discoverIndexNowKey(rootDir) {
  if (process.env.INDEXNOW_KEY) {
    return process.env.INDEXNOW_KEY.trim();
  }

  const entries = await readdir(rootDir, { withFileTypes: true });
  for (const entry of entries) {
    if (!entry.isFile() || !entry.name.endsWith('.txt')) continue;

    const candidateKey = entry.name.slice(0, -4);
    if (!KEY_PATTERN.test(candidateKey)) continue;

    const content = (await readFile(path.join(rootDir, entry.name), 'utf8')).trim();
    if (content === candidateKey) return candidateKey;
  }

  throw new Error(`Could not find an IndexNow key file in ${rootDir}`);
}

async function readText(source) {
  if (/^https?:\/\//i.test(source)) {
    const response = await fetch(source);
    if (!response.ok) {
      throw new Error(`Failed to fetch ${source}: HTTP ${response.status}`);
    }
    return response.text();
  }

  return readFile(path.resolve(process.cwd(), source), 'utf8');
}

function urlBlocksFromXml(xml) {
  return [...xml.matchAll(/<url>\s*([\s\S]*?)\s*<\/url>/g)].map((match) => match[1]);
}

function locsFromXml(xml) {
  return [...xml.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/gi)].map((match) => decodeXml(match[1].trim()));
}

async function readSitemapUrlBlocks(source, visited = new Set()) {
  const absoluteSource = /^https?:\/\//i.test(source)
    ? new URL(source).toString()
    : path.resolve(process.cwd(), source);

  if (visited.has(absoluteSource)) return [];
  visited.add(absoluteSource);

  const xml = await readText(source);
  if (!/<sitemapindex\b/i.test(xml)) return urlBlocksFromXml(xml);

  const blocks = [];
  for (const loc of locsFromXml(xml)) {
    blocks.push(...await readSitemapUrlBlocks(loc, visited));
  }
  return blocks;
}

async function readSitemapUrls({ sitemap, host, sinceDays, includeAll }) {
  const cutoffDate = toIsoDate(new Date(Date.now() - sinceDays * 24 * 60 * 60 * 1000));
  const urls = new Set();

  for (const block of await readSitemapUrlBlocks(sitemap)) {
    const loc = block.match(/<loc>(.*?)<\/loc>/)?.[1];
    const lastmod = block.match(/<lastmod>(.*?)<\/lastmod>/)?.[1];
    if (!loc) continue;

    const url = new URL(decodeXml(loc));
    if (url.hostname !== host) continue;
    if (!includeAll && (!lastmod || lastmod < cutoffDate)) continue;

    urls.add(url.toString());
  }

  return [...urls].sort();
}

async function main() {
  const rootDir = process.cwd();
  const host = getArgValue('host', process.env.INDEXNOW_HOST || DEFAULT_HOST);
  const endpoint = getArgValue('endpoint', process.env.INDEXNOW_ENDPOINT || DEFAULT_ENDPOINT);
  const sitemap = getArgValue('sitemap', process.env.INDEXNOW_SITEMAP || DEFAULT_SITEMAP);
  const sinceDays = Number(getArgValue('since-days', process.env.INDEXNOW_SINCE_DAYS || '14'));
  const retries = Number(getArgValue('retries', process.env.INDEXNOW_RETRIES || '2'));
  const retryDelayMs = Number(getArgValue('retry-delay-ms', process.env.INDEXNOW_RETRY_DELAY_MS || '15000'));
  const includeAll = hasFlag('all') || process.env.INDEXNOW_SUBMIT_ALL === '1';
  const dryRun = hasFlag('dry-run') || process.env.INDEXNOW_DRY_RUN === '1';

  if (!Number.isFinite(sinceDays) || sinceDays < 0) {
    throw new Error(`Invalid --since-days value: ${sinceDays}`);
  }
  if (!Number.isFinite(retries) || retries < 0 || !Number.isInteger(retries)) {
    throw new Error(`Invalid --retries value: ${retries}`);
  }
  if (!Number.isFinite(retryDelayMs) || retryDelayMs < 0) {
    throw new Error(`Invalid --retry-delay-ms value: ${retryDelayMs}`);
  }

  const key = await discoverIndexNowKey(rootDir);
  const keyLocation = process.env.INDEXNOW_KEY_LOCATION || `https://${host}/${key}.txt`;
  const urls = await readSitemapUrls({ sitemap, host, sinceDays, includeAll });

  await submitIndexNow({ endpoint, host, key, keyLocation, urls, dryRun, retries, retryDelayMs });
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : error);
  process.exitCode = 1;
});
