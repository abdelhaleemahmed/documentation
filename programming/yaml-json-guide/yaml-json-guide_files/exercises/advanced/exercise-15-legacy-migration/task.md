# Exercise 15: Legacy Configuration Migration

## Objective
Migrate legacy configuration formats to modern YAML/JSON standards.

## Difficulty
Advanced (⭐⭐⭐)

## What You'll Learn
- Handling legacy formats
- Data transformation
- Backward compatibility
- Migration strategies

## Task
Convert old-style configuration to modern format with best practices.

## Legacy Format Issues

### 1. INI/Properties Style
```ini
# Old format
[database]
host=localhost
port=5432
user=admin

[server]
host=0.0.0.0
port=8080
```

### 2. XML Style
```xml
<config>
  <database host="localhost" port="5432"/>
  <server host="0.0.0.0" port="8080"/>
</config>
```

### 3. Old YAML Conventions
```yaml
# Legacy (bad practices)
database.host: localhost
database.port: 5432
use_cache: yes  # Implicit boolean
version: 1.0  # Will become float
```

## Modern Format (Target)
```yaml
# Modern YAML with best practices
database:
  host: localhost
  port: 5432
  username: ${DB_USERNAME}  # Environment variables
  password: ${DB_PASSWORD}

server:
  host: 0.0.0.0
  port: 8080

features:
  use_cache: true  # Explicit boolean

application:
  version: "1.0"  # Quoted to remain string
```

## Migration Strategies

### 1. Automated Conversion
```python
import yaml
import configparser

# Read INI
config = configparser.ConfigParser()
config.read('legacy.ini')

# Convert to dict
data = {section: dict(config[section]) for section in config.sections()}

# Write YAML
with open('modern.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
```

### 2. Manual Improvements
- Add proper nesting
- Use environment variables for secrets
- Explicit boolean/string types
- Add validation schema
- Document breaking changes

### 3. Backward Compatibility
- Support both formats temporarily
- Provide migration script
- Document deprecations
- Version the config format

## Task Requirements
1. Convert `legacy-config.ini` to modern YAML
2. Replace hardcoded secrets with env vars
3. Fix implicit type conversions
4. Add proper structure and nesting
5. Add comments for clarity
6. Create migration script

## Migration Checklist
- [ ] Convert flat keys to nested structure
- [ ] Replace hardcoded secrets
- [ ] Fix boolean values (yes/no → true/false)
- [ ] Quote version strings
- [ ] Add environment variable support
- [ ] Validate with schema
- [ ] Document changes

## Hints
- Use configparser for INI files
- Group related settings
- Always quote strings that look like numbers
- Use explicit booleans
- Test backward compatibility

## Solution
Check `modern-config.yaml` and `migrate.py` when ready.
