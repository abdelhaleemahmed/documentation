#!/usr/bin/env python3
"""
Test script for Exercise 4: JSON Arrays
"""

import json
import sys
from pathlib import Path


def test_json_array(filename='starter.json'):
    """Test the JSON array file."""
    file_path = Path(__file__).parent / filename

    if not file_path.exists():
        print(f"❌ File not found: {filename}")
        return False

    # Parse JSON
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSON syntax error: {e}")
        print("\n💡 Common JSON errors:")
        print("  • Trailing comma after last item")
        print("  • Single quotes instead of double quotes")
        print("  • Missing commas between items")
        return False

    errors = []
    passed = []

    # Check root is array
    if not isinstance(data, list):
        errors.append("Root element should be an array []")
        return False
    else:
        passed.append("Root is an array ✓")

    # Check array length
    if len(data) != 3:
        errors.append(f"Array should have 3 users, has {len(data)}")
    else:
        passed.append("Array has 3 users ✓")

    # Check each user
    expected_users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com", "active": True},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "active": False},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com", "active": True}
    ]

    for i, expected in enumerate(expected_users):
        if i >= len(data):
            errors.append(f"Missing user {i+1}")
            continue

        user = data[i]

        # Check structure
        if not isinstance(user, dict):
            errors.append(f"User {i+1} should be an object")
            continue

        # Check fields
        for key, expected_value in expected.items():
            if key not in user:
                errors.append(f"User {i+1}: missing '{key}' field")
            elif user[key] != expected_value:
                errors.append(f"User {i+1}: incorrect {key} (expected {expected_value}, got {user[key]})")
            elif key == 'id' and not isinstance(user[key], int):
                errors.append(f"User {i+1}: 'id' should be a number, not string")
            elif key == 'active' and not isinstance(user[key], bool):
                errors.append(f"User {i+1}: 'active' should be boolean, not string")

        if not errors or all(key in user and user[key] == expected[key] for key in expected):
            passed.append(f"User {i+1} ({expected['name']}) correct ✓")

    # Print results
    if passed:
        print("\n✅ Passed checks:")
        for p in passed:
            print(f"  • {p}")

    if errors:
        print("\n❌ Failed checks:")
        for e in errors:
            print(f"  • {e}")
        print(f"\n{len(errors)} error(s) found.")
        return False
    else:
        print("\n🎉 All tests passed! Perfect JSON array!")
        print("\nYour data:")
        print(json.dumps(data, indent=2))
        return True


def main():
    """Main entry point."""
    print("=" * 50)
    print("Exercise 4: JSON Arrays - Test Suite")
    print("=" * 50)

    success = test_json_array('starter.json')

    if success:
        print("\n✨ Exercise completed! You can now:")
        print("  1. Compare with solution.json")
        print("  2. Move on to Exercise 5")
        return 0
    else:
        print("\n💡 Tips:")
        print("  • Arrays use square brackets []")
        print("  • Objects use curly braces {}")
        print("  • No trailing commas in JSON")
        print("  • Use double quotes only")
        print("  • Check solution.json if stuck")
        return 1


if __name__ == '__main__':
    sys.exit(main())
