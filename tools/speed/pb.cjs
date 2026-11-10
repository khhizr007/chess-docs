// Raw protobuf dump of a chess.com game-review capture's outbound request.
const fs = require("fs");
const path = require("path");

function varint(b, i) {
  let x = 0n, s = 0n;
  for (;;) { const c = b[i++]; x |= BigInt(c & 0x7f) << s; s += 7n; if (!(c & 0x80)) break; }
  return [x, i];
}
// Returns [{f, t, v}] or null if not a valid message.
function parse(b) {
  const out = []; let i = 0;
  try {
    while (i < b.length) {
      let k; [k, i] = varint(b, i); const f = Number(k >> 3n), t = Number(k & 7n);
      if (f === 0) return null;
      if (t === 0) { let v; [v, i] = varint(b, i); out.push({ f, t, v }); }
      else if (t === 1) { out.push({ f, t, v: b.readDoubleLE(i) }); i += 8; }
      else if (t === 5) { out.push({ f, t, v: b.readFloatLE(i) }); i += 4; }
      else if (t === 2) { let n; [n, i] = varint(b, i); n = Number(n); if (i + n > b.length) return null; out.push({ f, t, v: b.subarray(i, i + n) }); i += n; }
      else return null;
    }
  } catch { return null; }
  return out;
}
function dump(b, depth = 0, maxDepth = 12, lines = []) {
  const m = parse(b);
  for (const e of m) {
    const pad = "  ".repeat(depth);
    if (e.t === 2) {
      const sub = depth < maxDepth ? parse(e.v) : null;
      const printable = /^[\x20-\x7e]*$/.test(e.v.toString("latin1"));
      if (printable && e.v.length > 0) lines.push(`${pad}${e.f}: "${e.v.toString("latin1").slice(0, 80)}"`);
      else if (sub && sub.length) { lines.push(`${pad}${e.f} {`); dump(e.v, depth + 1, maxDepth, lines); lines.push(`${pad}}`); }
      else lines.push(`${pad}${e.f}: <${e.v.length} bytes>`);
    } else lines.push(`${pad}${e.f}: ${e.v}`);
  }
  return lines;
}
module.exports = { parse, dump, varint };
if (require.main === module) {
  const file = process.argv[2];
  const cap = JSON.parse(fs.readFileSync(file, "utf8"));
  const s = cap.sockets[0];
  console.log("ms", cap.ms, "in frames", s.in.length);
  const out = Buffer.from(s.out[0].b64, "base64");
  console.log(dump(out).join("\n"));
}
