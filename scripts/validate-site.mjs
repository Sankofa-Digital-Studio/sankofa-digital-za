import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDir, '..');
const dist = path.join(root, 'dist');
const htmlFiles = fs.readdirSync(dist).filter((name) => name.endsWith('.html')).sort();
const errors = [];
const warnings = [];

const exists = (file) => fs.existsSync(path.resolve(dist, file.split('#')[0].split('?')[0]));

for (const name of htmlFiles) {
  const source = fs.readFileSync(path.join(dist, name), 'utf8');
  if (!/<html\s+lang="en-ZA"/i.test(source)) errors.push(`${name}: missing en-ZA language`);
  if (!/<meta\s+name="viewport"/i.test(source)) errors.push(`${name}: missing viewport meta`);
  if (!/<title>[^<]+<\/title>/i.test(source)) errors.push(`${name}: missing title`);
  if (!/<main(?:\s|>)/i.test(source)) errors.push(`${name}: missing main landmark`);
  if (name !== '404.html' && !/class="skip-link"/i.test(source)) errors.push(`${name}: missing skip link`);

  const ids = [...source.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1]);
  const duplicateIds = ids.filter((id, index) => ids.indexOf(id) !== index);
  if (duplicateIds.length) errors.push(`${name}: duplicate ids ${[...new Set(duplicateIds)].join(', ')}`);

  for (const match of source.matchAll(/<(?:a|link)\b[^>]*\bhref="([^"]+)"/g)) {
    const href = match[1];
    if (/^(?:https?:|mailto:|tel:|#)/i.test(href)) continue;
    const target = href.startsWith('/') ? href.slice(1) : href;
    if (!exists(target)) errors.push(`${name}: missing link target ${href}`);
  }

  for (const match of source.matchAll(/<(?:img|script)\b[^>]*\bsrc="([^"]+)"/g)) {
    const src = match[1];
    if (/^https?:/i.test(src)) continue;
    if (!exists(src)) errors.push(`${name}: missing asset ${src}`);
  }

  for (const match of source.matchAll(/<img\b([^>]*)>/g)) {
    if (!/\balt="[^"]*"/i.test(match[1])) errors.push(`${name}: image missing alt attribute`);
  }

  if (/lorem ipsum/i.test(source)) {
    errors.push(`${name}: contains placeholder text`);
  }
  if (/\b(?:50\+|30\+|100%)\b/.test(source)) warnings.push(`${name}: review public metric claim`);
}

const hosting = JSON.parse(fs.readFileSync(path.join(root, '.openai', 'hosting.json'), 'utf8'));
if (!hosting.project_id) errors.push('.openai/hosting.json: missing project_id');
if (hosting.static?.directory !== 'dist') errors.push('.openai/hosting.json: static directory must be dist');

console.log(`Checked ${htmlFiles.length} HTML files.`);
for (const warning of warnings) console.warn(`WARN ${warning}`);
if (errors.length) {
  for (const error of errors) console.error(`ERROR ${error}`);
  process.exit(1);
}
console.log('Static site validation passed.');
