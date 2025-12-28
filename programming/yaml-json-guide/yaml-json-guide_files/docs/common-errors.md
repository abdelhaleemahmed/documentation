# Common Errors Reference Guide

**Quick reference for 38+ documented YAML and JSON errors with solutions.**

This standalone guide provides immediate solutions to the most common errors developers encounter when working with YAML and JSON. No need to read the entire guide - jump straight to your error!

---

## 📑 Quick Navigation

- [YAML Core Errors](#yaml-core-errors)
- [YAML Multi-line String Errors](#yaml-multi-line-string-errors)
- [JSON Syntax Errors](#json-syntax-errors)
- [Production Configuration Errors](#production-configuration-errors)
- [Advanced Pattern Errors](#advanced-pattern-errors)

---

## 🧭 YAML Core Errors

**Common mistakes with YAML fundamentals**

### Error 1: Mixing Tabs and Spaces

**Problem:**
```yaml
# ❌ WRONG - Contains tab character
config:
	database: localhost  # This will fail!
```

**Solution:**
```yaml
# ✅ CORRECT - Spaces only
config:
  database: localhost
```

**Why it happens:** YAML forbids tabs completely. Configure your editor to insert spaces when you press Tab.

---

### Error 2: Misaligned Indentation

**Problem:**
```yaml
# ❌ WRONG - port is misaligned
database:
  host: localhost
   port: 5432  # 3 spaces instead of 2!
```

**Solution:**
```yaml
# ✅ CORRECT - Consistent 2-space indentation
database:
  host: localhost
  port: 5432
```

**Why it happens:** YAML is indentation-sensitive. Every level must be consistently indented.

---

### Error 3: Missing Space After Colon

**Problem:**
```yaml
# ❌ WRONG - No space after colon
key:value
```

**Solution:**
```yaml
# ✅ CORRECT - Space required after colon
key: value
```

**Why it happens:** YAML syntax requires `key: value` format with space after colon.

---

### Error 4: Boolean Type Confusion

**Problem:**
```yaml
# ❌ WRONG - Becomes boolean true, not string "yes"
response: yes
enabled: on
disabled: off
```

**Solution:**
```yaml
# ✅ CORRECT - Quote to force string type
response: "yes"
enabled: "on"
disabled: "off"
```

**Why it happens:** YAML 1.1 interprets `yes`, `no`, `on`, `off` as booleans unless quoted.

---

### Error 5: Special Characters Without Quotes

**Problem:**
```yaml
# ❌ WRONG - Special characters need quoting
email: user@example.com
reference: *important
```

**Solution:**
```yaml
# ✅ CORRECT - Quote special characters
email: "user@example.com"
reference: "*important"
```

**Why it happens:** Characters like `@`, `*`, `&`, `!` have special meaning in YAML.

---

## 📝 YAML Multi-line String Errors

**Common mistakes with multi-line strings**

### Error 6: Wrong Multi-line Operator

**Problem:**
```yaml
# Using | when you want folding, or > when you want literals
description: |
  This is one long sentence that
  should be on one line
```

**Solution:**
```yaml
# ✅ Use > for folded (single line)
description: >
  This is one long sentence that
  should be on one line

# ✅ Use | for literal (preserve line breaks)
script: |
  line 1
  line 2
```

**Why it happens:** `|` preserves newlines, `>` folds them into spaces.

---

## 🔷 JSON Syntax Errors

**Common JSON mistakes that break parsing**

### Error 7: Trailing Commas

**Problem:**
```json
{
  "name": "Alice",
  "age": 30,
}
```

**Solution:**
```json
{
  "name": "Alice",
  "age": 30
}
```

**Why it happens:** JSON doesn't allow trailing commas (unlike JavaScript).

---

### Error 8: Single Quotes

**Problem:**
```json
{
  'name': 'Alice',
  'role': 'admin'
}
```

**Solution:**
```json
{
  "name": "Alice",
  "role": "admin"
}
```

**Why it happens:** JSON specification requires double quotes for strings and keys.

---

### Error 9: Unquoted Keys

**Problem:**
```json
{
  name: "Alice",
  age: 30
}
```

**Solution:**
```json
{
  "name": "Alice",
  "age": 30
}
```

**Why it happens:** All JSON keys must be quoted strings.

---

### Error 10: Comments in JSON

**Problem:**
```json
{
  "name": "Alice",  // User name
  "age": 30
}
```

**Solution:**
```json
{
  "name": "Alice",
  "age": 30
}
```

**Why it happens:** Standard JSON doesn't support comments (use JSONC variant if needed).

---

### Error 11: Using undefined

**Problem:**
```json
{
  "value": undefined
}
```

**Solution:**
```json
{
  "value": null
}
```

**Why it happens:** JSON only has `null`, not `undefined`.

---

### Error 12: Unescaped Special Characters

**Problem:**
```json
{
  "text": "Line 1
Line 2",
  "path": "C:\folder\file.txt"
}
```

**Solution:**
```json
{
  "text": "Line 1\nLine 2",
  "path": "C:\\folder\\file.txt"
}
```

**Why it happens:** Special characters must be escaped in JSON strings.

---

### Error 13: Numeric Precision Issues

**Problem:**
```json
{
  "id": 9007199254740993
}
```

**Solution:**
```json
{
  "id": "9007199254740993"
}
```

**Why it happens:** Large integers lose precision in JavaScript. Use strings for large numbers.

---

### Error 14: Missing Validation

**Problem:**
```javascript
const data = JSON.parse(userInput);
database.query(data.query);  // Unsafe!
```

**Solution:**
```javascript
const data = JSON.parse(userInput);
if (typeof data.query === 'string') {
  database.query(data.query);
}
```

**Why it happens:** Never trust user input without validation.

---

## 🌍 Production Configuration Errors

**Real-world mistakes that cause outages**

### Error 15: Kubernetes - Incorrect Indentation

**Problem:**
```yaml
apiVersion: v1
kind: Pod
spec:
containers:  # Should be indented!
- name: app
  image: nginx:latest
```

**Solution:**
```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    image: nginx:latest
```

**Why it happens:** Kubernetes YAML has specific indentation requirements.

---

### Error 16: Docker Compose - Version Mismatch

**Problem:**
```yaml
version: '2'
services:
  app:
    deploy:  # deploy only exists in v3+
      replicas: 3
```

**Solution:**
```yaml
version: '3.8'
services:
  app:
    deploy:
      replicas: 3
```

**Why it happens:** Features are version-specific. Match version to features used.

---

### Error 17: CI/CD - Unquoted Environment Variables

**Problem:**
```yaml
env:
  NODE_ENV: production
  DEBUG: false  # Becomes boolean, not string "false"
  PORT: 8080    # Becomes number
```

**Solution:**
```yaml
env:
  NODE_ENV: "production"
  DEBUG: "false"
  PORT: "8080"
```

**Why it happens:** YAML type inference can cause unexpected types.

---

### Error 18: API - Inconsistent Null Handling

**Problem:**
```json
{
  "user": {
    "name": "Alice",
    "email": null,
    "phone": ""
  }
}
```

**Solution:**
```json
{
  "user": {
    "name": "Alice",
    "email": null,
    "phone": null
  }
}
```

**Why it happens:** Mix of null, missing, and empty strings causes confusion. Be consistent.

---

### Error 19: Hardcoded Secrets

**Problem:**
```yaml
database:
  host: prod-db.example.com
  username: admin
  password: "SuperSecret123!"  # SECURITY RISK!
```

**Solution:**
```yaml
database:
  host: "${DB_HOST}"
  username: "${DB_USER}"
  password: "${DB_PASSWORD}"
```

**Why it happens:** Never commit secrets to configs. Use environment variables.

---

### Error 20: Missing Kubernetes Resource Limits

**Problem:**
```yaml
containers:
- name: app
  image: myapp:latest
```

**Solution:**
```yaml
containers:
- name: app
  image: myapp:latest
  resources:
    requests:
      memory: "128Mi"
      cpu: "100m"
    limits:
      memory: "512Mi"
      cpu: "500m"
```

**Why it happens:** Without limits, pods can crash nodes.

---

### Error 21: Unescaped User Data in JSON

**Problem:**
```json
{
  "comment": "User said: "I love this!""
}
```

**Solution:**
```json
{
  "comment": "User said: \"I love this!\""
}
```

**Why it happens:** User input must be properly escaped.

---

### Error 22: YAML Anchor Overuse

**Problem:**
```yaml
defaults: &defaults
  timeout: 30
  <<: *other-defaults
  overrides: &overrides
    <<: *base-overrides
```

**Solution:**
```yaml
common-settings: &common
  timeout: 30
  retries: 3

service-a:
  <<: *common
  name: "Service A"
```

**Why it happens:** Too many nested anchors become unmaintainable. Keep it simple.

---

### Error 23: Using `latest` Tag in Production

**Problem:**
```yaml
services:
  api:
    image: mycompany/api:latest
```

**Solution:**
```yaml
services:
  api:
    image: mycompany/api:1.2.3
```

**Why it happens:** `latest` is non-deterministic. Always pin to specific versions.

---

### Error 24: Missing Array Length Validation

**Problem:**
```javascript
const users = apiResponse.users;
const firstUser = users[0];  // May crash if empty!
```

**Solution:**
```javascript
const users = apiResponse.users || [];
if (users.length > 0) {
  const firstUser = users[0];
}
```

**Why it happens:** Always validate array lengths before accessing elements.

---

## 🏗️ Advanced Pattern Errors

**Expert-level mistakes that cause subtle bugs**

### Error 25: Over-constraining Schema Validation

**Problem:**
```json
{
  "type": "object",
  "properties": {
    "email": {
      "pattern": "^[a-z]+@[a-z]+\\.[a-z]{3}$"
    }
  },
  "additionalProperties": false
}
```

**Solution:**
```json
{
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "format": "email"
    }
  },
  "additionalProperties": true
}
```

**Why it happens:** Too strict validation breaks legitimate use cases.

---

### Error 26: Circular References with Anchors

**Problem:**
```yaml
service-a: &service-a
  name: "Service A"
  depends_on: *service-b

service-b: &service-b
  name: "Service B"
  depends_on: *service-a  # Circular!
```

**Solution:**
```yaml
common-config: &common
  timeout: 30
  retries: 3

service-a:
  <<: *common
  name: "Service A"

service-b:
  <<: *common
  name: "Service B"
```

**Why it happens:** Circular dependencies create confusion. Use clear hierarchies.

---

### Error 27: Unsafe Deserialization

**Problem:**
```python
import yaml
config = yaml.load(untrusted_input)  # UNSAFE!
```

**Solution:**
```python
import yaml
config = yaml.safe_load(untrusted_input)
```

**Why it happens:** `yaml.load()` can execute arbitrary code. Always use `safe_load()`.

---

### Error 28: Hardcoding Instead of Templating

**Problem:**
```yaml
# prod-config.yaml
database:
  host: prod-db.example.com
  replicas: 5
```

**Solution:**
```yaml
database:
  host: "${DB_HOST}"
  replicas: ${DB_REPLICAS:3}
```

**Why it happens:** Templates are more maintainable than separate hardcoded files.

---

### Error 29: Not Understanding Merge Key Precedence

**Problem:**
```yaml
defaults: &defaults
  timeout: 30
  port: 8080

service:
  <<: *defaults
  timeout: 60  # Which value wins?
```

**Solution:**
```yaml
# Merge keys are applied first, then explicit keys override
defaults: &defaults
  timeout: 30
  port: 8080

service:
  <<: *defaults
  timeout: 60  # This overrides defaults
```

**Why it happens:** Document override behavior clearly.

---

### Error 30: Incomplete Secret Management

**Problem:**
```yaml
secrets:
  api_key: "${API_KEY}"
```

**Solution:**
```yaml
secrets:
  api_key:
    value: "${API_KEY}"
    rotate_days: 90
    access_level: "service-account-only"
    audit_log: true
```

**Why it happens:** Complete lifecycle management prevents security issues.

---

### Error 31: Inconsistent Naming Conventions

**Problem:**
```yaml
conf:
  db_host: localhost
  DatabasePort: 5432
  DB-USER: admin
```

**Solution:**
```yaml
database:
  host: localhost
  port: 5432
  user: admin
```

**Why it happens:** Consistent naming improves maintainability.

---

### Error 32: Not Validating Before Deployment

**Problem:**
```bash
kubectl apply -f config.yaml
```

**Solution:**
```bash
kubectl apply -f config.yaml --dry-run=client
yamllint config.yaml
```

**Why it happens:** Validation catches errors before they reach production.

---

### Error 33: Breaking Schema Changes

**Problem:**
```yaml
# v2 schema (breaks v1 clients)
user:
  name: string
  # email removed!
```

**Solution:**
```yaml
# v2 schema (backward compatible)
user:
  name: string
  email: string  # Deprecated, use contact.email
  contact:
    email: string
```

**Why it happens:** Deprecate gradually to avoid breaking changes.

---

### Error 34: Undocumented Complex Merges

**Problem:**
```yaml
base: &base
  <<: *defaults
  settings:
    <<: *common-settings
    overrides:
      <<: *override-base
```

**Solution:**
```yaml
# Base configuration (merged in order):
# 1. defaults (timeout, retries)
# 2. common-settings (logging, monitoring)
# 3. local overrides
base: &base
  <<: *defaults
  <<: *common-settings
  timeout: 60  # Override from defaults
```

**Why it happens:** Document complex merges for future maintainers.

---

## 🔍 Quick Troubleshooting Checklist

**Before you debug, check these:**

### YAML Checklist:
- [ ] Using spaces, not tabs?
- [ ] Consistent indentation (2 or 4 spaces)?
- [ ] Space after colons (`key: value`)?
- [ ] Quoted booleans if you want strings (`"yes"`, `"no"`)?
- [ ] Special characters quoted (`@`, `*`, `&`)?
- [ ] Using `safe_load()` for untrusted input?

### JSON Checklist:
- [ ] All keys quoted with double quotes?
- [ ] No trailing commas?
- [ ] Using double quotes, not single?
- [ ] No comments in standard JSON?
- [ ] Using `null` instead of `undefined`?
- [ ] Special characters escaped (`\n`, `\\`, `\"`)?

### Production Checklist:
- [ ] No hardcoded secrets?
- [ ] Resource limits set (Kubernetes)?
- [ ] Version pinning (not `latest`)?
- [ ] Validated before deployment?
- [ ] Environment-specific configs templated?

---

## 🛠️ Validation Tools

**Catch errors before they happen:**

```bash
# YAML validation
yamllint config.yaml

# JSON validation
jq empty config.json

# Kubernetes validation
kubectl apply -f deployment.yaml --dry-run=client

# Docker Compose validation
docker-compose -f docker-compose.yml config
```

---

## 📚 Related Resources

- [Main YAML & JSON Guide](../README.md)
- [Misconceptions Debunked](misconceptions.md)
- [Troubleshooting Guide](troubleshooting.md)
- [Quick Reference](quick-reference.md)

---

**Remember:** 90% of YAML/JSON errors fall into these categories:
1. Indentation issues
2. Quoting/escaping issues
3. Type confusion
4. Validation skipped

Set up linters and validators to catch these early!

---

*Last updated: January 2025*
*Part of the YAML & JSON Mega Guide ecosystem*
