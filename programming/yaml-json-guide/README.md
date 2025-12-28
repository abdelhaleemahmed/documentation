---
title: YAML & JSON Guide Repository
description: Companion repository with examples, exercises, tools, and resources for the YAML & JSON Mega Guide
layout: default
---

# YAML & JSON Guide - Companion Repository

**Official companion repository for the [YAML & JSON Mega Guide](link-to-guide)**

This repository contains all the examples, exercises, tools, and resources from the guide, ready to download and use in your projects.

> 📖 **New here?** Start with our **[Complete User Guide](USER_GUIDE.md)** - it explains how to use all 105+ files in this repository!

> 🤔 **Guide vs Repository?** Read **[GUIDE_VS_REPO.md](GUIDE_VS_REPO.md)** to understand how they work together (spoiler: this repo does NOT replace the guide - they complement each other!)

---

## 📁 Repository Structure

```
yaml-json-guide/
├── examples/               # Real-world examples from the guide
│   ├── kubernetes/        # K8s deployments, services, configs
│   ├── docker-compose/    # Docker Compose examples
│   ├── ci-cd/             # GitHub Actions, CircleCI, GitLab CI
│   ├── config-management/ # Application configs
│   └── README.md
│
├── exercises/             # Practice exercises with solutions
│   ├── beginner/         # Exercises 1-5
│   ├── intermediate/     # Exercises 6-10
│   ├── advanced/         # Exercises 11-16
│   └── README.md
│
├── tools/                # Utility scripts and tools
│   ├── converters/       # YAML ↔ JSON conversion scripts
│   ├── validators/       # Validation scripts
│   ├── generators/       # Config generators
│   └── README.md
│
├── schemas/              # JSON Schemas for validation
│   ├── app-config.schema.json
│   ├── database-config.schema.json
│   └── kubernetes.schema.json
│
├── templates/            # Ready-to-use templates
│   ├── docker-compose.template.yml
│   ├── github-actions.template.yml
│   ├── kubernetes-deployment.template.yml
│   └── README.md
│
├── tests/                # Test files for validation
│   └── README.md
│
├── docs/                 # Documentation files
│   ├── getting-started.md
│   ├── contributing.md
│   ├── faq.md
│   ├── troubleshooting.md
│   ├── changelog.md
│   ├── common-errors.md        # 38 documented errors
│   ├── misconceptions.md       # 10 myths debunked
│   ├── interview-prep.md       # Interview questions
│   └── quick-reference.md      # Quick summary
│
├── .editorconfig         # Editor configuration
├── .gitignore           # Git ignore rules
├── .yamllint.yml        # YAML linting configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
├── LICENSE              # MIT License
└── README.md            # This file
```

---

## 🚀 Quick Start

### Clone the Repository

```bash
git clone https://github.com/yourusername/yaml-json-guide.git
cd yaml-json-guide
```

### Try an Example

```bash
# Run a Docker Compose example
cd examples/docker-compose/web-app
docker-compose up

# Validate a Kubernetes config
kubectl apply -f examples/kubernetes/deployment.yaml --dry-run=client

# Convert YAML to JSON
python tools/converters/yaml_to_json.py examples/config-management/app-config.yaml
```

### Work on Exercises

```bash
cd exercises/beginner
# Read the README for instructions
# Open exercise files in your editor
# Compare with solutions when done
```

---

## 📖 Complete User Guide

**→ [USER_GUIDE.md](USER_GUIDE.md) - Read this first!**

New to the repository? Our comprehensive user guide explains:
- ✅ How to use all 105+ files in this repository
- ✅ Step-by-step learning paths for beginners
- ✅ Developer workflows and tool usage
- ✅ Teaching resources and curriculum
- ✅ Troubleshooting common issues
- ✅ Real-world usage examples

