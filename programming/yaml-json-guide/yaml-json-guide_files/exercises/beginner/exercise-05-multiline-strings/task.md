# Exercise 5: YAML Multiline Strings

## Objective
Learn to use YAML's multiline string operators (`|` and `>`).

## Difficulty
Beginner (⭐☆☆)

## What You'll Learn
- Literal block scalar (`|`) - preserves newlines
- Folded block scalar (`>`) - folds into single line
- When to use each style
- How they differ

## Task
Create a YAML file with configuration that includes both types of multiline strings:

### Requirements
1. Use `|` (literal) for a shell script that must preserve newlines
2. Use `>` (folded) for a long description that should become one line

### Expected Structure
```yaml
deployment:
  name: "myapp"
  description: >
    This is a very long description
    that spans multiple lines but
    should be folded into a single
    line when parsed.

  script: |
    #!/bin/bash
    echo "Starting deployment..."
    npm install
    npm run build
    echo "Deployment complete!"
```

## Understanding `|` vs `>`

### Literal (`|`) - Preserves Newlines
```yaml
script: |
  line 1
  line 2
# Result: "line 1\nline 2"
```

Use for:
- Shell scripts
- Code blocks
- Formatted text
- Anything where newlines matter

### Folded (`>`) - Folds into Single Line
```yaml
description: >
  This becomes
  one line
# Result: "This becomes one line"
```

Use for:
- Long descriptions
- Paragraphs
- Text that should wrap

## Validation
Run the test to check your solution:

```bash
python test.py
```

## Hints
- `|` keeps each line separate (preserves `\n`)
- `>` joins lines with spaces
- Indentation after `|` or `>` must be consistent
- Empty lines are preserved in both styles

## Common Mistakes
❌ Using `>` for scripts (breaks on newlines)
❌ Using `|` for descriptions (keeps unnecessary newlines)
❌ Inconsistent indentation after `|` or `>`
❌ Forgetting the space after `|` or `>`

## Examples

### Script (use `|`)
```yaml
install_script: |
  npm install
  npm test
  npm run build
```

### Description (use `>`)
```yaml
about: >
  This application provides
  a complete solution for
  managing your data.
```

## Solution
Once you've attempted the exercise, check `solution.yaml` for the correct answer.
