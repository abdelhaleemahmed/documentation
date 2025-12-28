#!/usr/bin/env python3
"""
Performance benchmark: YAML vs JSON
"""

import json
import time
import yaml

# Generate test data
def generate_data(num_items=1000):
    """Generate sample data for benchmarking."""
    return {
        "users": [
            {
                "id": i,
                "name": f"User {i}",
                "email": f"user{i}@example.com",
                "active": i % 2 == 0,
                "metadata": {
                    "created": "2024-01-01",
                    "updated": "2024-01-15",
                    "tags": ["tag1", "tag2", "tag3"]
                }
            }
            for i in range(num_items)
        ]
    }

def benchmark_yaml(data, iterations=10):
    """Benchmark YAML parsing."""
    # Write to file
    yaml_str = yaml.dump(data)

    times = []
    for _ in range(iterations):
        start = time.time()
        yaml.safe_load(yaml_str)
        times.append(time.time() - start)

    return sum(times) / len(times), len(yaml_str)

def benchmark_json(data, iterations=10):
    """Benchmark JSON parsing."""
    # Write to file
    json_str = json.dumps(data)

    times = []
    for _ in range(iterations):
        start = time.time()
        json.loads(json_str)
        times.append(time.time() - start)

    return sum(times) / len(times), len(json_str)

def main():
    print("=" * 60)
    print("YAML vs JSON Performance Benchmark")
    print("=" * 60)

    for num_items in [100, 500, 1000]:
        print(f"\n Testing with {num_items} items:")
        data = generate_data(num_items)

        yaml_time, yaml_size = benchmark_yaml(data)
        json_time, json_size = benchmark_json(data)

        print(f"  YAML: {yaml_time*1000:.2f}ms | Size: {yaml_size/1024:.1f}KB")
        print(f"  JSON: {json_time*1000:.2f}ms | Size: {json_size/1024:.1f}KB")
        print(f"  Speedup: {yaml_time/json_time:.1f}x faster with JSON")

    print("\n" + "=" * 60)
    print("Conclusion: JSON is significantly faster for parsing")
    print("=" * 60)

if __name__ == '__main__':
    main()
