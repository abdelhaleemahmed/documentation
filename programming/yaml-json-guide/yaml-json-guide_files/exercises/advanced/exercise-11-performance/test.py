#!/usr/bin/env python3
"""Test for Exercise 11"""

import subprocess
import sys

def test_benchmark():
    """Run the benchmark."""
    try:
        result = subprocess.run(
            [sys.executable, 'benchmark.py'],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            print("✅ Benchmark completed successfully!")
            print(result.stdout)
            return True
        else:
            print(f"❌ Benchmark failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error running benchmark: {e}")
        return False

if __name__ == '__main__':
    sys.exit(0 if test_benchmark() else 1)
