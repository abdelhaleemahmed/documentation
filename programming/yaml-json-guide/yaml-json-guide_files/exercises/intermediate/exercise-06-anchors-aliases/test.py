#!/usr/bin/env python3
"""Test script for Exercise 6: Anchors & Aliases"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)


def test_anchors(filename='starter.yaml'):
    """Test the anchors and aliases."""
    file_path = Path(__file__).parent / filename

    if not file_path.exists():
        print(f"❌ File not found: {filename}")
        return False

    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error: {e}")
        return False

    errors = []
    passed = []

    # Check for environments
    for env in ['development', 'staging', 'production']:
        if env not in data:
            errors.append(f"Missing '{env}' environment")
            continue

        if 'database' not in data[env]:
            errors.append(f"Missing 'database' in {env}")
            continue

        db = data[env]['database']

        # Check merged defaults
        if db.get('timeout') == 30 and db.get('retries') == 3 and db.get('pool_size') == 10:
            passed.append(f"{env}: defaults merged correctly ✓")
        else:
            errors.append(f"{env}: defaults not properly merged")

        # Check environment-specific values
        if env == 'development' and db.get('host') == 'localhost':
            passed.append(f"{env}: has correct host ✓")

    # Print results
    if passed:
        print("\n✅ Passed checks:")
        for p in passed:
            print(f"  • {p}")

    if errors:
        print("\n❌ Failed checks:")
        for e in errors:
            print(f"  • {e}")
        return False
    else:
        print("\n🎉 Perfect! Anchors and aliases working correctly!")
        return True


if __name__ == '__main__':
    sys.exit(0 if test_anchors() else 1)
