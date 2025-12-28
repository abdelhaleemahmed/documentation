#!/usr/bin/env python3
"""Test script for Exercise 7: Schema Validation"""

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Error: jsonschema is not installed. Run: pip install jsonschema")
    sys.exit(1)


def test_schema_validation():
    """Test schema and data files."""
    base_path = Path(__file__).parent
    schema_path = base_path / 'schema.json'
    data_path = base_path / 'data.json'

    # Load schema
    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
    except FileNotFoundError:
        print("❌ schema.json not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in schema.json: {e}")
        return False

    # Load data
    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ data.json not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in data.json: {e}")
        return False

    # Validate
    try:
        jsonschema.validate(instance=data, schema=schema)
        print("✅ Data validates against schema!")
        print(f"\nValidated data:")
        print(json.dumps(data, indent=2))
        return True
    except jsonschema.ValidationError as e:
        print(f"❌ Validation error: {e.message}")
        return False
    except jsonschema.SchemaError as e:
        print(f"❌ Invalid schema: {e.message}")
        return False


if __name__ == '__main__':
    sys.exit(0 if test_schema_validation() else 1)
