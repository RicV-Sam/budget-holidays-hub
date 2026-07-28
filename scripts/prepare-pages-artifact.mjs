import { cpSync, existsSync, mkdirSync, rmSync } from "node:fs";
import path from "node:path";

const root = process.cwd();
const outputDir = path.join(root, "_site");

const publicPaths = [
  ".nojekyll",
  "CNAME",
  "about",
  "affiliate-disclosure",
  "assets",
  "b686a7138c594c208fb6d2a10279f474.txt",
  "calculator",
  "contact",
  "editorial-standards",
  "guides",
  "how-we-research",
  "index.html",
  "make-money-for-travel",
  "planner",
  "privacy",
  "robots.txt",
  "sitemap.xml",
  "taste-the-world",
  "terms",
  "visit-uk",
  "videos",
];

rmSync(outputDir, { recursive: true, force: true });
mkdirSync(outputDir, { recursive: true });

for (const relativePath of publicPaths) {
  const source = path.join(root, relativePath);
  if (!existsSync(source)) {
    throw new Error(`Expected public path is missing: ${relativePath}`);
  }

  const destination = path.join(outputDir, relativePath);
  cpSync(source, destination, { recursive: true });
}

console.log(`Prepared ${publicPaths.length} public paths in ${path.relative(root, outputDir)}`);
