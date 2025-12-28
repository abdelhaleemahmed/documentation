#!/usr/bin/env python3
"""Test for Exercise 12: Secure Config"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed")
    sys.exit(1)

def test_secure_config():
    """Test that secrets are properly handled."""
    secure_path = Path(__file__).parent / 'secure.yaml'

    if not secure_path.exists():
        print("❌ secure.yaml not found")
        return False

    with open(secure_path, 'r') as f:
        content = f.read()

    # Check for environment variables
    env_vars = re.findall(r'\$\{([A-Z_]+)\}', content)

    if len(env_vars) >= 6:
        print(f"✅ Found {len(env_vars)} environment variables")
    else:
        print(f"❌ Only found {len(env_vars)} environment variables, expected 6+")
        return False

    # Check for hardcoded secrets
    dangerous_patterns = [
        r'password\s*:\s*["\']?[^$\s][^"\'\s]+',
        r'api[_-]?key\s*:\s*["\']?sk_[a-zA-Z0-9]+',
        r'secret\s*:\s*["\']?[^$\s][^"\'\s]+',
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            print("❌ Found potential hardcoded secret!")
            return False

    print("✅ No hardcoded secrets found!")
    print("\n🎉 Configuration is secure!")
    print(f"\nEnvironment variables used: {', '.join(set(env_vars))}")
    return True

if __name__ == '__main__':
    sys.exit(0 if test_secure_config() else 1)
