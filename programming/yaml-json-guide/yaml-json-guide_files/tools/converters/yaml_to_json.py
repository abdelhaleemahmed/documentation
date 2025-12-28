#!/usr/bin/env python3
"""
YAML to JSON Converter

Converts YAML files to JSON format with proper formatting and error handling.

Usage:
    python yaml_to_json.py input.yaml [output.json]
    python yaml_to_json.py input.yaml --stdout

Examples:
    python yaml_to_json.py config.yaml config.json
    python yaml_to_json.py config.yaml --stdout > output.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML", file=sys.stderr)
    sys.exit(1)


def load_yaml(file_path: str) -> Any:
    """
    Load YAML file safely.

    Args:
        file_path: Path to YAML file

    Returns:
        Parsed YAML data

    Raises:
        FileNotFoundError: If file doesn't exist
        yaml.YAMLError: If YAML is invalid
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(path, 'r', encoding='utf-8') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Invalid YAML syntax in {file_path}: {e}")


def convert_to_json(data: Any, indent: int = 2) -> str:
    """
    Convert Python data structure to JSON string.

    Args:
        data: Data to convert
        indent: Number of spaces for indentation

    Returns:
        JSON string
    """
    return json.dumps(data, indent=indent, ensure_ascii=False)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Convert YAML files to JSON format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s config.yaml config.json
  %(prog)s config.yaml --stdout > output.json
  %(prog)s input.yaml --indent 4
        """
    )
    parser.add_argument('input', help='Input YAML file')
    parser.add_argument('output', nargs='?', help='Output JSON file (optional if --stdout)')
    parser.add_argument('--stdout', action='store_true', help='Print to stdout instead of file')
    parser.add_argument('--indent', type=int, default=2, help='Indentation spaces (default: 2)')
    parser.add_argument('--compact', action='store_true', help='Compact output (no indentation)')

    args = parser.parse_args()

    # Validate arguments
    if not args.stdout and not args.output:
        parser.error("Output file required (or use --stdout)")

    try:
        # Load YAML
        print(f"Loading YAML from: {args.input}", file=sys.stderr)
        data = load_yaml(args.input)

        # Convert to JSON
        indent = None if args.compact else args.indent
        json_str = convert_to_json(data, indent=indent)

        # Output
        if args.stdout:
            print(json_str)
        else:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(json_str)
            print(f"✓ Converted successfully: {args.output}", file=sys.stderr)

        return 0

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except yaml.YAMLError as e:
        print(f"YAML Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
