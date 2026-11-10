#!/usr/bin/env python3
"""Experiment only (apply to a scratch copy of backend/, never the repo): replace the order-preserving `buffered` engine
streams in analysis/mod.rs with `buffer_unordered`, then restore the order by index."""
import sys
p = sys.argv[1]
s = open(p).read()
old = """    let searches =
        futures::stream::iter(work.into_iter().chain(threat_work).map(|req| async move {
            let Some(req) = req else { return Ok(None) };
            let analysis = evaluator.analyze(&req, cancel).await?;
            let n = done.fetch_add(1, Ordering::SeqCst) + 1;
            progress(n, total);
            Ok::<_, EngineError>(Some(analysis))
        }))
        .buffered(evaluator.parallelism().max(1))
        .collect::<Vec<_>>()
        .await;"""
new = """    let mut tagged = futures::stream::iter(work.into_iter().chain(threat_work).enumerate().map(
        |(k, req)| async move {
            let Some(req) = req else { return (k, Ok(None)) };
            let r = evaluator.analyze(&req, cancel).await;
            let n = done.fetch_add(1, Ordering::SeqCst) + 1;
            progress(n, total);
            (k, r.map(Some))
        },
    ))
    .buffer_unordered(evaluator.parallelism().max(1))
    .collect::<Vec<(usize, Result<Option<PositionAnalysis>, EngineError>)>>()
    .await;
    tagged.sort_by_key(|(k, _)| *k);
    let searches: Vec<_> = tagged.into_iter().map(|(_, r)| r).collect();"""
assert old in s, "pattern not found"
s = s.replace(old, new)
s = s.replace(".buffered(evaluator.parallelism().max(1))", ".buffer_unordered(evaluator.parallelism().max(1))")
open(p, "w").write(s)
print("patched")
