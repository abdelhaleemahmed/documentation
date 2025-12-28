# Exercise 4: Working with JSON Arrays

## Objective
Learn to work with JSON arrays and nested structures.

## Difficulty
Beginner (⭐☆☆)

## What You'll Learn
- Creating JSON arrays
- Nested objects in arrays
- Proper JSON syntax
- Array vs object structure

## Task
Create a JSON file representing a list of users with the following structure:

```json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "active": true
  },
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "active": false
  },
  {
    "id": 3,
    "name": "Charlie",
    "email": "charlie@example.com",
    "active": true
  }
]
```

### Requirements
1. Root element must be an array `[]`
2. Each user is an object in the array
3. Use correct data types (numbers, strings, booleans)
4. No trailing commas!
5. Use double quotes for strings

## Validation
Run the test to check your solution:

```bash
python test.py
```

Or validate manually:
```bash
python -m json.tool starter.json
```

## Hints
- Arrays start with `[` and end with `]`
- Objects inside arrays are separated by commas
- Last item in array has NO trailing comma
- Use `true`/`false` (lowercase) for booleans

## JSON Arrays vs Objects

**Array** (ordered list):
```json
["apple", "banana", "cherry"]
```

**Object** (key-value pairs):
```json
{"fruit": "apple", "count": 5}
```

**Array of objects**:
```json
[
  {"name": "Alice"},
  {"name": "Bob"}
]
```

## Common Mistakes
❌ Trailing comma after last item
❌ Single quotes instead of double quotes
❌ Quoting numbers or booleans
❌ Missing commas between array items

## Solution
Once you've attempted the exercise, check `solution.json` for the correct answer.
