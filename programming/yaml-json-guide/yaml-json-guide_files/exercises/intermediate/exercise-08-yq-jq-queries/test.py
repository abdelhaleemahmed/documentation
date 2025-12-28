#!/usr/bin/env python3
"""Test script for Exercise 8"""

import json
import sys
from pathlib import Path

def test_queries():
    """Test that data file is valid for querying."""
    data_path = Path(__file__).parent / 'data.json'

    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ data.json not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False

    print("✅ data.json is valid!")
    print("\nTry these queries:")
    print("  jq '.users[] | select(.active == true)' data.json")
    print("  jq '.users[] | .email' data.json")
    print("\nSee solution_queries.sh for all answers")
    return True

if __name__ == '__main__':
    sys.exit(0 if test_queries() else 1)
