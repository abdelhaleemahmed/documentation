# Contributing Guide

Thank you for your interest in contributing to the YAML & JSON Guide! This document will help you get started.

## How to Contribute

We welcome contributions in many forms:
- 🐛 Bug reports and error corrections
- 📖 Documentation improvements
- 💡 New examples and use cases
- 🎓 Additional exercises
- 🔧 Tool improvements
- ✨ New features and content

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/yaml-json-guide.git
cd yaml-json-guide
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

Branch naming conventions:
- `feature/` - New features or content
- `fix/` - Bug fixes or corrections
- `docs/` - Documentation updates
- `examples/` - New examples
- `exercises/` - New exercises

### 3. Make Your Changes

Follow the guidelines below for specific types of contributions.

### 4. Test Your Changes

```bash
# Validate YAML files
yamllint **/*.yaml

# Validate JSON files
find . -name "*.json" -exec python -m json.tool {} \; > /dev/null

# Run tests (if applicable)
pytest tests/
```

### 5. Commit Your Changes

Follow conventional commit format:

```bash
git commit -m "feat: add Docker Compose example for microservices"
git commit -m "fix: correct indentation in Kubernetes deployment"
git commit -m "docs: update FAQ with anchor questions"
```

Commit message format:
- `feat:` - New features or content
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `test:` - Test additions or updates
- `refactor:` - Code refactoring
- `style:` - Formatting changes

### 6. Push and Create Pull Request

```bash
git push origin your-branch-name
```

Then create a Pull Request on GitHub with:
- Clear title describing the change
- Description of what and why
- Reference to related issues (if any)

## Contribution Guidelines

### Documentation

When adding or updating documentation:

- ✅ Use clear, concise language
- ✅ Provide code examples
- ✅ Include both correct and incorrect examples
- ✅ Explain the "why", not just the "what"
- ✅ Use consistent formatting
- ✅ Link to related documentation
- ❌ Don't assume prior knowledge
- ❌ Don't use overly technical jargon without explanation

**Example structure:**
```markdown
## Feature Name

**What it does:** Brief description

**Why it matters:** Practical context

**Example:**
```yaml
# ❌ WRONG - Why this is wrong
incorrect: example

# ✅ CORRECT - Why this is right
correct: example
```

**Common mistakes:**
- Mistake 1 and how to avoid it
- Mistake 2 and how to fix it
```

### Code Examples

All code examples should be:

- ✅ **Valid and tested** - Must parse without errors
- ✅ **Realistic** - Reflect real-world usage
- ✅ **Well-commented** - Explain non-obvious parts
- ✅ **Complete** - Include necessary context
- ✅ **Consistent** - Follow style guidelines

**YAML examples:**
```yaml
# Use 2-space indentation
# Include comments for clarity
# Show both right and wrong patterns
app:
  name: example
  version: "1.0.0"
  settings:
    debug: false
    port: 8080
```

**JSON examples:**
```json
{
  "description": "Always valid JSON",
  "formatting": "2-space indent",
  "quotes": "double only",
  "trailingCommas": "never"
}
```

### New Examples

When adding examples to `examples/`:

1. **Create a directory** for your example
2. **Include these files:**
   - `README.md` - Explanation and usage
   - Example YAML/JSON files
   - Expected output (if applicable)
3. **Document:**
   - What the example demonstrates
   - How to use it
   - Common issues
   - Related concepts

**Example structure:**
```
examples/
└── your-category/
    └── your-example/
        ├── README.md
        ├── config.yaml
        ├── expected-output.json
        └── notes.md
```

### New Exercises

When adding exercises to `exercises/`:

1. **Choose appropriate difficulty:**
   - `beginner/` - Basic syntax and patterns
   - `intermediate/` - Real-world scenarios
   - `advanced/` - Complex patterns and debugging

2. **Include these files:**
   - `task.md` - Problem description
   - `starter.yaml` or `starter.json` - Starting point
   - `solution.yaml` or `solution.json` - Correct answer
   - `test.py` - Automated validation

3. **Make it practical:**
   - Real-world scenarios
   - Clear learning objectives
   - Incremental difficulty
   - Good error messages

