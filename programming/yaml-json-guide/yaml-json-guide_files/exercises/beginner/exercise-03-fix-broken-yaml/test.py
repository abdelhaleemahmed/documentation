#!/usr/bin/env python3
"""
Test script for Exercise 3: Fix Broken YAML
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)


def test_fixed_yaml(filename='broken.yaml'):
    """Test the fixed YAML file."""
    file_path = Path(__file__).parent / filename

    if not file_path.exists():
        print(f"❌ File not found: {filename}")
        return False

    errors = []
    passed = []

    # Check for tabs
    with open(file_path, 'r') as f:
        content = f.read()
        if '\t' in content:
            errors.append("File contains tabs! Replace tabs with spaces")
        else:
            passed.append("No tabs found (spaces only) ✓")

    # Try to parse YAML
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error: {e}")
        print("\n💡 Tips:")
        print("  • Check for missing colons after keys")
        print("  • Verify indentation (2 spaces per level)")
        print("  • Look for tabs (use spaces only)")
        return False

    # Check structure
    if 'server' not in data:
        errors.append("Missing 'server' key")
        return False

    server = data['server']

    # Check fields
    if 'host' in server and server['host'] == 'localhost':
        passed.append("Correct host ✓")
    else:
        errors.append("Missing or incorrect 'host'")

    if 'port' in server and server['port'] == 8080:
        passed.append("Correct port ✓")
    else:
        errors.append("Missing or incorrect 'port'")

    # Check country (should be string "NO", not boolean)
    if 'country' in server:
        if isinstance(server['country'], str) and server['country'] == "NO":
            passed.append("Correct country (string 'NO') ✓")
        elif server['country'] == False:
            errors.append("Country is boolean false - should be quoted string 'NO'")
        else:
            errors.append(f"Incorrect country value: {server['country']}")
    else:
        errors.append("Missing 'country' field")

    # Check features list
    if 'features' in server:
        if isinstance(server['features'], list):
            if len(server['features']) == 2:
                if 'authentication' in server['features'] and 'caching' in server['features']:
                    passed.append("Correct features list ✓")
                else:
                    errors.append("Features list has wrong items")
            else:
                errors.append(f"Features list should have 2 items, has {len(server['features'])}")
        else:
            errors.append("Features should be a list")
    else:
        errors.append("Missing 'features' field")

    # Print results
    if passed:
        print("\n✅ Passed checks:")
        for p in passed:
            print(f"  • {p}")

    if errors:
        print("\n❌ Failed checks:")
        for e in errors:
            print(f"  • {e}")
        print(f"\n{len(errors)} error(s) remaining. Keep fixing!")
        return False
    else:
        print("\n🎉 All errors fixed! Excellent debugging!")
        print("\nYour fixed YAML:")
        print(yaml.dump(data, default_flow_style=False, indent=2))
        return True


def main():
    """Main entry point."""
    print("=" * 50)
    print("Exercise 3: Fix Broken YAML - Test Suite")
    print("=" * 50)

    success = test_fixed_yaml('broken.yaml')

    if success:
        print("\n✨ Exercise completed! You can now:")
        print("  1. Compare with solution.yaml")
        print("  2. Move on to Exercise 4")
        return 0
    else:
        print("\n💡 Debugging tips:")
        print("  • Use 'cat -A broken.yaml' to see hidden chars")
        print("  • Count spaces carefully (2 per level)")
        print("  • Quote special values like 'NO'")
        print("  • Check solution.yaml if stuck")
        return 1


if __name__ == '__main__':
    sys.exit(main())
