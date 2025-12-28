# Exercise 16: Custom YAML/JSON Parser

## Objective
Build a custom parser with validation, environment variable substitution, and includes.

## Difficulty
Advanced (⭐⭐⭐⭐)

## What You'll Learn
- Parser architecture
- Environment variable expansion
- File inclusion
- Custom validation
- Error handling

## Task
Create a ConfigParser class with advanced features.

## Features to Implement

### 1. Environment Variable Substitution
```yaml
database:
  password: ${DB_PASSWORD}  # Replace at parse time
  host: ${DB_HOST:-localhost}  # Default value
```

### 2. File Inclusion
```yaml
# main.yaml
app:
  name: MyApp
  !include database.yaml
  !include server.yaml
```

### 3. Custom Validation
```python
schema = {
    'database': {
        'required': True,
        'type': dict,
        'schema': {
            'host': {'required': True, 'type': str},
            'port': {'required': True, 'type': int, 'min': 1, 'max': 65535}
        }
    }
}
```

### 4. Type Coercion
```yaml
port: "8080"  # Auto-convert to int
enabled: "true"  # Auto-convert to bool
```

## Implementation Guide

### Basic Structure
```python
class ConfigParser:
    def __init__(self, schema=None):
        self.schema = schema

    def parse(self, file_path):
        """Parse config with all features."""
        # 1. Load YAML/JSON
        # 2. Expand environment variables
        # 3. Process includes
        # 4. Validate against schema
        # 5. Return config object
        pass

    def expand_env_vars(self, data):
        """Replace ${VAR} with environment variables."""
        pass

    def process_includes(self, data, base_path):
        """Process !include directives."""
        pass

    def validate(self, data):
        """Validate against schema."""
        pass
```

### Environment Variable Expansion
```python
import os
import re

def expand_env_vars(self, value):
    """Expand ${VAR} and ${VAR:-default}."""
    if not isinstance(value, str):
        return value

    pattern = r'\$\{([A-Z_][A-Z0-9_]*)(:-([^}]+))?\}'

    def replace(match):
        var_name = match.group(1)
        default_value = match.group(3)
        return os.getenv(var_name, default_value or '')

    return re.sub(pattern, replace, value)
```

### Recursive Processing
```python
def process_dict(self, data, base_path):
    """Recursively process dict."""
    result = {}
    for key, value in data.items():
        if key == '!include':
            # Load and merge included file
            included = self.parse(base_path / value)
            result.update(included)
        elif isinstance(value, dict):
            result[key] = self.process_dict(value, base_path)
        elif isinstance(value, list):
            result[key] = self.process_list(value, base_path)
        else:
            result[key] = self.expand_env_vars(value)
    return result
```

## Task Requirements
1. Implement ConfigParser class
2. Support environment variable expansion
3. Support file includes (optional)
4. Validate against schema
5. Handle errors gracefully
6. Write comprehensive tests

## Testing
```python
# Test env var expansion
os.environ['DB_PASSWORD'] = 'secret123'
config = parser.parse('config.yaml')
assert config['database']['password'] == 'secret123'

# Test defaults
config = parser.parse('config.yaml')
assert config['database']['host'] == 'localhost'  # Default

# Test validation
schema = {'database': {'required': True}}
parser = ConfigParser(schema)
config = parser.parse('config.yaml')  # Should validate
```

## Hints
- Use regex for env var pattern matching
- Handle nested dicts/lists recursively
- Validate types before coercion
- Provide helpful error messages
- Test edge cases (missing vars, circular includes)

## Bonus Features
- Template variables: `{{variable}}`
- Encrypted values: `!encrypted <base64>`
- Remote includes: `!include https://...`
- Schema auto-generation
- Config diff/merge tools

## Solution
Check `parser.py` when ready.
