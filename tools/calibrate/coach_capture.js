// Phase 0 capture of Chess.com Game Review coach output (docs/calibration/coach-log.md).
//
// Run in the browser console (or a browser automation tool) on any signed-in
// https://www.chess.com/analysis/... page, with Game Review set to engine Stockfish. For each game it
// opens the game's review page in a hidden same-origin iframe, wraps that frame's WebSocket before
// the page's scripts start, and keeps the binary frames of the `/v2/game-review` socket: the request
// the page itself sends and the GameReviewResponse. Nothing is sent beyond what opening each
// review page sends; games are opened one at a time with a pause in between.
//
// The frames stay in the page (window.__caps) until pulled with `coachPull()`, which returns them as
// one JSON string `{"caps": [...]}`. Save that outside the repository and turn it into
// <captures>/raw/<id>.json with `coach_oracle.py ingest`. The frames contain Chess.com text: never
// commit them.
//
//   coachStart([["185058622904", "live"], ["1011026868", "daily"]]);
//   coachStatus();   // {done, ok, failed, running}
//   coachPull();     // frames captured since the last pull
//   await coachPullGz(40);  // the same, gzipped: "GZ1:<base64>|" padded past the size at which a tool
//                           // result is saved to disk instead of entering the transcript (batch 5)
//
// The review engine comes from the page's cached settings (localStorage `json_settings`,
// `fullAnalysisEngine`). A page load can refresh that cache from the server and switch it back to
// Torch, so before each game the cached value is set back to Stockfish. Check every capture's score
// engines anyway (13 = Stockfish 18, 11 = Torch).
//
// When the browser pane is hidden, timers are throttled and a timer-driven hook can attach after the
// app has opened its socket. The hook therefore polls on a MessageChannel, which is not throttled,
// until it is installed.

