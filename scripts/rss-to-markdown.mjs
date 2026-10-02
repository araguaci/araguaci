import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const [feedUrl, templateFile, outputDir] = process.argv.slice(2);

if (!feedUrl || !templateFile || !outputDir) {
  console.error("Uso: node scripts/rss-to-markdown.mjs <feed_url> <template> <output_dir>");
  process.exit(1);
}

const response = await fetch(feedUrl);
if (!response.ok) {
  console.error(`Feed respondeu ${response.status}: ${feedUrl}`);
  process.exit(1);
}

const xml = await response.text();
const template = readFileSync(templateFile, "utf8");
mkdirSync(outputDir, { recursive: true });

const entries = [...xml.matchAll(/<entry>([\s\S]*?)<\/entry>/g)];
if (entries.length === 0) {
  console.error("Nenhuma entrada <entry> no feed.");
  process.exit(1);
}

let written = 0;
for (const match of entries) {
  const entry = match[1];
  const title = textOf(entry, "title") || "sem-titulo";
  const published = textOf(entry, "published") || textOf(entry, "updated") || "";
  const link =
    attrOf(entry, "link", "href") ||
    textOf(entry, "link") ||
    "";
  const description = strip(textOf(entry, "media:description") || title);
  const date = published.slice(0, 10) || "sem-data";
  const slug = slugify(title);
  const body = template
    .replaceAll("[TITLE]", title.replaceAll("\n", " ").trim())
    .replaceAll("[DATE]", date)
    .replaceAll("[DESCRIPTION]", description);

  const file = join(outputDir, `${date}-${slug}.md`);
  writeFileSync(file, `${body.trim()}\n\n${link}\n`, "utf8");
  written += 1;
}

console.log(`${written} arquivos em ${outputDir}`);

function textOf(entry, tag) {
  const found = entry.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`));
  return found ? decode(strip(found[1])) : "";
}

function attrOf(entry, tag, attr) {
  const found = entry.match(new RegExp(`<${tag}[^>]*${attr}="([^"]+)"`));
  return found ? decode(found[1]) : "";
}

function strip(value) {
  return value.replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, "$1").replace(/<[^>]+>/g, "").trim();
}

function decode(value) {
  return value
    .replaceAll("&amp;", "&")
    .replaceAll("&lt;", "<")
    .replaceAll("&gt;", ">")
    .replaceAll("&quot;", '"')
    .replaceAll("&#39;", "'");
}

function slugify(value) {
  const base = value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "")
    .slice(0, 80);
  return base || "item";
}
