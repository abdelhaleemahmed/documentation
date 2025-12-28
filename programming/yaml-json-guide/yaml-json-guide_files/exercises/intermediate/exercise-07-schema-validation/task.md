# Exercise 7: JSON Schema Validation

## Objective
Learn to validate JSON data against a JSON Schema.

## Difficulty
Intermediate (⭐⭐☆)

## What You'll Learn
- Creating JSON Schemas
- Validation rules
- Required vs optional fields
- Type constraints

## Task
Create both a JSON Schema and a valid JSON data file that conforms to it.

### Requirements
Create a schema for a user profile with:
- Required: `name`, `email`, `age`
- Optional: `bio`, `website`
- Constraints:
  - `name`: string, 1-100 characters
  - `email`: string, email format
  - `age`: integer, minimum 18
  - `bio`: string, max 500 characters
  - `website`: string, URL format

### Schema Template
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["name", "email", "age"],
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100
    },
    "email": {
      "type": "string",
      "format": "email"
    },
    "age": {
      "type": "integer",
      "minimum": 18
    }
  }
}
```

## Validation
```bash
python test.py
```

Or manually:
```bash
python ../../../tools/validators/validate_json.py data.json schema.json
```

## Hints
- `required` array lists mandatory fields
- `properties` defines each field's validation
- `format` provides built-in validators (email, url, etc.)
- `minimum`/`maximum` for numbers
- `minLength`/`maxLength` for strings

## JSON Schema Keywords
- `type`: "string", "integer", "boolean", "array", "object"
- `required`: Array of required field names
- `properties`: Field definitions
- `minimum`/`maximum`: Number constraints
- `minLength`/`maxLength`: String length
- `format`: Built-in formats (email, url, date-time)
- `enum`: Allowed values
- `pattern`: Regex validation

## Solution
Check `schema.json` and `data.json` when ready.
