#!/usr/bin/env python3
"""
Test script for Exercise 2: Convert JSON to YAML
"""

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)


def test_conversion(filename='starter.yaml'):
    """Test the YAML conversion."""
    file_path = Path(__file__).parent / filename

    if not file_path.exists():
        print(f"❌ File not found: {filename}")
        return False

    # Load expected JSON
    json_path = Path(__file__).parent / 'input.json'
    with open(json_path, 'r') as f:
        expected_data = json.load(f)

    # Load YAML solution
    try:
        with open(file_path, 'r') as f:
            yaml_data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error: {e}")
        return False

    # Check structure
    if not isinstance(yaml_data, dict):
        print("❌ Root should be a dictionary/object")
        return False

    if 'database' not in yaml_data:
        print("❌ Missing 'database' key")
        return False

    db = yaml_data['database']
    if not isinstance(db, dict):
        print("❌ 'database' should be a dictionary")
        return False

    # Check fields
    errors = []
    passed = []

    # Check host
    if 'host' not in db:
        errors.append("Missing 'host' field")
    elif db['host'] != 'localhost':
        errors.append(f"Incorrect host: expected 'localhost', got '{db['host']}'")
    else:
        passed.append("Correct database host ✓")

    # Check port
    if 'port' not in db:
        errors.append("Missing 'port' field")
    elif not isinstance(db['port'], int):
        errors.append(f"Port should be a number, got {type(db['port']).__name__}")
    elif db['port'] != 5432:
        errors.append(f"Incorrect port: expected 5432, got {db['port']}")
    else:
        passed.append("Correct port (number) ✓")

    # Check name
    if 'name' not in db:
        errors.append("Missing 'name' field")
    elif db['name'] != 'myapp':
        errors.append(f"Incorrect name: expected 'myapp', got '{db['name']}'")
    else:
        passed.append("Correct database name ✓")

    # Check users list
    if 'users' not in db:
        errors.append("Missing 'users' field")
    elif not isinstance(db['users'], list):
        errors.append(f"Users should be a list, got {type(db['users']).__name__}")
    elif len(db['users']) != 3:
        errors.append(f"Users list should have 3 items, got {len(db['users'])}")
    elif db['users'] != ['admin', 'developer', 'readonly']:
        errors.append(f"Incorrect users list: {db['users']}")
    else:
        passed.append("Correct users list (3 items) ✓")

    # Check for tabs
    with open(file_path, 'r') as f:
        content = f.read()
        if '\t' in content:
            errors.append("File contains tabs! Use spaces only")
        else:
            passed.append("No tabs found (spaces only) ✓")

    # Check for JSON syntax remnants
    with open(file_path, 'r') as f:
        content = f.read()
        json_chars = ['{', '}', '[', ']']
        found_json = [char for char in json_chars if char in content and not content.strip().startswith('#')]
        if found_json:
            errors.append(f"Found JSON syntax characters: {found_json}. Use YAML syntax!")
        else:
            passed.append("Pure YAML syntax (no JSON characters) ✓")

    # Print results
    if passed:
        print("\n✅ Passed checks:")
        for p in passed:
            print(f"  • {p}")

    if errors:
        print("\n❌ Failed checks:")
        for e in errors:
            print(f"  • {e}")
        print(f"\n{len(errors)} error(s) found. Please fix them and try again.")
        return False
    else:
        print("\n🎉 All tests passed! Excellent work!")
        print("\nYour YAML structure:")
        print(yaml.dump(yaml_data, default_flow_style=False, indent=2))

        # Bonus: Show JSON equivalent
        print("\nJSON equivalent:")
        print(json.dumps(yaml_data, indent=2))
        return True


def main():
    """Main entry point."""
    print("=" * 50)
    print("Exercise 2: Convert JSON to YAML - Test Suite")
    print("=" * 50)

    success = test_conversion('starter.yaml')

    if success:
        print("\n✨ Exercise completed! You can now:")
        print("  1. Compare with solution.yaml")
        print("  2. Try the bonus challenge")
        print("  3. Move on to Exercise 3")
        return 0
    else:
        print("\n💡 Tips:")
        print("  • Remove all JSON braces and brackets")
        print("  • Use - for list items")
        print("  • Use 2-space indentation")
        print("  • Check solution.yaml if you're stuck")
        return 1


if __name__ == '__main__':
    sys.exit(main())
