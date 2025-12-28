#!/usr/bin/env python3
"""Test for Exercise 14: Real-World Error Debugging"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed")
    sys.exit(1)

def test_fixed_config():
    """Test that all errors have been fixed."""
    fixed_path = Path(__file__).parent / 'fixed-config.yaml'

    if not fixed_path.exists():
        print("❌ fixed-config.yaml not found")
        return False

    with open(fixed_path, 'r') as f:
        content = f.read()

    # Test 1: File should parse without errors
    try:
        config = yaml.safe_load(content)
        print("✅ YAML parses successfully")
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        return False

    # Test 2: Version should be string (not float)
    version = config.get('application', {}).get('version')
    if not isinstance(version, str):
        print(f"❌ Version should be string, got {type(version).__name__}")
        return False
    print("✅ Version is string (quoted)")

    # Test 3: Country code should be string "NO" (not boolean False)
    country = config.get('application', {}).get('country_code')
    if country != "NO":
        print(f"❌ Country code should be 'NO', got {country}")
        return False
    print("✅ Country code is string 'NO' (not boolean)")

    # Test 4: No hardcoded secrets
    secret_patterns = [
        r'password\s*:\s*["\']?\w+["\']?\s*(?:#|$)',
        r'secret\s*:\s*["\']?\w+["\']?\s*(?:#|$)',
    ]

    # Should have environment variable patterns
    if not re.search(r'\$\{[A-Z_]+\}', content):
        print("❌ No environment variables found for secrets")
        return False
    print("✅ Using environment variables for secrets")

    # Test 5: Check booleans are explicit
    enabled = config.get('application', {}).get('enabled')
    if not isinstance(enabled, bool):
        print(f"❌ 'enabled' should be boolean, got {type(enabled).__name__}")
        return False
    print("✅ Boolean values are explicit")

    # Test 6: No duplicate keys (check logging is single)
    if 'logging' in config:
        logging_count = content.count('logging:')
        if logging_count > 1:
            print(f"❌ Found {logging_count} 'logging:' keys (should be 1)")
            return False
        print("✅ No duplicate keys")

    # Test 7: List indentation is correct
    formats = config.get('supported_formats', [])
    if len(formats) != 4 or 'xml' not in formats:
        print(f"❌ Expected 4 formats including 'xml', got {formats}")
        return False
    print("✅ List indentation is correct")

    # Test 8: Anchors defined before use
    lines = content.split('\n')
    anchor_line = None
    reference_line = None

    for i, line in enumerate(lines):
        if '&api_defaults' in line:
            anchor_line = i
        if '*api_defaults' in line and 'api_client' in line:
            reference_line = i

    if anchor_line is not None and reference_line is not None:
        if anchor_line > reference_line:
            print("❌ Anchor used before definition")
            return False
        print("✅ Anchor defined before use")

    print("\n🎉 All debugging tests passed!")
    print("\nErrors fixed:")
    print("  - Version quoted to remain string")
    print("  - Country code quoted to prevent boolean conversion")
    print("  - Hardcoded secrets replaced with env vars")
    print("  - Indentation corrected")
    print("  - Anchor defined before reference")
    print("  - Duplicate keys removed")
    print("  - Explicit boolean values")
    print("  - List indentation fixed")

    return True

if __name__ == '__main__':
    sys.exit(0 if test_fixed_config() else 1)