(() => {
  const isBin = (x) => x && typeof x === "object" && typeof x.byteLength === "number";
  const size = (x) => (isBin(x) ? x.byteLength : String(x).length);
  const b64 = (buf) => {
    const u = new Uint8Array(buf);
    let s = "";
    for (let i = 0; i < u.length; i += 0x8000) s += String.fromCharCode.apply(null, u.subarray(i, i + 0x8000));
    return btoa(s);
  };

  function capture(path, timeoutMs) {
    return new Promise((resolve) => {
      const rec = { path, sockets: [] };
      const ifr = document.createElement("iframe");
      ifr.style.cssText =
        "position:fixed;left:0;top:0;width:1200px;height:900px;opacity:0.01;pointer-events:none;z-index:-1";
      // Wrap the iframe's WebSocket as soon as its document exists (before the app creates sockets).
      const hook = () => {
        let w;
        try {
          w = ifr.contentWindow;
          if (!w || w.__coachHooked || !w.WebSocket || w.location.href === "about:blank") return;
        } catch (e) {
          return;
        }
        const Orig = w.WebSocket;
        function Wrapped(url, protocols) {
          const ws = protocols === undefined ? new Orig(url) : new Orig(url, protocols);
          if (String(url).includes("game-review")) {
            const s = { url: String(url), out: [], in: [] };
            rec.sockets.push(s);
            const send = ws.send.bind(ws);
            ws.send = (d) => {
              try {
                s.out.push(isBin(d) ? (d.buffer ? d.buffer.slice(d.byteOffset, d.byteOffset + d.byteLength) : d.slice(0)) : d);
              } catch (e) {}
              return send(d);
            };
            ws.addEventListener("message", (ev) => {
              const d = ev.data;
              if (d && typeof d.arrayBuffer === "function" && !isBin(d)) d.arrayBuffer().then((b) => s.in.push(b));
              else s.in.push(isBin(d) ? d.slice(0) : d);
            });
          }
          return ws;
        }
        Wrapped.prototype = Orig.prototype;
        Object.assign(Wrapped, { CONNECTING: 0, OPEN: 1, CLOSING: 2, CLOSED: 3 });
        w.WebSocket = Wrapped;
        w.__coachHooked = true;
      };
      let stopHook = false;
      const hookTimer = setInterval(hook, 50);
      const mc = new MessageChannel();
      mc.port1.onmessage = () => {
        hook();
        let hooked = false;
        try {
          hooked = !!ifr.contentWindow.__coachHooked;
        } catch (e) {}
        if (!stopHook && !hooked) mc.port2.postMessage(0);
      };
      mc.port2.postMessage(0);
      ifr.src = path;
      document.body.appendChild(ifr);
      const t0 = Date.now();
      const doneTimer = setInterval(() => {
        // The review arrives as one large frame after a few small progress frames.
        const big = rec.sockets.some((s) => s.in.some((x) => size(x) > 2000));
        if (big || Date.now() - t0 > timeoutMs) {
          stopHook = true;
          clearInterval(hookTimer);
          clearInterval(doneTimer);
          setTimeout(() => {
            rec.ms = Date.now() - t0;
            rec.ok = big;
            ifr.remove();
            resolve(rec);
          }, big ? 2000 : 0);
        }
      }, 250);
    });
  }

  window.__caps = window.__caps || {};
  window.__pulled = window.__pulled || {};

  window.coachStart = async (games, { pauseMs = 3000, timeoutMs = 90000 } = {}) => {
    if (window.__coachRunning) return "already running";
    window.__coachRunning = true;
    window.__coachStop = false;
    for (const [id, kind] of games) {
      if (window.__coachStop) break;
      if (window.__caps[id] && window.__caps[id].ok) continue;
      const js = localStorage.getItem("json_settings");
      if (js && js.includes('"fullAnalysisEngine":"torch-human"')) {
        localStorage.setItem(
          "json_settings",
          js.replace('"fullAnalysisEngine":"torch-human"', '"fullAnalysisEngine":"stockfish16 nnue"'),
        );
      }
      const rec = await capture(`/analysis/game/${kind}/${id}/review`, timeoutMs);
      window.__caps[id] = {
        id,
        kind,
        path: rec.path,
        ok: rec.ok,
        ms: rec.ms,
        captured_at: new Date().toISOString(),
        sockets: rec.sockets.map((s) => ({
          url: s.url,
          out: s.out.map((x) => (isBin(x) ? { b64: b64(x) } : { text: String(x) })),
          in: s.in.map((x) => (isBin(x) ? { b64: b64(x) } : { text: String(x) })),
        })),
      };
      await new Promise((r) => setTimeout(r, pauseMs));
    }
    window.__coachRunning = false;
    return "done";
  };

  window.coachStatus = () => {
    const caps = Object.values(window.__caps);
    return {
      done: caps.length,
      ok: caps.filter((c) => c.ok).length,
      failed: caps.filter((c) => !c.ok).map((c) => c.id),
      running: !!window.__coachRunning,
    };
  };

  window.coachPull = () => {
    const ids = Object.keys(window.__caps).filter((i) => window.__caps[i].ok && !window.__pulled[i]);
    ids.forEach((i) => (window.__pulled[i] = 1));
    return JSON.stringify({ caps: ids.map((i) => window.__caps[i]) });
  };

  window.coachPullGz = async (max = 40, pad = 130000) => {
    const ids = Object.keys(window.__caps)
      .filter((i) => window.__caps[i].ok && !window.__pulled[i])
      .slice(0, max);
    const json = JSON.stringify({ caps: ids.map((i) => window.__caps[i]) });
    const gz = await new Response(
      new Blob([json]).stream().pipeThrough(new CompressionStream("gzip")),
    ).arrayBuffer();
    ids.forEach((i) => (window.__pulled[i] = 1));
    const out = "GZ1:" + b64(gz) + "|";
    return out.length < pad ? out + ".".repeat(pad - out.length) : out;
  };
})();
