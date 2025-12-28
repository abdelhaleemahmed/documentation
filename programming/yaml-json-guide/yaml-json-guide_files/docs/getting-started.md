# Getting Started

Welcome to the YAML & JSON Guide! This guide will help you quickly get up to speed with YAML and JSON configuration formats.

## What You'll Learn

- YAML and JSON syntax fundamentals
- When to use each format
- Common patterns and best practices
- Real-world examples (Kubernetes, Docker, CI/CD)
- Error debugging and troubleshooting
- Security considerations

## Prerequisites

- Basic understanding of text files and configuration
- Familiarity with command line (optional)
- A text editor (VS Code, Sublime, or any editor)

## Quick Start (5 minutes)

### 1. Understanding the Basics

**YAML** - Human-friendly configuration format:
```yaml
# Comments are supported
app:
  name: MyApp
  version: 1.0
  settings:
    debug: true
    port: 8080
```

**JSON** - Structured data exchange format:
```json
{
  "app": {
    "name": "MyApp",
    "version": "1.0",
    "settings": {
      "debug": true,
      "port": 8080
    }
  }
}
```

### 2. Install Tools (Optional)

**Python tools:**
```bash
pip install -r requirements.txt
```

**YAML linter:**
```bash
pip install yamllint
yamllint config.yaml
```

**JSON validator:**
```bash
# Built into Python
python -c "import json; json.load(open('data.json'))"
```

### 3. Try the Examples

Navigate to the `examples/` directory:

```bash
# Kubernetes examples
cd examples/kubernetes/basic-deployment/
cat deployment.yaml

# Docker Compose examples
cd examples/docker-compose/web-app/
cat docker-compose.yml

# CI/CD examples
cd examples/ci-cd/github-actions/
cat workflow.yml
```

### 4. Practice with Exercises

Start with beginner exercises:

```bash
cd exercises/beginner/exercise-01-first-yaml/
cat task.md
# Follow the instructions and create your solution
```

## Learning Path

### Beginner (Week 1)
1. ✅ Read [Quick Reference](quick-reference.md)
2. ✅ Complete exercises 1-5 in `exercises/beginner/`
3. ✅ Review [Common Errors](common-errors.md)
4. ✅ Try YAML to JSON conversion with tools

### Intermediate (Week 2)
1. ✅ Study real-world examples in `examples/`
2. ✅ Complete exercises 6-10 in `exercises/intermediate/`
3. ✅ Read [Misconceptions](misconceptions.md)
4. ✅ Practice with Docker Compose and Kubernetes configs

### Advanced (Week 3)
1. ✅ Complete exercises 11-16 in `exercises/advanced/`
2. ✅ Review [Interview Questions](interview-prep.md)
3. ✅ Build your own projects using YAML/JSON
4. ✅ Contribute to this repository!

## Key Concepts to Master

### YAML Essentials
- ✅ Indentation (2 spaces, no tabs)
- ✅ Key-value pairs
- ✅ Lists and nested structures
- ✅ Multi-line strings (`|` and `>`)
- ✅ Anchors and aliases (`&`, `*`)
- ✅ Comments

### JSON Essentials
- ✅ Object and array syntax
- ✅ String quoting rules
- ✅ No trailing commas
- ✅ Proper escaping
- ✅ Schema validation
- ✅ No comments (in standard JSON)

## Common First-Time Mistakes

### YAML
```yaml
# ❌ Using tabs instead of spaces
	key: value

# ✅ Use spaces only
  key: value

# ❌ Missing colon space
key:value

# ✅ Space after colon
key: value

# ❌ Unquoted special values
country: NO  # Becomes boolean false!

# ✅ Quote special strings
country: "NO"
```

### JSON
```json
// ❌ Trailing comma
{
  "name": "Alice",
  "age": 30,
}

// ✅ No trailing comma
{
  "name": "Alice",
  "age": 30
}

// ❌ Single quotes
{'name': 'Alice'}

// ✅ Double quotes only
{"name": "Alice"}
```

