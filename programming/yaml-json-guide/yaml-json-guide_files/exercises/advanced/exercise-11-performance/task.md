# Exercise 11: Performance Comparison

## Objective
Compare YAML vs JSON parsing performance and understand the trade-offs.

## Difficulty
Advanced (⭐⭐⭐)

## What You'll Learn
- Performance characteristics of YAML vs JSON
- Benchmarking techniques
- When performance matters
- Optimization strategies

## Task
Benchmark the parsing speed of YAML vs JSON for the same data.

### Create Performance Test
1. Generate large dataset (1000+ items)
2. Save as both YAML and JSON
3. Measure parse time for each
4. Compare results

## Running the Benchmark
```bash
python benchmark.py
```

## Expected Results
Typical performance (10MB file):
- JSON parsing: ~100ms
- YAML parsing: ~1400ms (10-15x slower)

## Why YAML is Slower
- Complex grammar (multiple syntaxes)
- Indentation parsing
- Anchor resolution
- Type inference
- Multi-line processing

## When Performance Matters
✅ **Use JSON when:**
- High-throughput APIs (1000+ req/sec)
- Large files (>10MB)
- Real-time systems
- Mobile apps (battery/CPU)

✅ **YAML is fine for:**
- Configuration files (read once at startup)
- Small files (<1MB)
- Human-edited files
- CI/CD configs

## Solution
Check `benchmark.py` for the complete implementation.
