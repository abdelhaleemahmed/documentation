# Exercise 6: YAML Anchors & Aliases

## Objective
Learn to use YAML anchors and aliases to reduce duplication.

## Difficulty
Intermediate (⭐⭐☆)

## What You'll Learn
- Creating anchors with `&`
- Referencing with aliases `*`
- Merging with `<<:`
- DRY (Don't Repeat Yourself) principle

## Task
Create a multi-environment configuration using anchors to avoid repetition.

### Requirements
Create a configuration for 3 environments (dev, staging, production) where:
1. Define default database settings as an anchor
2. Each environment merges the defaults and overrides specific values
3. Use `&defaults` for the anchor
4. Use `<<: *defaults` to merge

### Expected Structure
```yaml
defaults: &defaults
  timeout: 30
  retries: 3
  pool_size: 10

development:
  database:
    <<: *defaults
    host: localhost
    debug: true

staging:
  database:
    <<: *defaults
    host: staging.db.example.com
    debug: false

production:
  database:
    <<: *defaults
    host: prod.db.example.com
    ssl: true
```

## Anchor & Alias Syntax

### Define an Anchor
```yaml
defaults: &my_anchor
  key: value
```

### Reference an Alias
```yaml
copy: *my_anchor  # Complete copy
```

### Merge with Override
```yaml
extended:
  <<: *my_anchor  # Merge
  extra: value     # Add/override
```

## Validation
```bash
python test.py
```

## Hints
- `&name` defines an anchor
- `*name` references it
- `<<:` merges the referenced content
- You can override merged values

## Benefits
- ✅ Reduces duplication
- ✅ Easier maintenance
- ✅ Consistent defaults
- ⚠️ Lost when converting to JSON!

## Solution
Check `solution.yaml` when ready.
