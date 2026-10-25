// Simulate the review server's engine schedule from measured per-search times.
// futures::stream::buffered(n) keeps at most n searches in flight *including finished ones
// that wait for an earlier, slower search* (FuturesOrdered::len counts queued outputs), so one
// slow search stalls the pool. buffer_unordered(n) starts a new search as soon as any slot frees.
const fs = require("fs");
const path = require("path");
const dir = process.argv[2];
const load = (c) => fs.readFileSync(path.join(dir, c + ".jsonl"), "utf8").trim().split("\n").map((l) => JSON.parse(l));
const byGame = (recs) => recs.reduce((m, r) => ((m[r.game] ||= []).push(r), m), {});

function ordered(times, n) {
  // buffered(n): job k may start only once job k-n has been *yielded*, and yields are in order.
  const start = [], end = [], yielded = [];
  for (let k = 0; k < times.length; k++) {
    const s = k < n ? 0 : yielded[k - n];
    start[k] = s; end[k] = s + times[k];
    yielded[k] = Math.max(end[k], k ? yielded[k - 1] : 0);
  }
  return yielded[times.length - 1] || 0;
}
function unordered(times, n) {
  const slots = new Array(n).fill(0);
  for (const t of times) { slots.sort((a, b) => a - b); slots[0] += t; }
  return Math.max(...slots);
}
const main = byGame(load(process.argv[3] || "ours_d18_mpv3_clear"));
const threat = byGame(load(process.argv[4] || "threat_d10_clear"));
const pool = Number(process.argv[5] || 4);
const bestThreatShare = 0.55; // played move is not the engine's best move (coached, non-book)
let tot = { ord: 0, unord: 0, cpu: 0, plies: 0 };
console.log("game plies  cpu_s  buffered(4)_s  unordered(4)_s  stall%");
for (const [g, recs] of Object.entries(main)) {
  recs.sort((a, b) => a.ply - b.ply);
  const thr = (threat[g] || []).sort((a, b) => a.ply - b.ply).map((r) => r.ms);
  const phase1 = [...recs.map((r) => r.ms), ...thr];
  const phase2 = thr.filter((_, i) => i % 100 < bestThreatShare * 100);
  const o = ordered(phase1, pool) + ordered(phase2, pool);
  const u = unordered(phase1, pool) + unordered(phase2, pool);
  const cpu = [...phase1, ...phase2].reduce((a, b) => a + b, 0);
  tot.ord += o; tot.unord += u; tot.cpu += cpu; tot.plies += recs.length - 1;
  console.log(`${g} ${recs.length - 1}  ${(cpu / 1000).toFixed(1)}  ${(o / 1000).toFixed(1)}  ${(u / 1000).toFixed(1)}  ${(100 * (o - u) / o).toFixed(0)}%`);
}
console.log(`total plies ${tot.plies}: cpu ${(tot.cpu / 1000).toFixed(0)} s, buffered ${(tot.ord / 1000).toFixed(0)} s, unordered ${(tot.unord / 1000).toFixed(0)} s, ideal cpu/${pool} ${(tot.cpu / pool / 1000).toFixed(0)} s`);
console.log(`ms per ply: buffered ${(tot.ord / tot.plies).toFixed(0)}, unordered ${(tot.unord / tot.plies).toFixed(0)}`);
