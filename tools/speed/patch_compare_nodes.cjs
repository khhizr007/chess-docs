// One-off: add --nodes to compare.py.
const fs = require("fs");
const f = process.argv[2];
let s = fs.readFileSync(f, "utf8");
const rep = (a, b) => {
  if (!s.includes(a)) throw new Error("missing " + a);
  s = s.replace(a, b);
};
rep(
  `body = {"pgn": pgn, "depth": self.args.depth, "multipv": self.args.multipv}`,
  `body = {"pgn": pgn, "multipv": self.args.multipv}
        if self.args.nodes:
            body["nodes"] = self.args.nodes
        else:
            body["depth"] = self.args.depth`,
);
rep(
  `if limit.get("depth") != self.args.depth or settings.get("multipv")`,
  `want = {"nodes": self.args.nodes} if self.args.nodes else {"depth": self.args.depth}
        if any(limit.get(k) != v for k, v in want.items()) or settings.get("multipv")`,
);
rep(`expected depth {self.args.depth} "`, `expected {want} "`);
rep(
  `settings = {"depth": args.depth, "multipv": args.multipv, "config": args.config_override}`,
  `settings = {"depth": args.depth, "multipv": args.multipv, "config": args.config_override}
        if args.nodes:
            settings = {"nodes": args.nodes, "multipv": args.multipv, "config": args.config_override}`,
);
rep(
  `    p.add_argument("--multipv"`,
  `    p.add_argument("--nodes", type=int, default=None,
                   help="node budget per position, replacing --depth")
    p.add_argument("--multipv"`,
);
rep(
  `depth {s['depth']}, multipv {s['multipv']}; "`,
  `{'nodes ' + str(s['nodes']) if s.get('nodes') else 'depth ' + str(s['depth'])}, multipv {s['multipv']}; "`,
);
fs.writeFileSync(f, s);
console.log("ok");
