# YAML & JSON Quick Reference Cheat Sheet

**One-page reference for syntax, patterns, and common operations**

---

## 📋 Syntax Comparison

| Feature | YAML | JSON |
|---------|------|------|
| **Comments** | `# Comment` | ❌ Not supported |
| **String** | `name: John` or `name: "John"` | `"name": "John"` |
| **Number** | `age: 30` | `"age": 30` |
| **Boolean** | `active: true` | `"active": true` |
| **Null** | `value: null` or `value: ~` | `"value": null` |
| **Array** | `- item1`<br>`- item2` | `["item1", "item2"]` |
| **Object** | `key: value` | `{"key": "value"}` |
| **Multi-line** | `text: \|`<br>`  Line 1`<br>`  Line 2` | `"text": "Line 1\\nLine 2"` |
| **Nesting** | Indentation (2 or 4 spaces) | Braces `{}` and brackets `[]` |

---

## 🎯 Common Patterns

### YAML

```yaml
# Simple config
app:
  name: MyApp
  version: 1.0.0
  debug: true

# List of strings
features:
  - authentication
  - logging
  - monitoring

# List of objects
users:
  - name: Alice
    role: admin
  - name: Bob
    role: user

# Nested structure
database:
  primary:
    host: localhost
    port: 5432
  replica:
    host: replica.db
    port: 5432

# Anchors & Aliases (DRY)
defaults: &defaults
  timeout: 30
  retries: 3

service1:
  <<: *defaults
  name: API

# Multi-line strings
description: |
  This preserves
  line breaks
  exactly

summary: >
  This folds into
  a single line
  of text
```

### JSON

```json
{
  "app": {
    "name": "MyApp",
    "version": "1.0.0",
    "debug": true
  },
  "features": [
    "authentication",
    "logging",
    "monitoring"
  ],
  "users": [
    {
      "name": "Alice",
      "role": "admin"
    },
    {
      "name": "Bob",
      "role": "user"
    }
  ],
  "database": {
    "primary": {
      "host": "localhost",
      "port": 5432
    },
    "replica": {
      "host": "replica.db",
      "port": 5432
    }
  }
}
```

---

## 🔥 Common Pitfalls

### YAML

| ❌ Wrong | ✅ Correct | Issue |
|----------|-----------|-------|
| `key:value` | `key: value` | Missing space after `:` |
| `- item1`<br>`  - item2` | `- item1`<br>`- item2` | Inconsistent indentation |
| Mixed tabs/spaces | Use spaces only | Tabs not allowed |
| `name: yes` | `name: "yes"` | `yes` becomes boolean |
| `version: 1.0` | `version: "1.0"` | Numbers lose precision |
| Unquoted `@`, `*`, `&` | Quote special chars | Reserved characters |

### JSON

| ❌ Wrong | ✅ Correct | Issue |
|----------|-----------|-------|
| `{name: "John"}` | `{"name": "John"}` | Keys must be quoted |
| `{"age": 30,}` | `{"age": 30}` | Trailing comma not allowed |
| `{'name': 'John'}` | `{"name": "John"}` | Must use double quotes |
| `// comment` | ❌ Remove comments | Comments not supported |
| `"value": undefined` | `"value": null` | Use `null`, not `undefined` |

---

## 🛠️ Essential Tools

### Command-Line Tools

```bash
# YAML validation
yamllint config.yaml

# YAML to JSON
yq eval -o=json config.yaml > config.json

# JSON to YAML
yq eval -P config.json > config.yaml

# Query YAML
yq eval '.database.host' config.yaml

# Query JSON
jq '.database.host' config.json

# Format/prettify JSON
jq '.' config.json

# Validate JSON
jq empty config.json

# Kubernetes validation
kubectl apply -f deployment.yaml --dry-run=client

# Docker Compose validation
docker-compose -f docker-compose.yml config
```

### Python Quick Scripts

```python
# YAML → JSON
import yaml, json
with open('config.yaml') as f:
    data = yaml.safe_load(f)
with open('config.json', 'w') as f:
    json.dump(data, f, indent=2)

# JSON → YAML
import yaml, json
with open('config.json') as f:
    data = json.load(f)
with open('config.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)

# Validate with schema
import jsonschema
jsonschema.validate(data, schema)
```

---

## 🚀 Quick Decision Guide

```
Choose YAML when:
  ✅ Human editing required
  ✅ Need comments
  ✅ Complex nested configs
  ✅ Configuration files
  ✅ CI/CD pipelines
  ✅ Infrastructure as Code

Choose JSON when:
  ✅ API responses
  ✅ Web services
  ✅ Performance critical
  ✅ No human editing
  ✅ JavaScript integration
  ✅ Data interchange
```

---

## 📊 Data Types Quick Reference

### YAML Type Inference

