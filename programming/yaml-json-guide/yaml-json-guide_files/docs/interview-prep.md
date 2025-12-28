# Interview Questions & Answers

Prepare for technical interviews with these common YAML/JSON questions and expert answers.

## YAML Interview Questions

### Q1: Why does YAML parse `no` as a boolean?

**Answer:**
In YAML 1.1, `yes`, `no`, `on`, `off`, `true`, and `false` are all interpreted as booleans. This is due to implicit type conversion.

To force a string:
```yaml
status: "no"  # String
status: no    # Boolean false
```

YAML 1.2 removed many of these implicit conversions, but most parsers still support YAML 1.1 for backwards compatibility.

---

### Q2: What's the difference between `|` and `>` in YAML?

**Answer:**
- `|` (literal) preserves newlines exactly as written
- `>` (folded) folds newlines into spaces (creates a single paragraph)

```yaml
# Literal - preserves formatting
script: |
  line 1
  line 2
# Result: "line 1\nline 2"

# Folded - creates one line
description: >
  This is
  one paragraph
# Result: "This is one paragraph"
```

Use `|` for code/scripts, use `>` for long descriptive text.

---

### Q3: How do anchors and aliases work in YAML?

**Answer:**
Anchors (`&`) create a reusable reference, aliases (`*`) reference it:

```yaml
defaults: &db_defaults
  port: 5432
  timeout: 30

dev:
  database:
    <<: *db_defaults  # Merge
    host: localhost

prod:
  database:
    <<: *db_defaults
    host: prod.db.com
```

The `<<:` merge key combines the anchor's values.

**Important:** Anchors are lost when converting to JSON.

---

### Q4: Why is YAML slower than JSON?

**Answer:**
YAML parsing is slower due to:
1. Complex grammar with multiple syntaxes
2. Indentation-based structure requiring careful parsing
3. Anchor resolution (expanding aliases)
4. Type inference (guessing if `123` is string or number)
5. Multi-line block processing

JSON is faster because it has a strict, simple grammar with no ambiguity.

**Benchmark:** JSON is typically 10-50x faster to parse than YAML.

---

## JSON Interview Questions

### Q5: How do you validate JSON with a schema?

**Answer:**
Use JSON Schema with a validator:

```python
import jsonschema

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0}
    },
    "required": ["name"]
}

data = {"name": "Alice", "age": 30}
jsonschema.validate(data, schema)  # Raises error if invalid
```

JSON Schema defines:
- Required fields
- Data types
- Validation rules (min/max, patterns, enums)
- Nested structures

---

### Q6: What's wrong with using `eval()` to parse JSON?

**Answer:**
**NEVER use `eval()` to parse JSON!** It's a major security vulnerability.

```javascript
// ❌ DANGEROUS - Code injection risk!
let data = eval('(' + jsonString + ')');

// ✅ SAFE - Use JSON.parse()
let data = JSON.parse(jsonString);
```

`eval()` executes arbitrary JavaScript code, allowing attackers to:
- Execute malicious code
- Access sensitive data
- Modify application state

Always use `JSON.parse()` in JavaScript or equivalent in other languages.

---

### Q7: Can JSON represent dates natively?

**Answer:**
**No, JSON has no native date type.**

Dates must be represented as:
- ISO 8601 string: `"2024-01-15T10:30:00Z"`
- Unix timestamp: `1705318200`
- Custom format

```json
{
  "created": "2024-01-15T10:30:00Z",  ← String
  "timestamp": 1705318200            ← Number
}
```

The application must parse and interpret these as dates.

---

## DevOps Interview Questions

### Q8: How do you manage secrets in YAML config files?

**Answer:**
**Never hardcode secrets in YAML!**

**Best practices:**
1. **Environment variables:**
   ```yaml
   database:
     password: ${DB_PASSWORD}  # Injected at runtime
   ```

2. **Secret management tools:**
   - HashiCorp Vault
   - AWS Secrets Manager
   - Kubernetes Secrets (base64 encoded)

3. **Encrypted secrets:**
   - SOPS (Secrets OPerationS)
   - Sealed Secrets for Kubernetes

4. **Git-ignored `.env` files:**
   ```bash
   # .env (never commit!)
   DB_PASSWORD=secret123
   ```

---

### Q9: How do you debug Kubernetes YAML validation errors?

**Answer:**
**Debugging workflow:**

1. **Dry-run validation:**
   ```bash
   kubectl apply -f deployment.yaml --dry-run=client -o yaml
   ```

2. **Explain fields:**
   ```bash
   kubectl explain deployment.spec.template.spec.containers
   ```

3. **Check specific errors:**
   ```bash
   kubectl apply -f deployment.yaml
   # Read error message carefully
   ```

4. **Use yamllint:**
   ```bash
   yamllint deployment.yaml
   ```

5. **Use kubeval:**
   ```bash
   kubeval deployment.yaml
   ```

**Common errors:**
- Wrong `apiVersion`
- Unknown fields (typos in spec)
- Indentation errors
- Missing required fields

---

### Q10: What's the difference between ConfigMap and Secret in Kubernetes?

**Answer:**

| Feature | ConfigMap | Secret |
|---------|-----------|--------|
| **Purpose** | Non-sensitive config data | Sensitive data (passwords, tokens) |
| **Encoding** | Plain text | Base64 encoded |
| **Storage** | Stored as plain text in etcd | Stored base64 in etcd (encryption at rest optional) |
| **Usage** | Environment variables, config files | Credentials, TLS certs, SSH keys |

```yaml
# ConfigMap - for non-sensitive data
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  app.properties: |
    debug=true
    log_level=INFO

# Secret - for sensitive data
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=  # Base64 encoded
```

**Important:** Base64 is encoding, NOT encryption! Enable encryption at rest for true security.

---

## Quick Answer Cheat Sheet

| Question | Answer Keywords |
|----------|----------------|
| YAML vs JSON when? | YAML=config/comments, JSON=APIs/speed |
| YAML indentation? | 2 spaces, no tabs, alignment matters |
| JSON trailing comma? | Not allowed in standard JSON |
| Parse safety? | Use `safe_load()` for YAML, `JSON.parse()` for JSON |
| Secret management? | Environment variables, Vault, never hardcode |
| YAML anchors? | `&anchor` define, `*alias` reference, `<<:` merge |
| Schema validation? | JSON Schema with validators |
| Multi-line YAML? | `\|` literal preserves, `>` folded combines |

> **Pro Tip:** Practice these questions out loud! Being able to explain concepts clearly is just as important as knowing the technical details.

---

**See also:**
- [Common Errors](common-errors.md) - 38 documented errors with solutions
- [Misconceptions](misconceptions.md) - YAML & JSON myths debunked
- [Quick Reference](quick-reference.md) - Essential YAML & JSON rules
