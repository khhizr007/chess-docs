// Chess.com review wall time vs game length, from the captures.
const fs = require("fs");
const path = require("path");
const { parse } = require("./pb.cjs");
const get = (m, f) => m.filter((e) => e.f === f);
const dir = process.argv[2];
const rows = [];
for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".json"))) {
  const cap = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8"));
  if (!cap.ok || !cap.sockets?.length) continue;
  const s = cap.sockets[0];
  const out = parse(Buffer.from(s.out[0].b64, "base64"));
  let m = out;
  for (const k of [1, 1, 1]) m = parse(get(m, k)[0].v);
  const plies = get(m, 2).length;
  const progress = s.in.filter((fr) => { const p = parse(Buffer.from(fr.b64, "base64")); return p && p.length === 1 && p[0].f === 1; }).length;
  const big = s.in.reduce((a, fr) => Math.max(a, fr.b64.length * 0.75), 0);
  rows.push({ id: cap.id, kind: cap.kind, plies, ms: cap.ms, progress, frames: s.in.length, bytes: Math.round(big) });
}
const q = (a, p) => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(p * (s.length - 1))]; };
const ok = rows.filter((r) => r.ms < 300000);
console.log("captures", rows.length, "under 300 s", ok.length);
console.log("plies p10/50/90", q(ok.map((r) => r.plies), 0.1), q(ok.map((r) => r.plies), 0.5), q(ok.map((r) => r.plies), 0.9));
console.log("ms p10/50/90", q(ok.map((r) => r.ms), 0.1), q(ok.map((r) => r.ms), 0.5), q(ok.map((r) => r.ms), 0.9));
const mpp = ok.map((r) => r.ms / Math.max(1, r.plies));
console.log("ms per ply p10/50/90", q(mpp, 0.1).toFixed(0), q(mpp, 0.5).toFixed(0), q(mpp, 0.9).toFixed(0));
// Least squares ms = a + b * plies
const n = ok.length, sx = ok.reduce((a, r) => a + r.plies, 0), sy = ok.reduce((a, r) => a + r.ms, 0);
const sxx = ok.reduce((a, r) => a + r.plies * r.plies, 0), sxy = ok.reduce((a, r) => a + r.plies * r.ms, 0);
const b = (n * sxy - sx * sy) / (n * sxx - sx * sx), a = (sy - b * sx) / n;
console.log(`fit: ms = ${a.toFixed(0)} + ${b.toFixed(1)} * plies`);
console.log("progress frames p10/50/90", q(ok.map((r) => r.progress), 0.1), q(ok.map((r) => r.progress), 0.5), q(ok.map((r) => r.progress), 0.9));
for (const band of [[0, 40], [40, 80], [80, 120], [120, 999]]) {
  const g = ok.filter((r) => r.plies >= band[0] && r.plies < band[1]);
  if (g.length) console.log(`plies ${band[0]}-${band[1]}: n=${g.length} median ms ${q(g.map((r) => r.ms), 0.5)}`);
}
fs.writeFileSync(path.join(__dirname, "timing.json"), JSON.stringify(rows));
