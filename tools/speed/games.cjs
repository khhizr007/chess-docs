// Turn chess.com captures into per-game UCI move lists (square 0 = a1) for the engine bench.
const fs = require("fs");
const path = require("path");
const { parse } = require("./pb.cjs");
const get = (m, f) => m.filter((e) => e.f === f);
// chesscom.chess.v1.Square is 1-based (A1 = 1); PromotionPieceType 1..4 = N, B, R, Q.
const sq = (i) => "abcdefgh"[(i - 1) % 8] + (Math.floor((i - 1) / 8) + 1);
const promo = { 1: "n", 2: "b", 3: "r", 4: "q" };
const dir = process.argv[2];
const want = Number(process.argv[3] || 8);
const files = fs.readdirSync(dir).filter((x) => x.endsWith(".json")).sort();
const out = [];
const dump = [];
for (const f of files) {
  const cap = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8"));
  let m = parse(Buffer.from(cap.sockets[0].out[0].b64, "base64"));
  for (const k of [1, 1, 1]) m = parse(get(m, k)[0].v);
  const moves = [];
  for (const e of get(m, 2)) {
    const mv = parse(get(parse(e.v), 1)[0].v);
    const g = (k) => { const x = get(mv, k)[0]; return x ? Number(x.v) : undefined; };
    moves.push(sq(g(1) ?? 0) + sq(g(2) ?? 0) + (g(3) ? promo[g(3)] ?? "?" : ""));
    if (dump.length < 3 && mv.some((x) => x.f > 2)) dump.push(JSON.stringify(mv.map((x) => [x.f, String(x.v)])));
  }
  out.push({ id: cap.id, ms: cap.ms, moves });
}
// A deterministic spread of game lengths: every k-th game.
const pick = out.filter((_, i) => i % Math.floor(out.length / want) === 0).slice(0, want);
fs.writeFileSync(path.join(__dirname, "bench-games.json"), JSON.stringify(pick));
console.log("promotion samples", dump);
console.log(pick.map((g) => `${g.id} plies=${g.moves.length} cc_ms=${g.ms}`).join("\n"));
