#!/bin/bash
# Exercise 8: Query Solutions

echo "=== Exercise 8: Query Solutions ==="

# 1. Get all active users
echo -e "\n1. Active users:"
jq '.users[] | select(.active == true)' data.json

# 2. Get user emails only
echo -e "\n2. User emails:"
jq '.users[] | .email' data.json

# 3. Get services on port 8080
echo -e "\n3. Services on port 8080:"
jq '.services[] | select(.port == 8080)' data.json

# 4. Count total users
echo -e "\n4. Total users:"
jq '.users | length' data.json

# 5. Update version (prints result, doesn't modify file)
echo -e "\n5. Update version to 2.0.0:"
jq '.app.version = "2.0.0"' data.json | jq '.app'
