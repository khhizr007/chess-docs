// Compare bench scores/depths with chess.com's own per-position scores (cc-reviews/<id>.sf.txt).
// sf.txt line k: "<ply> <uci> <class> <cp>@<depth> ..." = chess.com's eval (White POV) of the
// position after ply k, and the depth it reports. Bench ply k = the same position.
const fs = require("fs");
const path = require("path");
const ccDir = process.env.CC_REVIEWS || path.join(__dirname, "../../tests/calibration/cc-reviews");
const dir = process.argv[2];
const cc = {};
function ccFor(id) {
  if (cc[id]) return cc[id];
  const m = {};
  for (const l of fs.readFileSync(path.join(ccDir, id + ".sf.txt"), "utf8").split("\n").slice(1)) {
    const t = l.trim().split(/\s+/);
    const s = (t[3] || "").match(/^(-?\d+)@(\d+)$/);
    if (s) m[Number(t[0])] = { cp: Number(s[1]), depth: Number(s[2]) };
  }
  return (cc[id] = m);
}
const q = (a, p) => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(p * (s.length - 1))]; };
for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".jsonl")).sort()) {
  const recs = fs.readFileSync(path.join(dir, f), "utf8").trim().split("\n").filter(Boolean).map((l) => JSON.parse(l));
  if (!recs.length || !recs[0].score === undefined) continue;
  let n = 0, exact = 0, within5 = 0, dEq = 0, sdEq = 0; const diffs = [], dd = [], sdd = [];
  for (const r of recs) {
    if (!r.score || !r.score.startsWith("cp")) continue;
    const c = ccFor(r.game)[r.ply];
    if (!c) continue;
    const v = Number(r.score.slice(2));
    n++; if (v === c.cp) exact++; if (Math.abs(v - c.cp) <= 5) within5++;
    diffs.push(Math.abs(v - c.cp)); dd.push(r.depth - c.depth);
    if (r.depth === c.depth) dEq++;
    if (r.seldepth != null) { sdd.push(r.seldepth - c.depth); if (r.seldepth === c.depth) sdEq++; }
  }
  if (!n) continue;
  console.log(`${f.padEnd(40)} n=${n} exact ${(100 * exact / n).toFixed(1)}% ±5cp ${(100 * within5 / n).toFixed(1)}% |Δcp| p50 ${q(diffs, 0.5)} p90 ${q(diffs, 0.9)}  depth-cc p50 ${q(dd, 0.5)} eq ${(100 * dEq / n).toFixed(0)}%  seldepth-cc p50 ${sdd.length ? q(sdd, 0.5) : "-"} eq ${sdd.length ? (100 * sdEq / n).toFixed(0) + "%" : "-"}`);
}
