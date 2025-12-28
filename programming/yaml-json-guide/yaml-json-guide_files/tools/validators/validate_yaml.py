#!/usr/bin/env python3
"""
YAML Validator

Validates YAML files for syntax errors and common issues.

Usage:
    python validate_yaml.py file.yaml
    python validate_yaml.py file1.yaml file2.yaml file3.yaml

Examples:
    python validate_yaml.py config.yaml
    python validate_yaml.py **/*.yaml
"""

import argparse
import sys
from pathlib import Path
from typing import Any, List, Tuple

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML", file=sys.stderr)
    sys.exit(1)


def validate_yaml_file(file_path: str, strict: bool = False) -> Tuple[bool, str]:
    """
    Validate a YAML file.

    Args:
        file_path: Path to YAML file
        strict: Enable strict validation

    Returns:
        Tuple of (is_valid, error_message)
    """
    path = Path(file_path)

    if not path.exists():
        return False, f"File not found: {file_path}"

    if not path.is_file():
        return False, f"Not a file: {file_path}"

    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for tabs (common error)
        if '\t' in content:
            lines_with_tabs = [i+1 for i, line in enumerate(content.split('\n')) if '\t' in line]
            return False, f"Tabs found in lines: {lines_with_tabs} (YAML requires spaces only)"

        # Parse YAML
        data = yaml.safe_load(content)

        # Strict checks
        if strict and data is None:
            return False, "File is empty or contains only comments"

        return True, "Valid YAML"

    except yaml.YAMLError as e:
        return False, f"YAML syntax error: {e}"
    except UnicodeDecodeError as e:
        return False, f"Encoding error: {e}"
    except Exception as e:
        return False, f"Unexpected error: {e}"


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate YAML files for syntax errors',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s config.yaml
  %(prog)s file1.yaml file2.yaml
  %(prog)s **/*.yaml --strict
        """
    )
    parser.add_argument('files', nargs='+', help='YAML files to validate')
    parser.add_argument('--strict', action='store_true', help='Enable strict validation')
    parser.add_argument('--quiet', action='store_true', help='Only show errors')

    args = parser.parse_args()

    all_valid = True
    results = []

    for file_path in args.files:
        is_valid, message = validate_yaml_file(file_path, strict=args.strict)
        results.append((file_path, is_valid, message))

        if not is_valid:
            all_valid = False

    # Print results
    for file_path, is_valid, message in results:
        if is_valid:
            if not args.quiet:
                print(f"✓ {file_path}: {message}")
        else:
            print(f"✗ {file_path}: {message}", file=sys.stderr)

    # Summary
    if len(results) > 1:
        valid_count = sum(1 for _, is_valid, _ in results if is_valid)
        total_count = len(results)
        print(f"\n{valid_count}/{total_count} files valid", file=sys.stderr if not all_valid else sys.stdout)

    return 0 if all_valid else 1


if __name__ == '__main__':
    sys.exit(main())
