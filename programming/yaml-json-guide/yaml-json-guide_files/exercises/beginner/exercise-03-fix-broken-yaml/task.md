# Exercise 3: Fix Broken YAML

## Objective
Learn to debug and fix common YAML syntax errors.

## Difficulty
Beginner (⭐☆☆)

## What You'll Learn
- Identifying YAML syntax errors
- Fixing indentation issues
- Correcting common mistakes
- Using validation tools

## Task
The `broken.yaml` file contains several YAML syntax errors. Your job is to fix them!

### Errors to Find
1. Tab character used for indentation (should be spaces)
2. Missing colon after a key
3. Incorrect indentation level
4. Unquoted special value that becomes boolean

### Expected Output
After fixing, the YAML should represent:
```yaml
server:
  host: localhost
  port: 8080
  country: "NO"  # Must be quoted!
  features:
    - authentication
    - caching
```

## Validation
Run the test to check your solution:

```bash
python test.py
```

Or validate manually:
```bash
yamllint broken.yaml
python -c "import yaml; yaml.safe_load(open('broken.yaml'))"
```

## Hints
- Use `cat -A broken.yaml` to see hidden characters (tabs show as `^I`)
- Count spaces carefully - should be 2 spaces per level
- Some strings like "NO", "yes", "on" need quotes
- Every key needs a colon `:`

## Common YAML Errors
❌ Tabs instead of spaces
❌ Missing colons
❌ Wrong indentation
❌ Unquoted special values

## Solution
Once you've attempted the exercise, check `solution.yaml` for the correct answer.