**Exercise template:**
```markdown
# Exercise N: Title

## Objective
What you'll learn from this exercise.

## Task
What you need to do, step by step.

## Hints
- Hint 1
- Hint 2

## Validation
How to check your solution:
```bash
python test.py
```

## Learning Points
- Key concept 1
- Key concept 2
```

### Tools

When adding or modifying tools in `tools/`:

- ✅ Use Python 3.8+ features
- ✅ Include type hints
- ✅ Add docstrings
- ✅ Handle errors gracefully
- ✅ Support `-h/--help` flag
- ✅ Write unit tests
- ✅ Update requirements.txt if needed

**Tool template:**
```python
#!/usr/bin/env python3
"""
Tool description.

Usage:
    python tool.py input.yaml
"""

import argparse
import sys
from typing import Any, Dict

def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Tool description')
    parser.add_argument('input', help='Input file')
    args = parser.parse_args()

    try:
        # Tool logic here
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
```

### Schemas

When adding JSON schemas to `schemas/`:

- ✅ Follow JSON Schema specification
- ✅ Include descriptions for all fields
- ✅ Provide examples
- ✅ Set appropriate validation rules
- ✅ Document required vs optional fields

### Templates

When adding templates to `templates/`:

- ✅ Make them production-ready
- ✅ Include comprehensive comments
- ✅ Cover common use cases
- ✅ Provide usage instructions
- ✅ Show customization points

## Code Style

### YAML Style
- Use 2-space indentation
- No tabs (ever)
- Include comments for complex sections
- Quote strings when ambiguous
- Use `|` for multi-line, `>` for folded
- Consistent anchor naming

### JSON Style
- Use 2-space indentation
- Double quotes only
- No trailing commas
- No comments (except in JSONC examples)
- Pretty-printed format

### Python Style
- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use f-strings for formatting
- Docstrings for all functions

### Markdown Style
- Use ATX-style headers (`#`)
- Code blocks with language tags
- Blank line before/after code blocks
- Use tables for comparisons
- Link to related documents

## Testing

### Validation Tests

Before submitting:

```bash
# YAML validation
yamllint **/*.yaml **/*.yml

# JSON validation
find . -name "*.json" -exec python -m json.tool {} \; > /dev/null

# Python tests
pytest tests/ -v

# Tool tests
python tools/converters/yaml_to_json.py examples/kubernetes/basic-deployment/deployment.yaml
```

### Documentation Tests

- [ ] All links work
- [ ] Code examples are valid
- [ ] Commands execute successfully
- [ ] Screenshots are up-to-date (if any)

## Pull Request Checklist

Before submitting your PR:

- [ ] Code follows style guidelines
- [ ] All files validated (YAML/JSON/Python)
- [ ] Tests pass (if applicable)
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] Branch is up to date with main
- [ ] PR description is clear and complete

## Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] New example
- [ ] New exercise
- [ ] Tool improvement

## Changes Made
- Change 1
- Change 2

## Testing
How you tested these changes

## Related Issues
Fixes #123 (if applicable)

## Screenshots
If relevant (e.g., documentation examples)
```

## Review Process

1. **Automated checks** - CI runs validation
2. **Code review** - Maintainer reviews changes
3. **Feedback** - Address any comments
4. **Approval** - Maintainer approves PR
5. **Merge** - Changes merged to main

## Community Guidelines

### Be Respectful
- Welcome newcomers
- Provide constructive feedback
- Assume good intentions
- Help others learn

### Be Clear
- Explain your reasoning
- Ask questions if unclear
- Provide context
- Link to relevant resources

### Be Patient
- Reviews take time
- Maintainers are volunteers
- Not all PRs will be merged
- Feedback helps everyone improve

## Recognition

Contributors are recognized in:
- GitHub contributors page
- Release notes (for significant contributions)
- Hall of fame (coming soon)

## Questions?

- Open an issue for questions
- Check existing issues first
- Provide clear problem description
- Include relevant examples

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to the YAML & JSON Guide!** Your help makes this resource better for everyone. 🎉