```yaml
string1: Hello           # String (unquoted)
string2: "123"           # String (quoted)
string3: 'true'          # String (quoted)

number1: 42              # Integer
number2: 3.14            # Float
number3: 1.23e+3         # Scientific notation

bool1: true              # Boolean
bool2: false             # Boolean
bool3: yes               # Boolean (YAML 1.1)
bool4: no                # Boolean (YAML 1.1)

null1: null              # Null
null2: ~                 # Null
null3:                   # Null (empty value)

# Explicit typing
string: !!str 123        # Force string
integer: !!int "123"     # Force integer
```

### JSON Types (Always Explicit)

```json
{
  "string": "Hello",
  "number": 42,
  "float": 3.14,
  "boolean": true,
  "null": null,
  "array": [1, 2, 3],
  "object": {"key": "value"}
}
```

---

## ⚡ Performance Tips

| Operation | Tip |
|-----------|-----|
| **Large files** | Use JSON for 10x faster parsing |
| **Streaming** | Use `yaml.safe_load_all()` for multi-doc |
| **Caching** | Cache parsed configs, don't re-parse |
| **Validation** | Validate once at load, not repeatedly |
| **Serialization** | JSON is 5-10x faster to serialize |

---

## 🔒 Security Checklist

```yaml
# ✅ DO
- Use safe_load() not load()
- Validate with JSON Schema
- Use environment variables for secrets
- Scan for committed secrets
- Validate before deployment
- Set resource limits in configs

# ❌ DON'T
- Don't use yaml.load() with untrusted input
- Don't commit secrets to configs
- Don't skip validation
- Don't trust user-provided configs
- Don't use eval() on config values
```

---

## 🎨 Formatting Best Practices

### YAML

```yaml
# Indentation: 2 spaces (consistent)
# Quotes: Only when needed
# Comments: Above or beside values
# Blank lines: Separate logical sections

database:  # Database configuration
  host: localhost
  port: 5432

  # Connection pool settings
  pool:
    min: 5
    max: 20
```

### JSON

```json
// Indentation: 2 spaces
// Always quote keys
// No trailing commas
// Minify for production

{
  "database": {
    "host": "localhost",
    "port": 5432
  }
}
```

---

## 📦 Common Use Cases

| Use Case | Format | Why |
|----------|--------|-----|
| **Kubernetes** | YAML | Human-readable, comments |
| **Docker Compose** | YAML | Multi-service configs |
| **API Responses** | JSON | Performance, universal |
| **Config Files** | YAML | Comments, readability |
| **CI/CD Pipelines** | YAML | Human editing |
| **Data Exchange** | JSON | Language agnostic |
| **Web Apps** | JSON | Native JS support |
| **IaC (Terraform)** | YAML/JSON | Both supported |

---

## 🔄 Quick Conversion Reference

### Remove for JSON → YAML

```yaml
- Remove all { } braces
- Remove all [ ] brackets
- Remove quotes from keys
- Remove commas after values
- Add proper indentation
- Optional: Add comments
```

### Add for YAML → JSON

```json
{
  "Add": "braces around objects",
  "Add": "brackets around arrays",
  "Quote": "all keys and string values",
  "Add": "commas after values",
  "Remove": "all comments"
}
```

---

## 📝 File Extensions

```
YAML: .yaml, .yml
JSON: .json

# Kubernetes
- deployment.yaml
- service.yaml
- configmap.yaml

# Config files
- config.yaml
- settings.json
- package.json
```

---

## 🎓 Learning Path

```
1. Basic Syntax          → 30 min
2. Data Types            → 30 min
3. Conversion            → 30 min
4. Tools (yq, jq)        → 1 hour
5. Real-World Examples   → 2 hours
6. Advanced Features     → 2 hours
7. Security & Validation → 1 hour
8. Practice Exercises    → 4 hours

Total: ~12 hours to proficiency
```

---

## 📚 Quick Links

- **YAML Spec:** https://yaml.org/spec/
- **JSON Spec:** https://www.json.org/
- **YAML Lint:** https://www.yamllint.com/
- **JSON Lint:** https://jsonlint.com/
- **yq Docs:** https://github.com/mikefarah/yq
- **jq Docs:** https://stedolan.github.io/jq/

---

## 🆘 Emergency Fixes

```bash
# Fix indentation issues
python -c "import yaml, sys; yaml.dump(yaml.safe_load(sys.stdin), sys.stdout)" < broken.yaml

# Validate and show errors
yamllint -f parsable config.yaml

# Quick format JSON
echo '{"a":1,"b":2}' | jq '.'

# Find all YAML files
find . -name "*.yaml" -o -name "*.yml"

# Batch validate
find . -name "*.yaml" -exec yamllint {} \;
```

---

**Print this page for quick reference at your desk!**

**For complete guide:** See YAML_and_JSON_Guide.md
