# Frequently Asked Questions (FAQ)

Common questions about YAML and JSON, answered concisely.

## General Questions

### Q: When should I use YAML vs JSON?

**A:**
- **YAML**: Configuration files, CI/CD pipelines, human-editable configs (Kubernetes, Docker Compose, Ansible)
- **JSON**: APIs, data exchange, web apps, programmatic processing, high-performance parsing

### Q: Is YAML a superset of JSON?

**A:** Yes! Valid JSON is also valid YAML. You can use JSON syntax directly in YAML files. However, YAML has many additional features JSON doesn't have (comments, anchors, multi-line strings).

### Q: Can I use YAML for API requests/responses?

**A:** Technically yes, but it's not recommended. JSON is the standard for APIs because:
- Faster to parse (10-50x faster)
- Smaller payload size
- Universal support across languages
- No ambiguity in data types

### Q: Why do some tools use both YAML and JSON?

**A:** Tools like Kubernetes accept both because:
- Humans prefer YAML for writing configs
- Programs prefer JSON for API responses
- Conversion between them is straightforward (with some caveats)

---

## YAML Specific Questions

### Q: Why doesn't my YAML file work with tabs?

**A:** YAML **forbids tabs** for indentation. Only spaces are allowed. Most editors can be configured to convert tabs to spaces automatically.

```yaml
# ❌ WRONG - Tab character
	key: value

# ✅ CORRECT - Spaces
  key: value
```

### Q: How many spaces should I use for indentation?

**A:** 2 spaces is the standard convention. Some use 4 spaces. The important thing is to be consistent throughout the file.

### Q: Why is my string `no` becoming `false`?

**A:** YAML 1.1 automatically converts certain strings to booleans:
- `yes`, `no` → boolean
- `on`, `off` → boolean
- `true`, `false` → boolean

**Solution:** Quote the string:
```yaml
answer: "no"  # String, not boolean
```

### Q: What's the difference between `|` and `>` for multi-line strings?

**A:**
- `|` (literal) - Preserves newlines exactly
- `>` (folded) - Folds newlines into spaces

```yaml
script: |
  line 1
  line 2
# Result: "line 1\nline 2"

description: >
  This becomes
  one line
# Result: "This becomes one line"
```

### Q: Can I use anchors in production?

**A:** Yes, but be aware:
- Anchors are lost when converting to JSON
- They can make debugging harder
- Not all YAML parsers support them equally
- They're great for reducing duplication in config files

### Q: Is YAML secure to parse?

**A:** YAML can be **dangerous** if parsed incorrectly. Always use safe loading:

```python
# ❌ DANGEROUS
yaml.load(untrusted_data)

# ✅ SAFE
yaml.safe_load(untrusted_data)
```

Some YAML parsers can execute arbitrary code if not configured safely!

---

## JSON Specific Questions

### Q: Can I use comments in JSON?

**A:** Standard JSON (RFC 8259) does **not** support comments. However:
- JSONC (JSON with Comments) is supported by some tools
- VS Code, TypeScript, Azure Pipelines support JSONC
- Don't rely on comments for portable JSON

```json
// This only works in JSONC, not standard JSON
{
  "name": "Alice",
  "age": 30  // JSONC comment
}
```

### Q: Why can't I use trailing commas?

**A:** JSON specification forbids trailing commas for simplicity:

```json
{
  "name": "Alice",
  "age": 30,  ← INVALID trailing comma
}
```

Some JavaScript parsers allow it, but it's not portable.

### Q: How do I represent dates in JSON?

**A:** JSON has **no native date type**. Use:
- ISO 8601 string: `"2024-01-15T10:30:00Z"`
- Unix timestamp: `1705318200`
- Your application must parse these

### Q: Can I use single quotes in JSON?

**A:** No, only double quotes are valid for strings and keys:

```json
// ❌ WRONG
{'name': 'Alice'}

// ✅ CORRECT
{"name": "Alice"}
```

### Q: What's the maximum nesting depth?

**A:** The JSON spec doesn't define a limit, but:
- Most parsers handle 100+ levels
- Practical limit is ~20 levels
- Deeply nested JSON hurts performance and readability

---

## Conversion Questions

### Q: Is YAML to JSON conversion lossless?

**A:** **No!** YAML → JSON loses:
- Comments
- Anchors and aliases
- Multi-line string formatting
- Custom tags
- Type information in some cases

### Q: Can I convert any JSON to YAML?

**A:** Yes, but watch for:
- Type reinterpretation (strings becoming booleans)
- Unquoted keys changing meaning
- Very long lines in YAML

### Q: How do I convert between formats?

**A:**

