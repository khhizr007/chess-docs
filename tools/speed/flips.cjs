// flips.cjs <runA> <runB> [label] : plies whose label differs between two runs, with Chess.com's label.
const fs = require("fs");
const path = require("path");
const T = path.join(__dirname, "../../tests/calibration");
const [a, b, focus] = process.argv.slice(2);
const MAP = { great_find: "great", forced: "best" };
const norm = (c) => (c == null ? "none" : MAP[c] || c);
const ours = (run, f) => {
  const p = path.join(T, "runs", run, f);
  return fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, "utf8")).result.plies : null;
};
const tally = {};
const list = [];
let gain = 0, loss = 0;
for (const f of fs.readdirSync(path.join(T, "runs", a))) {
  if (!/^\d+\.json$/.test(f)) continue;
  const pa = ours(a, f), pb = ours(b, f);
  if (!pb) continue;
  const id = f.replace(".json", "");
  const app = JSON.parse(fs.readFileSync(path.join(T, "games", `${id}.labels.json`), "utf8")).plies;
  for (let i = 0; i < Math.min(pa.length, pb.length, app.length); i++) {
    const la = norm(pa[i].classification), lb = norm(pb[i].classification), lc = app[i].label;
    if (la === lb) continue;
    if (la === lc) loss++;
    if (lb === lc) gain++;
    const k = `app ${lc}: ${la} -> ${lb}`;
    tally[k] = (tally[k] || 0) + 1;
    if (focus && [lc, la, lb].includes(focus))
      list.push(`${id} ply ${pa[i].ply} ${pa[i].san} app=${lc} A=${la} B=${lb} epLost ${pa[i].ep_lost.toFixed(3)}->${pb[i].ep_lost.toFixed(3)}`);
  }
}
console.log(`changed plies ${Object.values(tally).reduce((s, n) => s + n, 0)}: now right ${gain}, now wrong ${loss}`);
for (const [k, n] of Object.entries(tally).sort((p, q) => q[1] - p[1]).slice(0, 25)) console.log(String(n).padStart(4), k);
if (focus) console.log(list.join("\n"));
