#!/usr/bin/env python3
"""
Test script for Exercise 1: Your First YAML File
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)


def test_yaml_file(filename='starter.yaml'):
    """Test the YAML file for correctness."""
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

    # Check structure
    if not isinstance(data, dict):
        print("❌ Root should be a dictionary/object")
        return False

    if 'app' not in data:
        print("❌ Missing 'app' key")
        return False

    app = data['app']
    if not isinstance(app, dict):
        print("❌ 'app' should be a dictionary")
        return False

    # Check required fields
    errors = []
    passed = []

    # Check name
    if 'name' not in app:
        errors.append("Missing 'name' field")
    elif app['name'] != "MyFirstApp":
        errors.append(f"Incorrect name: expected 'MyFirstApp', got '{app['name']}'")
    else:
        passed.append("Correct app name ✓")

    # Check version
    if 'version' not in app:
        errors.append("Missing 'version' field")
    elif app['version'] != "1.0.0":
        errors.append(f"Incorrect version: expected '1.0.0', got '{app['version']}'")
    else:
        passed.append("Correct version ✓")

    # Check port
    if 'port' not in app:
        errors.append("Missing 'port' field")
    elif not isinstance(app['port'], int):
        errors.append(f"Port should be a number, got {type(app['port']).__name__}")
    elif app['port'] != 3000:
        errors.append(f"Incorrect port: expected 3000, got {app['port']}")
    else:
        passed.append("Correct port (number) ✓")

    # Check debug
    if 'debug' not in app:
        errors.append("Missing 'debug' field")
    elif not isinstance(app['debug'], bool):
        errors.append(f"Debug should be a boolean, got {type(app['debug']).__name__}")
    elif app['debug'] is not True:
        errors.append(f"Incorrect debug value: expected true, got {app['debug']}")
    else:
        passed.append("Correct debug flag (boolean) ✓")

    # Check for tabs
    with open(file_path, 'r') as f:
        content = f.read()
        if '\t' in content:
            errors.append("File contains tabs! Use spaces only for indentation")
        else:
            passed.append("No tabs found (spaces only) ✓")

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
        print("\n🎉 All tests passed! Great job!")
        print("\nYour YAML structure:")
        print(yaml.dump(data, default_flow_style=False, indent=2))
        return True


def main():
    """Main entry point."""
    print("=" * 50)
    print("Exercise 1: Your First YAML File - Test Suite")
    print("=" * 50)

    success = test_yaml_file('starter.yaml')

    if success:
        print("\n✨ Exercise completed! You can now:")
        print("  1. Compare with solution.yaml")
        print("  2. Move on to Exercise 2")
        return 0
    else:
        print("\n💡 Tips:")
        print("  • Use 2 spaces for indentation")
        print("  • Don't quote numbers or booleans")
        print("  • Check solution.yaml if you're stuck")
        return 1


if __name__ == '__main__':
    sys.exit(main())
