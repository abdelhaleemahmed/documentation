# Exercise 1: Your First YAML File

## Objective
Learn to create a basic YAML file with correct syntax and formatting.

## Difficulty
Beginner (⭐☆☆)

## What You'll Learn
- YAML basic syntax
- Key-value pairs
- Proper indentation
- Data types (strings, numbers, booleans)

## Task
Create a YAML configuration file for a simple application with the following requirements:

### Required Structure
```yaml
app:
  name: "MyFirstApp"
  version: "1.0.0"
  port: 3000
  debug: true
```

### Requirements
1. Use **2 spaces** for indentation (no tabs!)
2. Include all fields exactly as shown
3. Use proper data types:
   - `name` and `version` should be strings
   - `port` should be a number
   - `debug` should be a boolean

## Starting Point
Use the `starter.yaml` file in this directory.

## Validation
Run the test to check your solution:

```bash
python test.py
```

## Hints
- YAML uses spaces for indentation, never tabs
- Strings can be quoted or unquoted (quotes are safer)
- Numbers don't need quotes
- Booleans are `true` or `false`
- Each level of nesting adds 2 spaces of indentation

## Expected Output
When you run `python test.py`, you should see:

```
✅ All tests passed!
- Correct app name
- Correct version
- Correct port (number)
- Correct debug flag (boolean)
- Proper indentation
```

## Common Mistakes to Avoid
❌ Using tabs instead of spaces
❌ Missing colons after keys
❌ Incorrect indentation levels
❌ Quoting numbers or booleans

## Solution
Once you've attempted the exercise, check `solution.yaml` for the correct answer.

## Next Steps
After completing this exercise:
1. Try modifying values
2. Add more fields
3. Move on to Exercise 2: JSON to YAML conversion
