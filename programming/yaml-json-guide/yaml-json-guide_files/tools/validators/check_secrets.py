#!/usr/bin/env python3
"""
Secret Scanner

Scans YAML and JSON files for potential secrets and sensitive data.

Usage:
    python check_secrets.py file.yaml
    python check_secrets.py config.yaml data.json

Examples:
    python check_secrets.py config.yaml
    python check_secrets.py **/*.yaml **/*.json
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict

# Patterns for detecting secrets
SECRET_PATTERNS = {
    'password': re.compile(r'password\s*[:=]\s*["\']?([^"\'\s]+)["\']?', re.IGNORECASE),
    'api_key': re.compile(r'api[_-]?key\s*[:=]\s*["\']?([^"\'\s]+)["\']?', re.IGNORECASE),
    'secret': re.compile(r'secret\s*[:=]\s*["\']?([^"\'\s]+)["\']?', re.IGNORECASE),
    'token': re.compile(r'token\s*[:=]\s*["\']?([^"\'\s]+)["\']?', re.IGNORECASE),
    'private_key': re.compile(r'private[_-]?key\s*[:=]\s*["\']?([^"\'\s]+)["\']?', re.IGNORECASE),
    'aws_access_key': re.compile(r'AKIA[0-9A-Z]{16}'),
    'slack_token': re.compile(r'xox[pborsa]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32}'),
    'generic_secret': re.compile(r'-----BEGIN .* PRIVATE KEY-----'),
}

# Safe values that are placeholders or examples
SAFE_VALUES = [
    'your-password',
    'your-secret',
    'your-token',
    'your-api-key',
    'changeme',
    'example',
    'sample',
    'placeholder',
    'xxx',
    'yyy',
    'zzz',
    '******',
    '${',  # Environment variable reference
    '$(',  # Shell substitution
]


def is_safe_value(value: str) -> bool:
    """Check if a value is a safe placeholder."""
    value_lower = value.lower()
    return any(safe in value_lower for safe in SAFE_VALUES)


def scan_file(file_path: str) -> List[Tuple[int, str, str]]:
    """
    Scan a file for potential secrets.

    Args:
        file_path: Path to file

    Returns:
        List of (line_number, secret_type, line_content) tuples
    """
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return []

    findings = []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                # Skip comments
                if line.strip().startswith('#') or line.strip().startswith('//'):
                    continue

                # Check each pattern
                for secret_type, pattern in SECRET_PATTERNS.items():
                    matches = pattern.findall(line)
                    for match in matches:
                        # Extract value from match
                        value = match if isinstance(match, str) else match[0]

                        # Skip if it's a safe placeholder
                        if not is_safe_value(value):
                            findings.append((line_num, secret_type, line.strip()))

    except UnicodeDecodeError:
        pass  # Skip binary files
    except Exception:
        pass  # Skip files we can't read

    return findings


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Scan files for potential secrets and sensitive data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s config.yaml
  %(prog)s file1.yaml file2.json
  %(prog)s **/*.yaml **/*.json --strict

Detected patterns:
  - password, api_key, secret, token
  - private_key, aws_access_key, slack_token
  - PEM-encoded private keys
        """
    )
    parser.add_argument('files', nargs='+', help='Files to scan')
    parser.add_argument('--strict', action='store_true', help='Include placeholder values')

    args = parser.parse_args()

    has_findings = False
    total_findings = 0

    for file_path in args.files:
        findings = scan_file(file_path)

        if findings:
            has_findings = True
            total_findings += len(findings)

            print(f"\n⚠️  {file_path}:", file=sys.stderr)
            for line_num, secret_type, line_content in findings:
                print(f"  Line {line_num} [{secret_type}]: {line_content}", file=sys.stderr)

    # Summary
    if has_findings:
        print(f"\n❌ Found {total_findings} potential secret(s) in {len(args.files)} file(s)", file=sys.stderr)
        print("\nRecommendations:", file=sys.stderr)
        print("  1. Move secrets to environment variables", file=sys.stderr)
        print("  2. Use secret management tools (Vault, AWS Secrets Manager)", file=sys.stderr)
        print("  3. Add .env files to .gitignore", file=sys.stderr)
        print("  4. Use encrypted secrets (SOPS, Sealed Secrets)", file=sys.stderr)
        return 1
    else:
        print(f"✓ No secrets detected in {len(args.files)} file(s)")
        return 0


if __name__ == '__main__':
    sys.exit(main())
