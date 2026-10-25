// cachecheck.cjs <run> <e2e-dir-in-wsl-as-windows-path> : do a run's reviews equal fresh reviews?
const fs = require("fs");
const path = require("path");
const [run, dir] = process.argv.slice(2);
const R = path.join(__dirname, "../../tests/calibration/runs", run);
for (const f of fs.readdirSync(dir)) {
  if (!/^\d+\.json$/.test(f) || !fs.existsSync(path.join(R, f))) continue;
  const fresh = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8")).plies;
  const cached = JSON.parse(fs.readFileSync(path.join(R, f), "utf8")).result.plies;
  const canon = (v) => JSON.stringify(v, (k, x) => (x && typeof x === "object" && !Array.isArray(x) ? Object.fromEntries(Object.entries(x).sort()) : x));
  let diffCls = 0, diffEval = 0;
  for (let i = 0; i < fresh.length; i++) {
    if (fresh[i].classification !== cached[i].classification) diffCls++;
    if (canon(fresh[i].lines) !== canon(cached[i].lines) || canon(fresh[i].eval_after) !== canon(cached[i].eval_after)) diffEval++;
  }
  console.log(f, "plies", fresh.length, "class diff", diffCls, "eval diff", diffEval);
}
