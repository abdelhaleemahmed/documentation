# Quick Reference Guide

Essential YAML & JSON rules, syntax, and patterns for daily use.

## YAML Quick Reference

### Basic Syntax

```yaml
# Comments start with #
key: value           # String (quotes optional)
number: 42           # Integer
float: 3.14          # Float
boolean: true        # Boolean (true/false, yes/no)
null_value: null     # Null (null, ~)
list:                # Sequence/List
  - item1
  - item2
  - item3
dict:                # Mapping/Dictionary
  key1: value1
  key2: value2
```

### Advanced Features

```yaml
# Multi-line strings
literal: |
  Line 1
  Line 2

folded: >
  This folds
  into one line.

# Anchors & Aliases
defaults: &base
  timeout: 30
  retries: 3

service:
  <<: *base
  name: api

# Explicit types
str: !!str 123        # "123"
int: !!int "456"      # 456
float: !!float 1.2e3  # 1200.0
binary: !!binary |    # Base64
  R0lGODlhDAAMAIQAAP//9/X
```

### Common Patterns

```yaml
# Nested structures
app:
  server:
    host: localhost
    port: 3000
  database:
    primary:
      host: db1
      port: 5432
    replica:
      host: db2
      port: 5432

# Lists of objects
users:
  - name: Alice
    role: admin
    active: true
  - name: Bob
    role: user
    active: false

# Environment configuration
development: &dev
  debug: true
  database: localhost

production:
  <<: *dev
  debug: false
  database: cluster.prod.com
```

### YAML Rules to Remember

| Rule | Description |
|------|-------------|
| **Indentation** | Use 2 spaces, NO TABS |
| **Comments** | Start with `#` |
| **Strings** | Quotes optional unless special chars |
| **Booleans** | `true`/`false`, `yes`/`no`, `on`/`off` |
| **Null** | `null`, `~`, or empty |
| **Lists** | Start with `-` |
| **Multi-line** | `\|` preserves newlines, `>` folds |
| **Anchors** | `&name` to define, `*name` to reference |
| **Merge** | `<<: *anchor` to merge values |

---

## JSON Quick Reference

### Basic Syntax

```json
{
  "string": "value",
  "number": 123,
  "float": 3.14,
  "scientific": 1.2e3,
  "boolean_true": true,
  "boolean_false": false,
  "null": null,
  "array": ["item1", "item2", "item3"],
  "object": {
    "nested": "value",
    "deep": {
      "level": 3
    }
  }
}
```

### JSON Rules to Remember

| Rule | Description |
|------|-------------|
| **Quotes** | Double quotes only for strings and keys |
| **Comments** | NOT allowed (use JSONC for unofficial support) |
| **Trailing commas** | NOT allowed |
| **Keys** | Must be strings in double quotes |
| **Booleans** | `true` and `false` (lowercase only) |
| **Null** | `null` (lowercase only) |
| **Numbers** | No leading zeros (except `0.x`) |
| **Strings** | Escape special chars: `\n`, `\"`, `\\` |

### JSON Data Types

| Type | Example | Notes |
|------|---------|-------|
| String | `"hello"` | Double quotes required |
| Number | `123`, `3.14`, `1.2e3` | Integer or float |
| Boolean | `true`, `false` | Lowercase only |
| Null | `null` | Lowercase only |
| Array | `[1, 2, 3]` | Ordered list |
| Object | `{"key": "value"}` | Key-value pairs |

---

## YAML vs JSON Comparison

| Feature | YAML | JSON |
|---------|------|------|
| **Comments** | ✅ Yes (`#`) | ❌ No (JSONC unofficial) |
| **Readability** | High for configs | Good for data |
| **Quotes** | Optional | Required for strings |
| **Indentation** | 2 spaces (no tabs) | Any whitespace |
| **Multi-line** | `\|` and `>` | Escaped `\n` |
| **Anchors** | ✅ Yes (`&`, `*`) | ❌ No |
| **Trailing commas** | ❌ No | ❌ No |
| **Speed** | Slower (complex parsing) | Faster (simple grammar) |
| **Use cases** | Config files, CI/CD | APIs, data exchange |

---

## When to Use What?

### Use YAML for:
- Configuration files (Kubernetes, Docker Compose)
- CI/CD pipelines (GitHub Actions, GitLab CI)
- Infrastructure as Code (Ansible, Terraform)
- Application configs with comments
- Human-editable settings

### Use JSON for:
- REST API requests/responses
- Data exchange between systems
- Web application configs
- NoSQL database documents
- Programmatic data processing
- High-performance parsing needs

---

## Common Mistakes Quick Fix

### YAML Mistakes

```yaml
# ❌ WRONG - Tab character
	key: value

# ✅ CORRECT - 2 spaces
  key: value

# ❌ WRONG - Inconsistent indentation
list:
  - item1
   - item2

# ✅ CORRECT - Aligned properly
list:
  - item1
  - item2

# ❌ WRONG - Unquoted special string
country: NO  # Parsed as boolean false

# ✅ CORRECT - Quote special values
country: "NO"  # String
```

### JSON Mistakes

```json
// ❌ WRONG - Trailing comma
{
  "name": "Alice",
  "age": 30,
}

// ✅ CORRECT - No trailing comma
{
  "name": "Alice",
  "age": 30
}

// ❌ WRONG - Single quotes
{
  'name': 'Alice'
}

// ✅ CORRECT - Double quotes
{
  "name": "Alice"
}

// ❌ WRONG - Comments
{
  // This is a comment
  "name": "Alice"
}

// ✅ CORRECT - No comments
{
  "name": "Alice"
}
```

---

## Essential Commands

### Validation

```bash
# YAML validation
yamllint config.yaml

# JSON validation
jsonlint data.json

# Python validation
python -c "import yaml; yaml.safe_load(open('config.yaml'))"
python -c "import json; json.load(open('data.json'))"
```

### Conversion

```bash
# YAML to JSON (using Python)
python -c "import yaml, json; print(json.dumps(yaml.safe_load(open('config.yaml'))))"

# JSON to YAML (using Python)
python -c "import yaml, json; print(yaml.dump(json.load(open('data.json'))))"

# Using yq (YAML processor)
yq eval -o=json config.yaml > output.json

# Using jq (JSON processor)
jq '.' data.json
```

### Query

```bash
# Query YAML with yq
yq '.app.database.host' config.yaml

# Query JSON with jq
jq '.app.database.host' data.json

# Filter arrays
jq '.users[] | select(.active == true)' users.json
```

---

## Safety Checklist

### YAML Safety
- [ ] Use `yaml.safe_load()`, never `yaml.load()`
- [ ] Validate indentation (2 spaces, no tabs)
- [ ] Quote special values (`yes`, `no`, `on`, `off`)
- [ ] Never commit secrets in YAML files
- [ ] Use linters in CI/CD pipeline

### JSON Safety
- [ ] Use `JSON.parse()`, never `eval()`
- [ ] Validate with JSON Schema
- [ ] Check for trailing commas
- [ ] Ensure all keys are quoted
- [ ] Never commit secrets in JSON files

---

## Resources

### Tools
- **yamllint** - YAML linter
- **jsonlint** - JSON linter
- **yq** - YAML processor (like jq for JSON)
- **jq** - JSON processor
- **JSON Schema** - Validation framework

### Online Validators
- https://www.yamllint.com/
- https://jsonlint.com/
- https://www.json-schema.org/

---

**See also:**
- [Common Errors](common-errors.md) - 38 documented errors with solutions
- [Misconceptions](misconceptions.md) - YAML & JSON myths debunked
- [Interview Questions](interview-prep.md) - Practice questions
