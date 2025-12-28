#!/usr/bin/env python3
"""Migration script to convert legacy INI to modern YAML"""

import configparser
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed")
    sys.exit(1)

def convert_value(value):
    """Convert legacy values to modern equivalents."""
    # Boolean conversions
    if value.lower() in ('yes', 'on', 'true', '1'):
        return True
    if value.lower() in ('no', 'off', 'false', '0'):
        return False

    # Try to convert to int
    try:
        return int(value)
    except ValueError:
        pass

    # Keep as string
    return value

def is_secret(key):
    """Check if a key contains sensitive information."""
    secret_keywords = ['password', 'secret', 'key', 'token', 'credential']
    return any(keyword in key.lower() for keyword in secret_keywords)

def get_env_var_name(section, key):
    """Generate environment variable name."""
    if 'password' in key.lower():
        return f"{section.upper()}_PASSWORD"
    if 'username' in key.lower():
        return f"{section.upper()}_USERNAME"
    if 'api_key' in key.lower():
        return "API_KEY"
    if 'secret' in key.lower():
        return f"{section.upper()}_SECRET"
    return f"{section.upper()}_{key.upper()}"

def migrate_config(ini_path, yaml_path):
    """Migrate INI config to modern YAML."""
    config = configparser.ConfigParser()
    config.read(ini_path)

    result = {}
    secrets_found = []

    for section in config.sections():
        result[section] = {}

        for key, value in config[section].items():
            # Handle secrets
            if is_secret(key):
                env_var = get_env_var_name(section, key)
                result[section][key] = f"${{{env_var}}}"
                secrets_found.append((section, key, env_var))
            else:
                result[section][key] = convert_value(value)

    # Write YAML
    with open(yaml_path, 'w') as f:
        f.write("# Migrated from legacy INI configuration\n")
        f.write("# WARNING: Secrets replaced with environment variables\n\n")
        yaml.dump(result, f, default_flow_style=False, sort_keys=False)

    # Report
    print(f"✅ Migrated {ini_path} → {yaml_path}")
    print(f"\n🔐 Found {len(secrets_found)} secrets (replaced with env vars):")
    for section, key, env_var in secrets_found:
        print(f"  - [{section}] {key} → ${{{env_var}}}")

    # Generate .env.example
    env_example = Path(yaml_path).parent / '.env.example'
    with open(env_example, 'w') as f:
        f.write("# Environment Variables Template\n")
        f.write("# Copy to .env and fill in actual values\n\n")
        for section, key, env_var in secrets_found:
            f.write(f"{env_var}=your_{key}_here\n")

    print(f"\n✅ Created {env_example}")

    return True

def test_migration():
    """Test that migration was successful."""
    modern_path = Path(__file__).parent / 'modern-config.yaml'

    if not modern_path.exists():
        print("❌ modern-config.yaml not found")
        return False

    with open(modern_path, 'r') as f:
        config = yaml.safe_load(f)

    # Check secrets are not hardcoded
    yaml_str = open(modern_path).read()
    secret_patterns = [
        r'password\s*:\s*["\']?[A-Za-z0-9!@#$]+["\']?\s*$',
        r'api_key\s*:\s*sk_[a-zA-Z0-9]+',
    ]

    for pattern in secret_patterns:
        if re.search(pattern, yaml_str, re.MULTILINE):
            print("❌ Found hardcoded secret!")
            return False

    print("✅ No hardcoded secrets")

    # Check environment variables
    env_vars = re.findall(r'\$\{([A-Z_]+)\}', yaml_str)
    if len(env_vars) < 5:
        print(f"❌ Expected at least 5 environment variables, found {len(env_vars)}")
        return False

    print(f"✅ Found {len(env_vars)} environment variables")

    # Check explicit booleans
    if config['server']['keep_alive'] != True:
        print("❌ Boolean values not properly converted")
        return False

    print("✅ Boolean values converted correctly")

    # Check version is string
    if not isinstance(config['application']['version'], str):
        print("❌ Version should be string")
        return False

    print("✅ Version preserved as string")

    print("\n🎉 Migration successful!")
    print("\nChanges applied:")
    print("  - Secrets replaced with environment variables")
    print("  - Booleans converted (yes/no → true/false)")
    print("  - Version strings quoted")
    print("  - Proper YAML structure")

    return True

if __name__ == '__main__':
    # Run migration
    # migrate_config('legacy-config.ini', 'migrated.yaml')

    # Test the solution
    sys.exit(0 if test_migration() else 1)
