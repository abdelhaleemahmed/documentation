# Exercise 2: Convert JSON to YAML

## Objective
Learn to convert JSON data to YAML format while understanding the differences.

## Difficulty
Beginner (⭐☆☆)

## What You'll Learn
- JSON vs YAML syntax differences
- Converting between formats
- YAML list syntax
- Nested structures

## Task
Convert the following JSON configuration to YAML format:

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "name": "myapp",
    "users": [
      "admin",
      "developer",
      "readonly"
    ]
  }
}
```

### Requirements
1. Use YAML syntax (no curly braces!)
2. Use 2-space indentation
3. Convert the JSON array to a YAML list
4. Maintain the same data structure

## Starting Point
Use the `starter.yaml` file and convert the JSON from `input.json`.

## Conversion Guide

### JSON to YAML Conversion:

**JSON:**
```json
{
  "key": "value",
  "nested": {
    "field": 123
  },
  "list": ["a", "b", "c"]
}
```

**YAML:**
```yaml
key: value
nested:
  field: 123
list:
  - a
  - b
  - c
```

## Validation
Run the test to check your solution:

```bash
python test.py
```

Or manually convert and validate:

```bash
# Using the repo's converter
python ../../../tools/converters/json_to_yaml.py input.json output.yaml

# Validate result
python ../../../tools/validators/validate_yaml.py output.yaml
```

## Hints
- Remove curly braces `{}`
- Remove square brackets `[]` and use `-` for list items
- Remove commas (YAML doesn't use them)
- Remove quotes around keys
- Use colons `:` instead of colons with quotes `"key":`
- Each list item starts with `- `
- Nested objects use indentation, not braces

## Expected Output
When you run `python test.py`, you should see:

```
✅ All tests passed!
- Correct database host
- Correct port (number)
- Correct database name
- Correct users list (3 items)
- Valid YAML syntax
```

## Common Mistakes to Avoid
❌ Leaving JSON braces and commas
❌ Forgetting to add dashes for list items
❌ Incorrect indentation for nested fields
❌ Quoting all strings (YAML strings can be unquoted)

## Bonus Challenge
After completing the exercise:
1. Add a new field `ssl: true` to the database configuration
2. Add another user to the users list
3. Convert your result back to JSON using the converter tool

## Solution
Once you've attempted the exercise, check `solution.yaml` for the correct answer.

## Next Steps
- Exercise 3: Fix Broken YAML
- Learn about YAML multi-line strings
- Explore YAML anchors and aliases
