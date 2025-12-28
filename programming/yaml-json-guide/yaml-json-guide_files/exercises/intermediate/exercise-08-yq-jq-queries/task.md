# Exercise 8: Querying with yq and jq

## Objective
Learn to query and manipulate YAML/JSON using yq and jq command-line tools.

## Difficulty
Intermediate (⭐⭐☆)

## What You'll Learn
- Using jq to query JSON
- Using yq to query YAML
- Filtering data
- Transforming structures

## Task
Practice common query operations on the provided data files.

### Sample Queries

#### JSON with jq
```bash
# Get a field
jq '.app.name' data.json

# Get array element
jq '.users[0]' data.json

# Filter array
jq '.users[] | select(.active == true)' data.json

# Get specific fields
jq '.users[] | {name, email}' data.json

# Count array items
jq '.users | length' data.json
```

#### YAML with yq
```bash
# Get a field
yq '.app.name' config.yaml

# Get array element
yq '.services[0]' config.yaml

# Filter
yq '.services[] | select(.port == 8080)' config.yaml

# Convert to JSON
yq -o=json config.yaml

# Update value
yq '.app.version = "2.0.0"' config.yaml
```

## Exercises

Write queries to:
1. Get all active users
2. Get user emails only
3. Get services running on port 8080
4. Count total users
5. Update app version to 2.0.0

## Installation

```bash
# jq
sudo apt-get install jq  # Ubuntu/Debian
brew install jq          # macOS

# yq
brew install yq          # macOS
# Or download from: https://github.com/mikefarah/yq
```

## Testing
```bash
# Run the queries
bash test_queries.sh
```

## Common jq Patterns

```bash
# Get field
jq '.field'

# Array access
jq '.[0]'
jq '.array[0]'

# Filter
jq '.[] | select(.active == true)'

# Map
jq '.users[] | .name'

# Multiple fields
jq '{name: .name, email: .email}'

# Length
jq '. | length'
```

## Solution
Check `solution_queries.sh` for answers.
