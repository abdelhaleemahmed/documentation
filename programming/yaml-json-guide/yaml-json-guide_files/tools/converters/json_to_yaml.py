#!/usr/bin/env python3
"""
JSON to YAML Converter

Converts JSON files to YAML format with proper formatting and error handling.

Usage:
    python json_to_yaml.py input.json [output.yaml]
    python json_to_yaml.py input.json --stdout

Examples:
    python json_to_yaml.py config.json config.yaml
    python json_to_yaml.py data.json --stdout > output.yaml
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML", file=sys.stderr)
    sys.exit(1)


def load_json(file_path: str) -> Any:
    """
    Load JSON file.

    Args:
        file_path: Path to JSON file

    Returns:
        Parsed JSON data

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If JSON is invalid
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON syntax in {file_path}: {e.msg}",
                e.doc,
                e.pos
            )


def convert_to_yaml(data: Any, default_flow_style: bool = False) -> str:
    """
    Convert Python data structure to YAML string.

    Args:
        data: Data to convert
        default_flow_style: Use flow style (inline) for collections

    Returns:
        YAML string
    """
    return yaml.dump(
        data,
        default_flow_style=default_flow_style,
        allow_unicode=True,
        sort_keys=False,
        indent=2
    )


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Convert JSON files to YAML format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s config.json config.yaml
  %(prog)s config.json --stdout > output.yaml
  %(prog)s data.json output.yaml --flow-style
        """
    )
    parser.add_argument('input', help='Input JSON file')
    parser.add_argument('output', nargs='?', help='Output YAML file (optional if --stdout)')
    parser.add_argument('--stdout', action='store_true', help='Print to stdout instead of file')
    parser.add_argument('--flow-style', action='store_true', help='Use flow style (inline collections)')

    args = parser.parse_args()

    # Validate arguments
    if not args.stdout and not args.output:
        parser.error("Output file required (or use --stdout)")

    try:
        # Load JSON
        print(f"Loading JSON from: {args.input}", file=sys.stderr)
        data = load_json(args.input)

        # Convert to YAML
        yaml_str = convert_to_yaml(data, default_flow_style=args.flow_style)

        # Output
        if args.stdout:
            print(yaml_str)
        else:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(yaml_str)
            print(f"✓ Converted successfully: {args.output}", file=sys.stderr)

        return 0

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
