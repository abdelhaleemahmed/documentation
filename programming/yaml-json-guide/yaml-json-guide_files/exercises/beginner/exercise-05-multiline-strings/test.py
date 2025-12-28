#!/usr/bin/env python3
"""
Test script for Exercise 5: YAML Multiline Strings
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)


def test_multiline_yaml(filename='starter.yaml'):
    """Test the multiline YAML file."""
    file_path = Path(__file__).parent / filename

    if not file_path.exists():
        print(f"❌ File not found: {filename}")
        return False

    # Parse YAML
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error: {e}")
        return False

    errors = []
    passed = []

    # Check structure
    if 'deployment' not in data:
        errors.append("Missing 'deployment' key")
        return False

    deployment = data['deployment']

    # Check name
    if 'name' in deployment and deployment['name'] == 'myapp':
        passed.append("Correct name ✓")
    else:
        errors.append("Missing or incorrect 'name' field")

    # Check description (should be folded into one line)
    if 'description' in deployment:
        desc = deployment['description']
        # Folded text should not have newlines (except maybe trailing)
        desc_clean = desc.strip()
        if '\n' not in desc_clean:
            if 'description' in desc_clean and 'single' in desc_clean:
                passed.append("Description uses > (folded) correctly ✓")
            else:
                passed.append("Description is a single line (good!) ✓")
        else:
            errors.append("Description should use > (folded) to create a single line, not | (literal)")
    else:
        errors.append("Missing 'description' field")

    # Check script (should preserve newlines)
    if 'script' in deployment:
        script = deployment['script']
        # Script should have newlines
        if '\n' in script:
            # Count lines
            lines = [line for line in script.split('\n') if line.strip()]
            if len(lines) >= 4:
                passed.append(f"Script uses | (literal) correctly ({len(lines)} lines preserved) ✓")
            else:
                passed.append("Script preserves newlines ✓")
        else:
            errors.append("Script should use | (literal) to preserve newlines, not > (folded)")
    else:
        errors.append("Missing 'script' field")

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
        print("\n🎉 All tests passed! Perfect multiline strings!")
        print("\nYour parsed data:")
        print("\nDescription (folded):")
        print(f'  "{deployment.get("description", "").strip()}"')
        print("\nScript (literal):")
        for line in deployment.get('script', '').split('\n'):
            if line.strip():
                print(f"  {line}")
        return True


def main():
    """Main entry point."""
    print("=" * 50)
    print("Exercise 5: Multiline Strings - Test Suite")
    print("=" * 50)

    success = test_multiline_yaml('starter.yaml')

    if success:
        print("\n✨ Exercise completed! You can now:")
        print("  1. Compare with solution.yaml")
        print("  2. Move on to intermediate exercises")
        print("\n🎓 You've completed all beginner exercises!")
        return 0
    else:
        print("\n💡 Tips:")
        print("  • Use | (pipe) for literal/preserved newlines")
        print("  • Use > (greater than) for folded/single line")
        print("  • Scripts need | to preserve line breaks")
        print("  • Descriptions can use > to fold lines")
        print("  • Check solution.yaml if stuck")
        return 1


if __name__ == '__main__':
    sys.exit(main())
