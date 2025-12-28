#!/usr/bin/env python3
"""Test script for Exercise 10: Boolean Types"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)


def test_boolean_types(filename='starter.yaml'):
    """Test boolean type handling."""
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

    if 'settings' not in data:
        print("❌ Missing 'settings' key")
        return False

    settings = data['settings']

    # Check booleans
    if settings.get('debug') is True:
        passed.append("debug is boolean true ✓")
    else:
        errors.append("debug should be boolean true")

    if settings.get('ssl') is False:
        passed.append("ssl is boolean false ✓")
    else:
        errors.append("ssl should be boolean false")

    # Check strings (not booleans!)
    if isinstance(settings.get('country_code'), str) and settings['country_code'] == "NO":
        passed.append("country_code is string 'NO' ✓")
    else:
        errors.append("country_code should be string 'NO', not boolean")

    if isinstance(settings.get('answer'), str) and settings['answer'] == "no":
        passed.append("answer is string 'no' ✓")
    else:
        errors.append("answer should be string 'no', not boolean")

    if isinstance(settings.get('status'), str) and settings['status'] == "on":
        passed.append("status is string 'on' ✓")
    else:
        errors.append("status should be string 'on', not boolean")

    # Check flags array
    if 'flags' in settings and len(settings['flags']) == 4:
        flags = settings['flags']

        # flags[0] should be boolean true
        if flags[0] is True:
            passed.append("flags[0] is boolean true ✓")
        else:
            errors.append("flags[0] should be boolean true")

        # flags[1] should be string "yes"
        if isinstance(flags[1], str) and flags[1] == "yes":
            passed.append("flags[1] is string 'yes' ✓")
        else:
            errors.append("flags[1] should be string 'yes'")

        # flags[2] should be boolean false
        if flags[2] is False:
            passed.append("flags[2] is boolean false ✓")
        else:
            errors.append("flags[2] should be boolean false")

        # flags[3] should be string "no"
        if isinstance(flags[3], str) and flags[3] == "no":
            passed.append("flags[3] is string 'no' ✓")
        else:
            errors.append("flags[3] should be string 'no'")

    # Print results
    if passed:
        print("\n✅ Passed checks:")
        for p in passed:
            print(f"  • {p}")

    if errors:
        print("\n❌ Failed checks:")
        for e in errors:
            print(f"  • {e}")
        print("\n💡 Remember: Quote strings like 'NO', 'yes', 'on' to prevent boolean conversion!")
        return False
    else:
        print("\n🎉 Perfect! You've mastered YAML boolean types!")
        print("\n✨ All intermediate exercises complete!")
        return True


if __name__ == '__main__':
    sys.exit(0 if test_boolean_types() else 1)
