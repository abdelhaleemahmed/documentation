#!/usr/bin/env python3
"""
JSON Validator

Validates JSON files for syntax errors and optionally validates against JSON Schema.

Usage:
    python validate_json.py file.json
    python validate_json.py file.json --schema schema.json
    python validate_json.py file1.json file2.json

Examples:
    python validate_json.py config.json
    python validate_json.py data.json --schema schema.json
    python validate_json.py **/*.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, List, Tuple, Optional

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


def load_json(file_path: str) -> Tuple[bool, Any, str]:
    """
    Load and validate JSON file.

    Args:
        file_path: Path to JSON file

    Returns:
        Tuple of (is_valid, data, error_message)
    """
    path = Path(file_path)

    if not path.exists():
        return False, None, f"File not found: {file_path}"

    if not path.is_file():
        return False, None, f"Not a file: {file_path}"

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return True, data, "Valid JSON"

    except json.JSONDecodeError as e:
        return False, None, f"JSON syntax error at line {e.lineno}, column {e.colno}: {e.msg}"
    except UnicodeDecodeError as e:
        return False, None, f"Encoding error: {e}"
    except Exception as e:
        return False, None, f"Unexpected error: {e}"


def validate_against_schema(data: Any, schema_path: str) -> Tuple[bool, str]:
    """
    Validate JSON data against a schema.

    Args:
        data: Parsed JSON data
        schema_path: Path to JSON Schema file

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not HAS_JSONSCHEMA:
        return False, "jsonschema library not installed. Run: pip install jsonschema"

    try:
        # Load schema
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)

        # Validate
        jsonschema.validate(instance=data, schema=schema)
        return True, "Valid against schema"

    except json.JSONDecodeError as e:
        return False, f"Invalid schema JSON: {e}"
    except jsonschema.ValidationError as e:
        return False, f"Schema validation error: {e.message}"
    except jsonschema.SchemaError as e:
        return False, f"Invalid schema: {e.message}"
    except Exception as e:
        return False, f"Schema validation error: {e}"


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate JSON files and optionally check against JSON Schema',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s config.json
  %(prog)s file1.json file2.json
  %(prog)s data.json --schema schema.json
  %(prog)s **/*.json --quiet
        """
    )
    parser.add_argument('files', nargs='+', help='JSON files to validate')
    parser.add_argument('--schema', help='JSON Schema file for validation')
    parser.add_argument('--quiet', action='store_true', help='Only show errors')

    args = parser.parse_args()

    if args.schema and not HAS_JSONSCHEMA:
        print("Warning: jsonschema not installed. Schema validation disabled.", file=sys.stderr)
        print("Install with: pip install jsonschema", file=sys.stderr)

    all_valid = True
    results = []

    for file_path in args.files:
        # Validate JSON syntax
        is_valid, data, message = load_json(file_path)

        # Validate against schema if provided
        if is_valid and args.schema and HAS_JSONSCHEMA:
            schema_valid, schema_message = validate_against_schema(data, args.schema)
            if not schema_valid:
                is_valid = False
                message = schema_message

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
