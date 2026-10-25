// chess.com reported depth by game ply and by our 600k-node depth, over all 577 cc-reviews.
const fs = require("fs");
const path = require("path");
const ccDir = process.env.CC_REVIEWS || path.join(__dirname, "../../tests/calibration/cc-reviews");
const bands = {};
let total = 0, deep = 0, book = 0, bookDeep = 0;
for (const f of fs.readdirSync(ccDir).filter((x) => x.endsWith(".sf.txt"))) {
  for (const l of fs.readFileSync(path.join(ccDir, f), "utf8").split("\n").slice(1)) {
    const t = l.trim().split(/\s+/);
    const s = (t[3] || "").match(/^(-?\d+)@(\d+)$/);
    if (!s) continue;
    const ply = Number(t[0]), d = Number(s[2]);
    const b = ply <= 10 ? "01-10" : ply <= 20 ? "11-20" : ply <= 40 ? "21-40" : ply <= 60 ? "41-60" : ply <= 80 ? "61-80" : "81+";
    (bands[b] ||= []).push(d);
    total++; if (d >= 25) deep++;
    if (t[2] === "book") { book++; if (d >= 25) bookDeep++; }
  }
}
const q = (a, p) => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(p * (s.length - 1))]; };
for (const b of Object.keys(bands).sort()) {
  const a = bands[b];
  console.log(`plies ${b}: n=${a.length} depth p10/50/90 ${q(a, 0.1)}/${q(a, 0.5)}/${q(a, 0.9)}  >=25: ${(100 * a.filter((d) => d >= 25).length / a.length).toFixed(0)}%`);
}
console.log(`all: ${total} positions, depth>=25 ${(100 * deep / total).toFixed(1)}%; book moves ${book}, of which depth>=25 ${(100 * bookDeep / book).toFixed(0)}%`);
