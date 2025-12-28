#!/usr/bin/env python3
"""Custom YAML/JSON Configuration Parser with Advanced Features"""

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed")
    import sys
    sys.exit(1)


class ConfigValidationError(Exception):
    """Raised when configuration validation fails."""
    pass


class ConfigParser:
    """Advanced configuration parser with env vars, includes, and validation."""

    def __init__(self, schema: Optional[Dict] = None):
        """
        Initialize parser with optional schema.

        Args:
            schema: Validation schema for the configuration
        """
        self.schema = schema

    def parse(self, file_path: str) -> Dict[str, Any]:
        """
        Parse configuration file with all features.

        Args:
            file_path: Path to YAML or JSON file

        Returns:
            Parsed and processed configuration
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"Config file not found: {file_path}")

        # Load file
        with open(file_path, 'r') as f:
            if file_path.suffix in ['.yaml', '.yml']:
                data = yaml.safe_load(f)
            elif file_path.suffix == '.json':
                data = json.load(f)
            else:
                raise ValueError(f"Unsupported file type: {file_path.suffix}")

        # Process configuration
        data = self._process_data(data, file_path.parent)

        # Validate if schema provided
        if self.schema:
            self._validate(data, self.schema)

        return data

    def _process_data(self, data: Any, base_path: Path) -> Any:
        """
        Recursively process configuration data.

        Args:
            data: Configuration data to process
            base_path: Base path for resolving includes

        Returns:
            Processed data
        """
        if isinstance(data, dict):
            return self._process_dict(data, base_path)
        elif isinstance(data, list):
            return self._process_list(data, base_path)
        elif isinstance(data, str):
            return self._expand_env_vars(data)
        else:
            return data

    def _process_dict(self, data: Dict, base_path: Path) -> Dict:
        """Process dictionary with includes and env vars."""
        result = {}

        for key, value in data.items():
            # Handle includes
            if key == '!include':
                included_file = base_path / value
                included_data = self.parse(str(included_file))
                result.update(included_data)
            else:
                result[key] = self._process_data(value, base_path)

        return result

    def _process_list(self, data: List, base_path: Path) -> List:
        """Process list items."""
        return [self._process_data(item, base_path) for item in data]

    def _expand_env_vars(self, value: str) -> str:
        """
        Expand environment variables in string.

        Supports:
        - ${VAR} - Simple substitution
        - ${VAR:-default} - With default value

        Args:
            value: String with potential env vars

        Returns:
            String with expanded env vars
        """
        pattern = r'\$\{([A-Z_][A-Z0-9_]*)(:-([^}]+))?\}'

        def replace(match):
            var_name = match.group(1)
            default_value = match.group(3)

            env_value = os.getenv(var_name)
            if env_value is not None:
                return env_value
            elif default_value is not None:
                return default_value
            else:
                # No value and no default
                raise ConfigValidationError(
                    f"Environment variable {var_name} not set and no default provided"
                )

        return re.sub(pattern, replace, value)

    def _validate(self, data: Dict, schema: Dict, path: str = "") -> None:
        """
        Validate configuration against schema.

        Args:
            data: Configuration to validate
            schema: Validation schema
            path: Current path (for error messages)
        """
        for key, rules in schema.items():
            current_path = f"{path}.{key}" if path else key

            # Check required fields
            if rules.get('required', False) and key not in data:
                raise ConfigValidationError(f"Required field missing: {current_path}")

            if key not in data:
                continue

            value = data[key]

            # Type validation
            expected_type = rules.get('type')
            if expected_type and not isinstance(value, expected_type):
                raise ConfigValidationError(
                    f"Invalid type for {current_path}: expected {expected_type.__name__}, "
                    f"got {type(value).__name__}"
                )

            # Range validation for numbers
            if isinstance(value, (int, float)):
                min_val = rules.get('min')
                max_val = rules.get('max')

                if min_val is not None and value < min_val:
                    raise ConfigValidationError(
                        f"{current_path} is {value}, must be >= {min_val}"
                    )

                if max_val is not None and value > max_val:
                    raise ConfigValidationError(
                        f"{current_path} is {value}, must be <= {max_val}"
                    )

            # Nested schema validation
            if 'schema' in rules and isinstance(value, dict):
                self._validate(value, rules['schema'], current_path)


def main():
    """Example usage and tests."""
    # Set test environment variables
    os.environ['DB_HOST'] = 'localhost'
    os.environ['DB_PORT'] = '5432'
    os.environ['DB_PASSWORD'] = 'secret123'

    # Define schema
    schema = {
        'database': {
            'required': True,
            'type': dict,
            'schema': {
                'host': {'required': True, 'type': str},
                'port': {'required': True, 'type': int, 'min': 1, 'max': 65535},
                'password': {'required': True, 'type': str}
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

    # Create parser
    parser = ConfigParser(schema=schema)

    # Test data
    test_config = {
        'database': {
            'host': '${DB_HOST:-localhost}',
            'port': 5432,
            'password': '${DB_PASSWORD}'
        },
        'server': {
            'host': '0.0.0.0',
            'port': 8080
        }
    }

    # Process
    processed = parser._process_data(test_config, Path.cwd())

    # Validate
    try:
        parser._validate(processed, schema)
        print("✅ Configuration valid")
        print(f"\nProcessed config:")
        print(yaml.dump(processed, default_flow_style=False))
    except ConfigValidationError as e:
        print(f"❌ Validation error: {e}")
        return False

    return True


if __name__ == '__main__':
    import sys
    sys.exit(0 if main() else 1)