## Tools You'll Use

### Validation Tools
- **yamllint** - YAML syntax checker
- **jsonlint** - JSON syntax checker
- Python's `yaml` and `json` modules

### Conversion Tools
- **yq** - YAML processor (like jq for JSON)
- **jq** - JSON processor
- Python scripts in `tools/converters/`

### Editors
- **VS Code** - Great YAML/JSON support with extensions
- **Sublime Text** - Fast and lightweight
- **PyCharm/IntelliJ** - Excellent validation and autocomplete
- **Vim/Neovim** - For terminal enthusiasts

## Using This Repository

### Directory Structure

```
yaml-json-guide/
├── docs/               # Documentation
│   ├── getting-started.md (you are here)
│   ├── quick-reference.md
│   ├── common-errors.md
│   └── ...
├── examples/           # Real-world examples
│   ├── kubernetes/
│   ├── docker-compose/
│   ├── ci-cd/
│   └── config-management/
├── exercises/          # Practice exercises
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
├── tools/              # Utility scripts
│   ├── converters/
│   ├── validators/
│   └── generators/
├── schemas/            # JSON schemas for validation
└── templates/          # Reusable templates
```

### Running Examples

All examples are ready to use:

```bash
# Validate a YAML file
yamllint examples/kubernetes/basic-deployment/deployment.yaml

# Convert YAML to JSON
python tools/converters/yaml_to_json.py examples/kubernetes/basic-deployment/deployment.yaml

# Validate against schema
python tools/validators/validate_json.py data.json schemas/app-config.schema.json
```

## Getting Help

### Resources in This Repo
- 📖 [Quick Reference](quick-reference.md) - Fast syntax lookup
- ❗ [Common Errors](common-errors.md) - 38 documented errors
- 🧩 [Misconceptions](misconceptions.md) - Myths debunked
- 🧠 [Interview Prep](interview-prep.md) - Practice questions
- ❓ [FAQ](faq.md) - Frequently asked questions

### External Resources
- [YAML Specification](https://yaml.org/spec/)
- [JSON Specification (RFC 8259)](https://www.rfc-editor.org/rfc/rfc8259)
- [JSON Schema](https://json-schema.org/)

### Community
- Open an issue on GitHub for questions
- Submit a pull request to improve the guide
- Share your examples and exercises

## Next Steps

1. **Read the Quick Reference** - Get familiar with syntax
   - [Quick Reference Guide](quick-reference.md)

2. **Try Your First Exercise** - Hands-on practice
   - `exercises/beginner/exercise-01-first-yaml/`

3. **Explore Examples** - See real-world usage
   - `examples/kubernetes/`
   - `examples/docker-compose/`

4. **Bookmark Common Errors** - Reference when debugging
   - [Common Errors](common-errors.md)

## Tips for Success

1. **Practice regularly** - Do one exercise per day
2. **Use validation tools** - Catch errors early
3. **Study real examples** - Learn from production configs
4. **Understand the why** - Don't just memorize syntax
5. **Test your configs** - Always validate before deploying
6. **Keep security in mind** - Never commit secrets

## Quick Commands Cheatsheet

```bash
# Validate YAML
yamllint config.yaml

# Validate JSON
python -c "import json; json.load(open('data.json'))"

# Convert YAML to JSON
python tools/converters/yaml_to_json.py input.yaml

# Convert JSON to YAML
python tools/converters/json_to_yaml.py input.json

# Query YAML
yq '.app.database.host' config.yaml

# Query JSON
jq '.app.database.host' data.json

# Check for secrets
python tools/validators/check_secrets.py config.yaml
```

---

**Ready to dive in?** Start with the [Quick Reference](quick-reference.md) or jump straight into [Exercise 1](../exercises/beginner/exercise-01-first-yaml/task.md)!

**Questions?** Check the [FAQ](faq.md) or [Common Errors](common-errors.md) documentation.
