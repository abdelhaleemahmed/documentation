#!/usr/bin/env python3
"""Test script for Exercise 9: Multi-Document YAML"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)


def test_multi_document(filename='starter.yaml'):
    """Test multi-document YAML file."""
    file_path = Path(__file__).parent / filename

    if not file_path.exists():
        print(f"❌ File not found: {filename}")
        return False

    try:
        with open(file_path, 'r') as f:
            docs = list(yaml.safe_load_all(f))
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error: {e}")
        return False

    errors = []
    passed = []

    # Check document count
    if len(docs) < 3:
        errors.append(f"Expected 3 documents, found {len(docs)}")
        return False
    else:
        passed.append(f"Found {len(docs)} documents ✓")

    # Check for required kinds
    kinds = [doc.get('kind') for doc in docs if doc]
    required_kinds = ['ConfigMap', 'Service', 'Deployment']

    for kind in required_kinds:
        if kind in kinds:
            passed.append(f"Found {kind} resource ✓")
        else:
            errors.append(f"Missing {kind} resource")

    # Print results
    if passed:
        print("\n✅ Passed checks:")
        for p in passed:
            print(f"  • {p}")

    if errors:
        print("\n❌ Failed checks:")
        for e in errors:
            print(f"  • {e}")
        return False
    else:
        print("\n🎉 Perfect multi-document YAML!")
        print("\nDocuments found:")
        for i, doc in enumerate(docs, 1):
            if doc:
                print(f"  {i}. {doc.get('kind', 'Unknown')} - {doc.get('metadata', {}).get('name', 'unnamed')}")
        return True


if __name__ == '__main__':
    sys.exit(0 if test_multi_document() else 1)
