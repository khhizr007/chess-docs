// Summarise the engine bench (bench.py output) per config.
const fs = require("fs");
const path = require("path");
const dir = process.argv[2];
const q = (a, p) => { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.floor(p * (s.length - 1))] : NaN; };
const rows = [];
for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".jsonl")).sort()) {
  const recs = fs.readFileSync(path.join(dir, f), "utf8").trim().split("\n").filter(Boolean).map((l) => JSON.parse(l));
  if (!recs.length) continue;
  const ms = recs.map((r) => r.ms), d = recs.map((r) => r.depth), n = recs.map((r) => r.nodes);
  const sd = recs.map((r) => r.seldepth).filter((x) => x != null);
  rows.push({
    config: f.replace(".jsonl", ""), n: recs.length,
    mean_ms: (ms.reduce((a, b) => a + b, 0) / ms.length).toFixed(0),
    p50_ms: q(ms, 0.5).toFixed(0), p90_ms: q(ms, 0.9).toFixed(0), max_ms: q(ms, 1).toFixed(0),
    depth_p10_50_90: `${q(d, 0.1)}/${q(d, 0.5)}/${q(d, 0.9)}`,
    seldepth_p50: sd.length ? q(sd, 0.5) : "",
    nodes_p50: q(n, 0.5), nodes_p90: q(n, 0.9),
  });
}
console.table(rows);
