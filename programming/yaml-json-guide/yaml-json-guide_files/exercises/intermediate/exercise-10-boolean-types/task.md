# Exercise 10: Boolean Type Gotchas

## Objective
Learn YAML's boolean type system and avoid common pitfalls.

## Difficulty
Intermediate (⭐⭐☆)

## What You'll Learn
- YAML boolean values
- YAML 1.1 vs 1.2 differences
- When to quote strings
- Type coercion issues

## Task
Create a configuration that correctly handles various boolean-like values.

### The Problem
In YAML 1.1, many values become booleans:
```yaml
answer: no        # → false (boolean!)
country: NO       # → false (boolean!)
enabled: yes      # → true (boolean!)
active: on        # → true (boolean!)
```

### Your Task
Create a file with these fields, ensuring correct types:

```yaml
settings:
  debug: true           # boolean true
  ssl: false            # boolean false
  country_code: "NO"    # string "NO", not boolean
  answer: "no"          # string "no", not boolean
  status: "on"          # string "on", not boolean
  flags:
    - yes               # boolean true
    - "yes"             # string "yes"
    - no                # boolean false
    - "no"              # string "no"
```

## YAML Boolean Values (1.1)

These all become `true`:
- `true`, `True`, `TRUE`
- `yes`, `Yes`, `YES`
- `on`, `On`, `ON`

These all become `false`:
- `false`, `False`, `FALSE`
- `no`, `No`, `NO`
- `off`, `Off`, `OFF`

## The Solution
**Quote them** when you want strings:
```yaml
correct: "NO"   # String
wrong: NO       # Boolean false
```

## Validation
```bash
python test.py
```

## Hints
- Always quote country codes (NO, YES)
- Quote user answers (yes, no)
- Quote on/off when they're labels
- Test with: `python -c "import yaml; print(yaml.safe_load('value: NO'))"`

## YAML 1.2 Note
YAML 1.2 fixed this, only `true`/`false` are booleans.
But most parsers still default to YAML 1.1!

## Solution
Check `solution.yaml` when ready.
