const baseUrl = process.env.LIVE_SITE_URL || "https://budgetholidayshub.com";
const timeoutMs = Number.parseInt(process.env.LIVE_CHECK_TIMEOUT_MS || "15000", 10);

const canonicalHost = new URL(baseUrl).host;
const legacySpainUrl = `${baseUrl}/guides/spain-budget-holidays/`;
const canonicalSpainUrl = `${baseUrl}/guides/cheap-holidays-spain-from-uk/`;
const sitemapUrl = `${baseUrl}/sitemap.xml`;

function normalizeUrl(url) {
  return url.endsWith("/") ? url : `${url}/`;
}

async function fetchWithTimeout(url, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    return await fetch(url, {
      ...options,
      signal: controller.signal,
      headers: {
        "user-agent": "budget-holidays-live-seo-check",
        ...(options.headers || {}),
      },
    });
  } finally {
    clearTimeout(timer);
  }
}

async function checkRedirect(source, expectedTarget) {
  const response = await fetchWithTimeout(source, { method: "HEAD", redirect: "manual" });
  const location = response.headers.get("location") || "";

  if (![301, 302, 308].includes(response.status)) {
    throw new Error(`${source} returned HTTP ${response.status}; expected a canonical redirect.`);
  }

  if (normalizeUrl(location) !== normalizeUrl(expectedTarget)) {
    throw new Error(`${source} redirects to ${location || "(missing location)"}; expected ${expectedTarget}.`);
  }
}

async function checkLegacySpainHandoff() {
  const response = await fetchWithTimeout(legacySpainUrl, { redirect: "manual" });
  if (response.status !== 200) {
    throw new Error(`${legacySpainUrl} returned HTTP ${response.status}; expected the noindex handoff page.`);
  }

  const html = await response.text();
  const lowerHtml = html.toLowerCase();
  if (!lowerHtml.includes('name="robots"') || !lowerHtml.includes("noindex")) {
    throw new Error(`${legacySpainUrl} is missing a noindex robots directive.`);
  }
  if (!html.includes(`rel="canonical" href="${canonicalSpainUrl}"`)) {
    throw new Error(`${legacySpainUrl} is missing the canonical target ${canonicalSpainUrl}.`);
  }
  if (!html.includes(canonicalSpainUrl)) {
    throw new Error(`${legacySpainUrl} is missing a visible or scripted handoff to ${canonicalSpainUrl}.`);
  }
}

async function checkLegacyUrlExcludedFromSitemap() {
  const response = await fetchWithTimeout(sitemapUrl);
  if (!response.ok) {
    throw new Error(`${sitemapUrl} returned HTTP ${response.status}.`);
  }

  const xml = await response.text();
  if (xml.includes(legacySpainUrl)) {
    throw new Error(`${legacySpainUrl} should not be listed in the live sitemap.`);
  }
}

await checkRedirect(`http://${canonicalHost}/`, `${baseUrl}/`);
await checkRedirect(`http://www.${canonicalHost}/`, `${baseUrl}/`);
await checkRedirect(`https://www.${canonicalHost}/`, `${baseUrl}/`);
await checkLegacySpainHandoff();
await checkLegacyUrlExcludedFromSitemap();

console.log("Live SEO crawl hygiene check passed.");
