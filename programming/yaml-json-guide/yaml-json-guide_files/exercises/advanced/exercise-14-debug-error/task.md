# Exercise 14: Real-World Error Debugging

## Objective
Debug complex YAML/JSON parsing and validation errors.

## Difficulty
Advanced (⭐⭐⭐)

## What You'll Learn
- Reading error messages
- Identifying root causes
- Common gotchas
- Systematic debugging

## Task
Fix real-world configuration errors that would break production systems.

## Common Error Patterns

### 1. Indentation Errors
```yaml
# ❌ Mixed indentation (fatal)
services:
  web:
    image: nginx
     ports:  # Extra space!
      - 80:80
```

### 2. Type Coercion
```yaml
# ❌ Implicit boolean conversion
country: NO  # Becomes false!
version: 1.0  # Becomes float!
```

### 3. Duplicate Keys
```yaml
# ❌ Last value wins (silent error!)
database:
  host: localhost
  port: 5432
database:  # Overwrites above!
  host: prod.db
```

### 4. Anchor Reference Errors
```yaml
# ❌ Reference before definition
app: *defaults
defaults: &defaults
  timeout: 30
```

### 5. Invalid Escape Sequences
```json
{
  "path": "C:\new\test"  // ❌ Invalid \n and \t
}
```

## Debugging Workflow

### Step 1: Read the Error
```
yaml.scanner.ScannerError: while scanning a simple key
  in "config.yaml", line 15, column 1
could not find expected ':'
  in "config.yaml", line 16, column 1
```
→ Check line 15 for missing colon

### Step 2: Validate Syntax
```bash
# YAML validation
yamllint config.yaml
python -c "import yaml; yaml.safe_load(open('config.yaml'))"

# JSON validation
jq empty config.json
python -m json.tool config.json
```

### Step 3: Check Common Issues
- Tabs vs spaces
- Trailing whitespace
- Missing quotes around special values
- Boolean coercion
- Duplicate keys

### Step 4: Use Diff Tools
```bash
# Compare with known-good config
diff -u config.yaml.backup config.yaml
```

## Task Requirements
1. Fix all errors in `buggy-config.yaml`
2. Identify the root cause of each error
3. Verify with validators
4. Document what was wrong

## Error Categories in This Exercise
- Syntax errors (invalid YAML)
- Type errors (wrong data types)
- Logical errors (duplicate keys, wrong anchors)
- Security issues (exposed secrets)

## Hints
- Start with syntax validation
- Check line numbers in error messages
- Look for mixed tabs/spaces
- Watch for implicit type conversion
- Verify anchor definitions come before references

## Solution
Check `fixed-config.yaml` when ready.
