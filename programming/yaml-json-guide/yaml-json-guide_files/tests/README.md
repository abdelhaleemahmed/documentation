# Tests

This directory contains test suites for the YAML & JSON Guide.

## Test Structure

```
tests/
├── unit/              # Unit tests for individual components
├── integration/       # Integration tests for complete workflows
└── fixtures/          # Test data and sample files
```

## Running Tests

### All Tests
```bash
# Python tests
pytest tests/

# JavaScript tests
npm test
```

### Specific Test Suites
```bash
# Unit tests only
pytest tests/unit/

# Integration tests only
pytest tests/integration/

# Specific test file
pytest tests/unit/test_parser.py
```

### Exercise Tests
Each exercise has its own test file:
```bash
# Run a specific exercise test
python exercises/beginner/exercise-01-basic-yaml/test.py

# Run all exercise tests
find exercises -name "test.py" -exec python {} \;
```

## Writing Tests

### Example Test Structure
```python
#!/usr/bin/env python3
"""Test for specific functionality"""

import sys
from pathlib import Path

def test_feature():
    """Test description."""
    # Arrange
    input_data = {...}

    # Act
    result = process(input_data)

    # Assert
    assert result == expected
    print("✅ Test passed")
    return True

if __name__ == '__main__':
    sys.exit(0 if test_feature() else 1)
```

## Test Coverage

Run tests with coverage reporting:
```bash
pytest --cov=yaml_json_guide --cov-report=html tests/
```

View coverage report:
```bash
open htmlcov/index.html
```

## Continuous Integration

Tests are automatically run on:
- Every push to main branch
- Every pull request
- Scheduled daily runs

See `.github/workflows/test.yml` for CI configuration.

## Test Data

Test fixtures are located in `tests/fixtures/`:
- `valid/` - Valid YAML/JSON files
- `invalid/` - Files with intentional errors
- `schemas/` - JSON Schema files
- `examples/` - Real-world configuration examples

## Dependencies

Install test dependencies:
```bash
pip install -r requirements-test.txt
```

Required packages:
- pytest
- pytest-cov
- PyYAML
- jsonschema
- pyyaml-lint
