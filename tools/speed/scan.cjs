// Scan chess.com game-review captures for engine Score messages
// (chesscom.engine.v1.Score: 1 score{}, 2 depth, 3 engine, 4 variation, 5 strength, 6 nodes).
const fs = require("fs");
const path = require("path");
const { parse } = require("./pb.cjs");

function isScore(m) {
  if (!m || m.length < 2) return null;
  let s = {}; let ok = true;
  for (const e of m) {
    if (e.f === 1 && e.t === 2) { const sub = parse(e.v); if (!sub || !sub.every((x) => x.f >= 1 && x.f <= 4)) ok = false; s.score = true; }
    else if (e.f === 2 && e.t === 0) s.depth = Number(e.v);
    else if (e.f === 3 && e.t === 0) s.engine = Number(e.v);
    else if (e.f === 4 && e.t === 0) s.variation = Number(e.v);
    else if (e.f === 5 && e.t === 0) s.strength = Number(e.v);
    else if (e.f === 6 && e.t === 0) s.nodes = Number(e.v);
    else ok = false;
  }
  return ok && s.score && s.engine !== undefined && s.engine >= 1 && s.engine <= 13 ? s : null;
}
function walk(b, out, depth = 0) {
  if (depth > 25) return;
  const m = parse(b);
  if (!m) return;
  const s = isScore(m);
  if (s) { out.push(s); return; }
  for (const e of m) if (e.t === 2 && e.v.length > 1) walk(e.v, out, depth + 1);
}
const dir = process.argv[2];
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".json"));
const games = [];
for (const f of files) {
  const cap = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8"));
  if (!cap.ok) continue;
  const scores = [];
  let plies = 0;
  for (const sock of cap.sockets || []) {
    for (const fr of sock.in || []) walk(Buffer.from(fr.b64, "base64"), scores);
  }
  games.push({ id: cap.id, kind: cap.kind, ms: cap.ms, scores });
}
// Aggregate.
const cnt = (arr, key) => arr.reduce((m, s) => ((m[s[key]] = (m[s[key]] || 0) + 1), m), {});
const all = games.flatMap((g) => g.scores);
console.log("games", games.length, "scores", all.length);
console.log("engine", cnt(all, "engine"));
console.log("strength", cnt(all, "strength"));
console.log("variation", cnt(all, "variation"));
const q = (a, p) => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(p * (s.length - 1))]; };
for (const eng of [13, 11, 10]) {
  const sc = all.filter((s) => s.engine === eng);
  if (!sc.length) continue;
  const d = sc.map((s) => s.depth).filter((x) => x !== undefined);
  const n = sc.map((s) => s.nodes).filter((x) => x !== undefined);
  console.log(`engine ${eng}: n=${sc.length} depth p10/50/90 ${q(d, 0.1)}/${q(d, 0.5)}/${q(d, 0.9)} nodes p10/50/90/max ${q(n, 0.1)}/${q(n, 0.5)}/${q(n, 0.9)}/${q(n, 1)} with-nodes ${n.length}`);
}
fs.writeFileSync(path.join(__dirname, "scores.json"), JSON.stringify(games.map((g) => ({ id: g.id, kind: g.kind, ms: g.ms, n: g.scores.length, s: g.scores }))));