**Choose your path:**
- 🎓 **Learner?** → Start with [Learning Path](USER_GUIDE.md#for-learners---complete-learning-path)
- 💻 **Developer?** → Jump to [Tools & Workflows](USER_GUIDE.md#for-developers---practical-tools)
- 👨‍🏫 **Teacher?** → Check [Educational Resources](USER_GUIDE.md#for-teachers---educational-resources)
- 🚀 **Need examples?** → Browse [Using Examples](USER_GUIDE.md#using-the-examples)

---

## 📚 Examples

### Kubernetes Examples
- ✅ Complete deployment with ConfigMap and Secret
- ✅ StatefulSet for databases
- ✅ Ingress configuration
- ✅ CronJob examples
- ✅ Multi-container pods

**Location:** `examples/kubernetes/`

### Docker Compose Examples
- ✅ Web app with database
- ✅ Microservices architecture
- ✅ Development environment
- ✅ Production-ready setup

**Location:** `examples/docker-compose/`

### CI/CD Examples
- ✅ GitHub Actions workflows
- ✅ CircleCI pipelines
- ✅ GitLab CI configurations
- ✅ Jenkins pipelines

**Location:** `examples/ci-cd/`

### Configuration Management
- ✅ Multi-environment configs
- ✅ Secret management patterns
- ✅ Database configurations
- ✅ API service configs

**Location:** `examples/config-management/`

---

## 💪 Exercises

### Beginner (Exercises 1-5)
- Creating first YAML/JSON files
- Format conversions
- Fixing syntax errors
- Multi-line strings

**Difficulty:** 🟢 Easy
**Time:** 30-60 minutes total
**Location:** `exercises/beginner/`

### Intermediate (Exercises 6-10)
- Anchors and aliases
- Schema validation
- Using yq/jq tools
- Multi-document YAML
- Type handling

**Difficulty:** 🟡 Medium
**Time:** 2-3 hours total
**Location:** `exercises/intermediate/`

### Advanced (Exercises 11-16)
- Performance optimization
- Secure config management
- Kubernetes deployments
- Complex debugging
- Legacy system migration
- Complete config management system

**Difficulty:** 🔴 Hard
**Time:** 4-8 hours total
**Location:** `exercises/advanced/`

---

## 🛠️ Tools

### Converters
- **yaml_to_json.py** - Convert YAML to JSON with validation
- **json_to_yaml.py** - Convert JSON to YAML with formatting
- **batch_convert.sh** - Convert multiple files at once
- **format_yaml.py** - Auto-format and fix YAML files

**Location:** `tools/converters/`

**Usage:**
```bash
python tools/converters/yaml_to_json.py input.yaml output.json
python tools/converters/json_to_yaml.py input.json output.yaml
```

### Validators
- **validate_yaml.py** - YAML syntax and schema validation
- **validate_json.py** - JSON syntax and schema validation
- **validate_k8s.sh** - Kubernetes YAML validation
- **check_secrets.py** - Scan for accidentally committed secrets

**Location:** `tools/validators/`

**Usage:**
```bash
python tools/validators/validate_yaml.py config.yaml schema.json
python tools/validators/check_secrets.py .
```

### Generators
- **generate_config.py** - Interactive config generator
- **generate_k8s.py** - Kubernetes resource generator
- **generate_compose.py** - Docker Compose generator

**Location:** `tools/generators/`

**Usage:**
```bash
python tools/generators/generate_config.py --env production
```

---

## 📋 Templates

Ready-to-use, production-tested templates for common scenarios:

- **docker-compose.template.yml** - Full-stack web application
- **github-actions.template.yml** - CI/CD with testing and deployment
- **kubernetes-deployment.template.yml** - Complete K8s deployment
- **config-multi-env.template.yml** - Multi-environment configuration
- **.pre-commit-config.template.yaml** - Pre-commit hooks for YAML/JSON

**Location:** `templates/`

**Usage:**
1. Copy template to your project
2. Replace `{{placeholders}}` with your values
3. Customize as needed
4. Run and test

---

## ✅ JSON Schemas

Pre-built JSON Schemas for common configuration patterns:

- **app-config.schema.json** - General application configuration
- **database-config.schema.json** - Database connection settings
- **kubernetes.schema.json** - Kubernetes resource validation
- **docker-compose.schema.json** - Docker Compose validation

**Location:** `schemas/`

**Usage with Python:**
```python
import json
import jsonschema

with open('schemas/app-config.schema.json') as f:
    schema = json.load(f)

with open('config.json') as f:
    config = json.load(f)

jsonschema.validate(config, schema)  # Raises error if invalid
```

**Usage with VS Code:**
Add to your `settings.json`:
```json
{
  "yaml.schemas": {
    "./schemas/app-config.schema.json": "config/*.yaml"
  }
}
```

---

## 🧪 Testing

Run the test suite to validate all examples and tools:

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/

# Run specific test category
pytest tests/test_converters.py
pytest tests/test_validators.py

# Run with coverage
pytest --cov=tools tests/
```

---

## 🎯 Use Cases

### For Learners
- 📖 Work through exercises step-by-step
- 🔍 Study real-world examples
- 🛠️ Use tools to experiment safely
- ✅ Validate your work with schemas

### For Developers
- 📋 Copy-paste production-ready templates
- 🔄 Convert between formats quickly
- ✓ Validate configs before deploying
- 🔐 Scan for security issues

### For DevOps Engineers
- 🚀 Deploy example Kubernetes configs
- 🐳 Use Docker Compose examples
- 🤖 Set up CI/CD pipelines
- 📊 Manage multi-environment configs

### For Teams
- 📚 Onboard new team members
- 🎓 Training resource for YAML/JSON
- 🔧 Shared tools and utilities
- 📖 Reference documentation

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Issues
- Found a bug in an example? [Open an issue](../../issues)
- Example doesn't work? Let us know!
- Have a suggestion? We'd love to hear it!

### Contributing Examples
1. Fork the repository
2. Create a new branch: `git checkout -b feature/new-example`
3. Add your example in the appropriate folder
4. Include a README explaining the example
5. Test thoroughly
6. Submit a pull request

### Contributing Tools
1. Fork the repository
2. Create a new branch: `git checkout -b feature/new-tool`
3. Add your tool to `tools/`
4. Add tests to `tests/`
5. Update documentation
6. Submit a pull request

### Contribution Guidelines
- ✅ All examples must be tested and working
- ✅ Include README for complex examples
- ✅ Follow existing code style
- ✅ Add comments for clarity
- ✅ No secrets or credentials in code
- ✅ Use `.env.example` for secret templates

---

## 📖 Documentation

### Main Guide
Read the complete YAML & JSON Mega Guide: [Link to guide]

**The Guide provides comprehensive theory and explanations:**
- **~58,000 words** covering 200+ concepts
- **Deep conceptual understanding** - WHY things work
- **14 Mermaid diagrams** for visual learning
- **220+ code examples** across multiple languages
- **Interview preparation** guide included
- **Misconceptions debunked** - 10 common myths
- **Performance analysis** and security deep-dives

**This Repository provides practical resources:**
- **105+ working files** - examples, exercises, tools
- **Hands-on practice** - 16 exercises with automated tests
- **Developer tools** - converters, validators, scanners
- **Production templates** - copy-paste ready configs
- **Quick reference** - fast syntax lookup

→ **[Read how they work together](GUIDE_VS_REPO.md)**

### Standalone Documentation (No Guide Required)

**Quick References:**
- [`docs/quick-reference.md`](docs/quick-reference.md) - Essential rules and concepts at a glance
- [`docs/common-errors.md`](docs/common-errors.md) - 38 errors with step-by-step solutions
- [`docs/troubleshooting.md`](docs/troubleshooting.md) - Debugging workflow and prevention

**Learning Resources:**
- [`docs/misconceptions.md`](docs/misconceptions.md) - 10 YAML/JSON myths debunked with examples
- [`docs/interview-prep.md`](docs/interview-prep.md) - 15+ interview questions with expert answers
- [`docs/faq.md`](docs/faq.md) - Frequently asked questions

**Getting Started:**
- [`docs/getting-started.md`](docs/getting-started.md) - Quick start guide for the repository
- [`docs/contributing.md`](docs/contributing.md) - How to contribute to this project

### Example READMEs
Each example folder has its own README with:
- Description of the example
- Prerequisites
- Usage instructions
- Expected output
- Troubleshooting tips

### Tool Documentation
Each tool has inline documentation and usage examples.

Run any tool with `--help` for detailed usage:
```bash
python tools/converters/yaml_to_json.py --help
python tools/validators/validate_yaml.py --help
```

---

## 🔧 Setup & Configuration

### Prerequisites
- **Python 3.8+** for Python tools
- **Node.js 14+** for JavaScript tools
- **Docker** for Docker examples
- **kubectl** for Kubernetes examples
- **yq** for YAML processing
- **jq** for JSON processing

### Installation

**Install Python dependencies:**
```bash
pip install -r requirements.txt
```

**Install CLI tools:**
```bash
# Install yq (YAML processor)
brew install yq  # macOS
sudo apt-get install yq  # Ubuntu

# Install jq (JSON processor)
brew install jq  # macOS
sudo apt-get install jq  # Ubuntu
```

**Set up pre-commit hooks:**
```bash
pip install pre-commit
pre-commit install
```

**Configure your editor:**
Copy `.editorconfig` to your project root for consistent formatting.

---

## 📝 License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to use these examples, tools, and templates in your projects!

---

## 🌟 Star This Repo!

If you find this repository helpful, please star it! ⭐

It helps others discover these resources and motivates us to add more examples and tools.

---

## 🔗 Links

- **Main Guide:** [YAML & JSON Mega Guide](link-to-guide)
- **Issues:** [Report bugs or suggest features](../../issues)
- **Discussions:** [Ask questions or share ideas](../../discussions)
- **Pull Requests:** [Contribute examples or tools](../../pulls)

---

## 📊 Repository Stats

- **Examples:** 50+ real-world examples
- **Exercises:** 16 hands-on exercises with solutions
- **Tools:** 10+ utility scripts
- **Templates:** 5 production-ready templates
- **Schemas:** 4 JSON Schema validators
- **Languages:** Python, JavaScript, Bash, YAML, JSON
- **Technologies:** Kubernetes, Docker, CI/CD, Config Management

---

## 🎓 Learning Path

**Recommended order for beginners:**

1. **Read the Main Guide** - Start with Quick Start section
2. **Work through Beginner Exercises** - Practice basic syntax
3. **Study Examples** - See real-world usage
4. **Try Intermediate Exercises** - Learn advanced features
5. **Use Tools** - Automate validation and conversion
6. **Attempt Advanced Exercises** - Build production skills
7. **Contribute** - Share your own examples!

---

## 💡 Pro Tips

- 🔖 **Bookmark this repo** for quick reference
- 📁 **Clone locally** to work offline
- 🔄 **Pull regularly** for new examples and updates
- 🧪 **Experiment** in a separate branch
- 💬 **Join discussions** to learn from others
- 🤝 **Contribute** your own examples

---

## 🚀 Quick Commands Cheatsheet

```bash
# Convert YAML to JSON
python tools/converters/yaml_to_json.py input.yaml output.json

# Validate YAML with schema
python tools/validators/validate_yaml.py config.yaml schema.json

# Check for secrets
python tools/validators/check_secrets.py .

# Format YAML file
python tools/converters/format_yaml.py config.yaml

# Run all tests
pytest tests/

# Start Docker Compose example
cd examples/docker-compose/web-app && docker-compose up

# Validate Kubernetes config
kubectl apply -f examples/kubernetes/deployment.yaml --dry-run=client

# Use yq to query YAML
yq eval '.database.host' examples/config-management/app-config.yaml

# Use jq to query JSON
jq '.database.host' examples/config-management/app-config.json
```

---

## 📬 Contact & Support

- **Issues:** Use GitHub Issues for bugs and feature requests
- **Discussions:** Use GitHub Discussions for questions and ideas
- **Email:** support@example.com (for private matters)
- **Twitter:** @yamlguide (for updates and tips)

---

## 🙏 Acknowledgments

Thanks to all contributors who have helped make this repository better!

Special thanks to:
- The YAML and JSON specification maintainers
- The open-source community
- All the learners who provided feedback

---

**Happy learning! 🎉**

Master YAML and JSON with practical, production-ready examples!
