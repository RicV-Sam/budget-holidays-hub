const sitemapUrl = process.env.LIVE_SITEMAP_URL || "https://budgetholidayshub.com/sitemap.xml";
const timeoutMs = Number.parseInt(process.env.LIVE_CHECK_TIMEOUT_MS || "15000", 10);
const concurrency = Number.parseInt(process.env.LIVE_CHECK_CONCURRENCY || "8", 10);

function normalizeUrl(url) {
  return url.endsWith("/") ? url.slice(0, -1) : url;
}

async function fetchWithTimeout(url, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    return await fetch(url, {
      ...options,
      redirect: "follow",
      signal: controller.signal,
      headers: {
        "user-agent": "budget-holidays-live-sitemap-check",
        ...(options.headers || {}),
      },
    });
  } finally {
    clearTimeout(timer);
  }
}

async function loadSitemapUrls() {
  const response = await fetchWithTimeout(sitemapUrl);
  if (!response.ok) {
    throw new Error(`Sitemap returned HTTP ${response.status}: ${sitemapUrl}`);
  }

  const xml = await response.text();
  const urls = Array.from(xml.matchAll(/<loc>(.*?)<\/loc>/g), (match) => match[1].trim()).filter(Boolean);

  if (!urls.length) {
    throw new Error(`No <loc> URLs found in ${sitemapUrl}`);
  }

  return urls;
}

async function checkUrl(url) {
  try {
    const response = await fetchWithTimeout(url, { method: "HEAD" });
    const finalUrl = response.url || url;
    const statusOk = response.status === 200;
    const finalOk = normalizeUrl(finalUrl) === normalizeUrl(url);

    if (!statusOk || !finalOk) {
      return {
        url,
        ok: false,
        message: `HTTP ${response.status}, final URL ${finalUrl}`,
      };
    }

    return { url, ok: true };
  } catch (error) {
    return {
      url,
      ok: false,
      message: error instanceof Error ? error.message : String(error),
    };
  }
}

async function runPool(items, worker) {
  const results = [];
  let nextIndex = 0;

  async function runWorker() {
    while (nextIndex < items.length) {
      const index = nextIndex;
      nextIndex += 1;
      results[index] = await worker(items[index]);
    }
  }

  await Promise.all(Array.from({ length: Math.min(concurrency, items.length) }, runWorker));
  return results;
}

const urls = await loadSitemapUrls();
const results = await runPool(urls, checkUrl);
const failures = results.filter((result) => !result.ok);

console.log(`Checked ${urls.length} live sitemap URL(s) from ${sitemapUrl}.`);

if (failures.length) {
  console.error(`Live sitemap check failed for ${failures.length} URL(s):`);
  for (const failure of failures.slice(0, 50)) {
    console.error(`- ${failure.url}: ${failure.message}`);
  }
  process.exit(1);
}

console.log("Live sitemap check passed.");