```bash
# YAML to JSON (Python)
python -c "import yaml, json; print(json.dumps(yaml.safe_load(open('file.yaml'))))"

# JSON to YAML (Python)
python -c "import yaml, json; print(yaml.dump(json.load(open('file.json'))))"

# Using yq
yq eval -o=json file.yaml > file.json

# Using this repo's tools
python tools/converters/yaml_to_json.py file.yaml
python tools/converters/json_to_yaml.py file.json
```

---

## Validation & Schema Questions

### Q: How do I validate YAML syntax?

**A:**

```bash
# Using yamllint
yamllint config.yaml

# Using Python
python -c "import yaml; yaml.safe_load(open('config.yaml'))"

# Using this repo's tool
python tools/validators/validate_yaml.py config.yaml
```

### Q: How do I validate JSON against a schema?

**A:**

```python
import jsonschema
import json

schema = json.load(open('schema.json'))
data = json.load(open('data.json'))
jsonschema.validate(data, schema)
```

Or use the repo's validator:
```bash
python tools/validators/validate_json.py data.json schema.json
```

### Q: What is JSON Schema?

**A:** JSON Schema is a vocabulary that lets you validate JSON structure:
- Define required fields
- Specify data types
- Set validation rules (min/max, patterns)
- Document your data format

See `schemas/` directory for examples.

---

## Best Practices Questions

### Q: Should I commit YAML/JSON configs to Git?

**A:** Yes for configs, but:
- ✅ Commit: Application configs, infrastructure definitions
- ❌ Never commit: Secrets, passwords, API keys, tokens
- Use environment variables or secret managers for sensitive data

### Q: How do I manage secrets in configs?

**A:**
1. Environment variables: `${DB_PASSWORD}`
2. Secret managers: HashiCorp Vault, AWS Secrets Manager
3. Encrypted secrets: SOPS, Sealed Secrets
4. Git-ignored `.env` files (local development only)

```yaml
# ❌ NEVER DO THIS
database:
  password: "supersecret123"

# ✅ DO THIS
database:
  password: ${DB_PASSWORD}
```

### Q: Should I validate configs in CI/CD?

**A:** **Absolutely yes!** Always validate before deploying:

```yaml
# Example GitHub Actions workflow
- name: Validate YAML
  run: yamllint **/*.yaml

- name: Validate JSON
  run: |
    for file in **/*.json; do
      python -c "import json; json.load(open('$file'))"
    done
```

---

## Tool-Specific Questions

### Q: What's the best editor for YAML/JSON?

**A:**
- **VS Code** - Best overall, great extensions
- **IntelliJ/PyCharm** - Excellent validation
- **Sublime Text** - Fast and lightweight
- **Vim/Neovim** - Terminal-based power

All support syntax highlighting and validation plugins.

### Q: What command-line tools should I know?

**A:**
- `yamllint` - YAML linter
- `yq` - YAML processor (like jq for YAML)
- `jq` - JSON processor and formatter
- `kubeval` - Kubernetes YAML validator
- `jsonlint` - JSON validator

### Q: How do I pretty-print JSON?

**A:**

```bash
# Using jq
jq '.' file.json

# Using Python
python -m json.tool file.json

# In Python code
import json
print(json.dumps(data, indent=2))
```

---

## Performance Questions

### Q: Is JSON really faster than YAML?

**A:** Yes, typically 10-50x faster because:
- Simpler grammar
- No type inference
- No anchor resolution
- No multi-line processing

### Q: When does performance matter?

**A:**
- High-throughput APIs
- Large data processing (>10MB files)
- Real-time systems
- Mobile applications (battery/CPU)

For configs read once at startup, performance difference is negligible.

### Q: How can I optimize parsing?

**A:**
- Use streaming parsers for large files
- Cache parsed configs
- Validate only in development/CI
- Use binary formats (Protobuf, MessagePack) for performance-critical cases

---

## Error Debugging Questions

### Q: How do I debug indentation errors?

**A:**
1. Check for tabs (convert to spaces)
2. Use an editor with indentation guides
3. Run through `yamllint`
4. Copy to online validator (https://www.yamllint.com/)

### Q: What does "mapping values are not allowed here" mean?

**A:** Usually an indentation or syntax error:

```yaml
# ❌ WRONG - Missing indentation
services:
web:
  image: nginx

# ✅ CORRECT
services:
  web:
    image: nginx
```

### Q: How do I find the exact error line?

**A:** Most parsers show line numbers:

```bash
yamllint config.yaml
# Output: config.yaml:15:3: [error] syntax error
```

---

## Still Have Questions?

- 📖 Check [Quick Reference](quick-reference.md)
- ❗ Browse [Common Errors](common-errors.md)
- 🧩 Read [Misconceptions](misconceptions.md)
- 🧠 Review [Interview Questions](interview-prep.md)
- 💬 Open an issue on GitHub
