// ply.cjs <game> <ply> <run>... : one ply's lines, evals and rule in several runs.
const fs = require("fs");
const path = require("path");
const [g, ply, ...runs] = process.argv.slice(2);
const R = path.join(__dirname, "../../tests/calibration/runs");
for (const run of runs) {
  const p = JSON.parse(fs.readFileSync(path.join(R, run, `${g}.json`), "utf8")).result.plies;
  for (const k of [Number(ply) - 1, Number(ply)]) {
    const x = p[k - 1];
    if (!x) continue;
    console.log(`== ${run} ply ${x.ply} ${x.san} ${x.classification} rule=${x.rule} prec=${x.precision} epLost=${x.ep_lost.toFixed(3)} after=${JSON.stringify(x.eval_after)}`);
    for (const l of x.lines) console.log(`   ${l.rank} d${l.depth} ${JSON.stringify(l.eval)} ${l.moves.slice(0, 8).map((m) => m.san).join(" ")}`);
  }
}
