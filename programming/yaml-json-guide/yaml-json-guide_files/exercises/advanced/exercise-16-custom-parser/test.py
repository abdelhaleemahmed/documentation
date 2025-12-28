#!/usr/bin/env python3
"""Test for Exercise 16: Custom Parser"""

import os
import sys
from pathlib import Path

# Import the parser
try:
    from parser import ConfigParser, ConfigValidationError
except ImportError:
    print("❌ Could not import ConfigParser from parser.py")
    sys.exit(1)


def test_env_var_expansion():
    """Test environment variable expansion."""
    print("Testing environment variable expansion...")

    # Set test environment variables
    os.environ['DB_HOST'] = 'prod.db.example.com'
    os.environ['DB_PASSWORD'] = 'secret123'
    os.environ['API_KEY'] = 'sk_test_abc123'

    parser = ConfigParser()
    config_path = Path(__file__).parent / 'config.yaml'

    try:
        config = parser.parse(str(config_path))
    except Exception as e:
        print(f"❌ Failed to parse config: {e}")
        return False

    # Check expansions
    if config['database']['host'] != 'prod.db.example.com':
        print(f"❌ DB_HOST not expanded correctly: {config['database']['host']}")
        return False

    if config['database']['password'] != 'secret123':
        print(f"❌ DB_PASSWORD not expanded correctly")
        return False

    print("✅ Environment variables expanded correctly")
    return True


def test_default_values():
    """Test default values in env vars."""
    print("\nTesting default values...")

    # Unset CACHE_HOST to test default
    os.environ.pop('CACHE_HOST', None)

    parser = ConfigParser()
    config_path = Path(__file__).parent / 'config.yaml'

    try:
        config = parser.parse(str(config_path))
    except Exception as e:
        print(f"❌ Failed to parse config: {e}")
        return False

    # Check default value
    if config['cache']['host'] != 'localhost':
        print(f"❌ Default value not used: {config['cache']['host']}")
        return False

    print("✅ Default values work correctly")
    return True


def test_validation():
    """Test schema validation."""
    print("\nTesting validation...")

    schema = {
        'database': {
            'required': True,
            'type': dict,
            'schema': {
                'host': {'required': True, 'type': str},
                'port': {'required': True, 'type': int, 'min': 1, 'max': 65535}
            }
        },
        'server': {
            'required': True,
            'type': dict,
            'schema': {
                'port': {'required': True, 'type': int, 'min': 1024, 'max': 65535}
            }
        }
    }

    parser = ConfigParser(schema=schema)
    config_path = Path(__file__).parent / 'config.yaml'

    try:
        config = parser.parse(str(config_path))
        print("✅ Validation passed")
        return True
    except ConfigValidationError as e:
        print(f"❌ Validation failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def test_missing_env_var():
    """Test handling of missing environment variables."""
    print("\nTesting missing environment variable handling...")

    # Unset required var
    os.environ.pop('DB_USERNAME', None)

    parser = ConfigParser()
    config_path = Path(__file__).parent / 'config.yaml'

    try:
        config = parser.parse(str(config_path))
        # Should raise error for missing DB_USERNAME
        print("❌ Should have raised error for missing DB_USERNAME")
        return False
    except Exception as e:
        if 'DB_USERNAME' in str(e):
            print("✅ Correctly detected missing environment variable")
            return True
        else:
            print(f"❌ Wrong error: {e}")
            return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Testing Custom Configuration Parser")
    print("=" * 60)

    # Set all required env vars for first tests
    os.environ['DB_HOST'] = 'prod.db.example.com'
    os.environ['DB_USERNAME'] = 'admin'
    os.environ['DB_PASSWORD'] = 'secret123'
    os.environ['API_KEY'] = 'sk_test_abc123'
    os.environ['LOG_LEVEL'] = 'DEBUG'

    tests = [
        test_env_var_expansion,
        test_default_values,
        test_validation,
        test_missing_env_var,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test crashed: {e}")
            failed += 1

    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)

    if failed == 0:
        print("\n🎉 All tests passed!")
        print("\nFeatures implemented:")
        print("  ✓ Environment variable expansion")
        print("  ✓ Default values (${VAR:-default})")
        print("  ✓ Schema validation")
        print("  ✓ Type checking")
        print("  ✓ Range validation")
        print("  ✓ Error handling")
        return True
    else:
        print(f"\n❌ {failed} test(s) failed")
        return False


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
