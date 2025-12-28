# YAML & JSON Guide - Complete User Guide

**Welcome!** This guide will help you make the most of the 105+ files in this repository.

> 🤔 **Important:** This repository is a **companion** to the YAML & JSON Guide, not a replacement. See **[GUIDE_VS_REPO.md](GUIDE_VS_REPO.md)** for details on how they work together.

---

## 📚 Table of Contents

1. [Quick Start - Choose Your Path](#quick-start---choose-your-path)
2. [Repository Structure Overview](#repository-structure-overview)
3. [For Learners - Complete Learning Path](#for-learners---complete-learning-path)
4. [For Developers - Practical Tools](#for-developers---practical-tools)
5. [For Teachers - Educational Resources](#for-teachers---educational-resources)
6. [Using the Exercises](#using-the-exercises)
7. [Using the Examples](#using-the-examples)
8. [Using the Tools](#using-the-tools)
9. [Common Workflows](#common-workflows)
10. [Troubleshooting](#troubleshooting)

---

## Quick Start - Choose Your Path

### 🎓 I'm New to YAML/JSON
**Start here → Perfect for beginners**

```bash
# 1. Read the getting started guide
cat docs/getting-started.md

# 2. Check the quick reference
cat docs/quick-reference.md

# 3. Do your first exercise
cd exercises/beginner/exercise-01-basic-yaml
cat task.md
# Edit starter.yaml
python test.py
```

**Estimated time:** 2-3 hours to complete all beginner exercises

### 💻 I Need Config Files for My Project
**Start here → Copy production-ready templates**

```bash
# 1. Browse available templates
ls templates/

# 2. Copy what you need
cp templates/docker-compose.template.yml my-project/docker-compose.yml
cp templates/kubernetes-deployment.template.yml my-project/deployment.yaml

# 3. Customize for your project
# Edit the files with your specific values

# 4. Validate before using
python tools/validators/validate_yaml.py my-project/deployment.yaml
```

**Estimated time:** 15-30 minutes

### 🔧 I Need to Convert/Validate Files
**Start here → Use the tools**

```bash
# Install dependencies
pip install -r requirements.txt

# Convert YAML to JSON
python tools/converters/yaml_to_json.py config.yaml output.json

# Validate YAML syntax
python tools/validators/validate_yaml.py config.yaml

# Check for hardcoded secrets
python tools/validators/check_secrets.py config.yaml
```

**Estimated time:** 5 minutes per file

### 👨‍🏫 I'm Teaching YAML/JSON
**Start here → Use structured curriculum**

```bash
# 1. Review the course structure
cat docs/getting-started.md

# 2. Assign exercises progressively
# Week 1: Beginner exercises (1-5)
# Week 2: Intermediate exercises (6-10)
# Week 3: Advanced exercises (11-16)

# 3. Use examples for demonstrations
cd examples/kubernetes/basic-deployment
cat README.md

# 4. Point students to documentation
cat docs/common-errors.md  # For troubleshooting
```

**Estimated time:** 3-week curriculum

### 🚀 I Need Real-World Examples
**Start here → Browse examples**

```bash
# Kubernetes configurations
cd examples/kubernetes/
ls  # basic-deployment, statefulset, ingress, cronjob

# CI/CD pipelines
cd examples/ci-cd/
ls  # github-actions, circleci, gitlab-ci, jenkins

# Docker setups
cd examples/docker-compose/
ls  # web-app, development-environment, microservices

# Configuration management
cd examples/config-management/
ls  # database-configs, multi-environment, secret-management
```

**Estimated time:** 10 minutes to find what you need

---

## Repository Structure Overview

```
yaml-json-guide/
├── 📖 docs/              → Read these first (guides & reference)
├── 🎯 exercises/         → Hands-on practice (16 exercises)
├── 💡 examples/          → Real-world configurations (29 files)
├── 🔧 tools/             → Utilities (converters, validators)
├── 📋 templates/         → Copy-paste ready configs (5 templates)
├── ✓ schemas/            → Validation schemas (4 schemas)
└── 🧪 tests/             → Testing framework
```

### What Each Directory Contains

| Directory | Purpose | When to Use |
|-----------|---------|-------------|
| **docs/** | Learning materials, guides, FAQ | Start here for understanding |
| **exercises/** | 16 hands-on coding exercises | Learn by doing |
| **examples/** | Production-ready configurations | See real-world usage |
| **tools/** | Python scripts for conversion/validation | Automate your workflow |
| **templates/** | Starter templates for common needs | Quick project setup |
| **schemas/** | JSON Schema files for validation | Enforce configuration structure |
| **tests/** | Testing utilities and examples | Validate your learning |

---

## For Learners - Complete Learning Path

### Phase 1: Foundations (Week 1)
**Goal:** Understand YAML/JSON syntax and basic concepts

#### Day 1-2: Reading
```bash
# Read in this order:
1. docs/getting-started.md       # Start here
2. docs/quick-reference.md       # Syntax cheat sheet
3. docs/faq.md                   # Common questions
```

#### Day 3-5: Beginner Exercises
```bash
cd exercises/beginner/

# Exercise 1: Create your first YAML file
cd exercise-01-basic-yaml
cat task.md                    # Read the task
# Edit starter.yaml
python test.py                 # Check your work
cat solution.yaml              # Compare with solution

# Exercise 2: JSON to YAML conversion
cd ../exercise-02-json-to-yaml
cat task.md
# Edit starter.yaml
python test.py

# Exercise 3: Fix broken YAML
cd ../exercise-03-fix-broken-yaml
cat task.md
# Fix broken.yaml
python test.py

# Exercise 4: JSON arrays
cd ../exercise-04-json-array
cat task.md
# Edit data.json
python test.py

# Exercise 5: Multi-line strings
cd ../exercise-05-multiline-strings
cat task.md
# Edit config.yaml
python test.py
```

**✅ Checkpoint:** Can you create valid YAML/JSON files?

### Phase 2: Intermediate Skills (Week 2)
**Goal:** Master advanced YAML features and validation

#### Day 1-3: Intermediate Exercises
```bash
cd exercises/intermediate/

# Exercise 6: Anchors and aliases (DRY principle)
cd exercise-06-anchors-aliases
cat task.md
# Edit config.yaml
python test.py

# Exercise 7: JSON Schema validation
cd ../exercise-07-schema-validation
cat task.md
# Edit data.json to match schema
python test.py

# Exercise 8: Command-line queries (jq/yq)
cd ../exercise-08-yq-jq-queries
cat task.md
# Create queries
python test.py

# Exercise 9: Multi-document YAML
cd ../exercise-09-multi-document
cat task.md
# Edit kubernetes.yaml
python test.py

# Exercise 10: Boolean type gotchas
cd ../exercise-10-boolean-types
cat task.md
# Fix config.yaml
python test.py
```

#### Day 4-5: Study Real Examples
```bash
# Kubernetes configurations
cd examples/kubernetes/basic-deployment
cat README.md
cat deployment.yaml
cat service.yaml

# Docker Compose
cd examples/docker-compose/web-app
cat README.md
cat docker-compose.yml
```

**✅ Checkpoint:** Can you use anchors, validate with schemas, and avoid common pitfalls?

### Phase 3: Advanced Topics (Week 3)
**Goal:** Production-ready skills and best practices

#### Day 1-4: Advanced Exercises
```bash
cd exercises/advanced/

# Exercise 11: Performance benchmarking
cd exercise-11-performance
cat task.md
python benchmark.py

# Exercise 12: Secure configuration
cd ../exercise-12-secure-config
cat task.md
# Study insecure.yaml vs secure.yaml
python test.py

# Exercise 13: Kubernetes debugging
cd ../exercise-13-kubernetes
cat task.md
# Fix broken-deployment.yaml
python test.py

# Exercise 14: Real-world debugging
cd ../exercise-14-debug-error
cat task.md
# Fix buggy-config.yaml
python test.py

# Exercise 15: Legacy migration
cd ../exercise-15-legacy-migration
cat task.md
# Convert legacy-config.ini to modern YAML
python migrate.py

# Exercise 16: Custom parser
cd ../exercise-16-custom-parser
cat task.md
# Study parser.py implementation
python test.py
```

#### Day 5: Study Advanced Examples
```bash
# CI/CD pipelines
cd examples/ci-cd/
cat circleci/config.yml
cat gitlab-ci/.gitlab-ci.yml
cat jenkins/Jenkinsfile

# Configuration management
cd examples/config-management/
cat multi-environment/config.prod.yaml
cat secret-management/vault-config.yaml

# Microservices
cd examples/docker-compose/microservices/
cat docker-compose.yml
```

**✅ Checkpoint:** Can you secure configs, debug errors, and implement advanced patterns?

### Phase 4: Mastery (Ongoing)
**Goal:** Apply knowledge to real projects

1. **Build a project** using the templates
2. **Contribute** examples of your own
3. **Teach others** using this repository
4. **Reference** docs/common-errors.md when troubleshooting

---

## For Developers - Practical Tools

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import yaml; print('PyYAML installed')"
python -c "import jsonschema; print('jsonschema installed')"
```

### Daily Workflows

#### Converting Files
```bash
# YAML → JSON
python tools/converters/yaml_to_json.py input.yaml output.json

# JSON → YAML
python tools/converters/json_to_yaml.py input.json output.yaml

# Batch conversion
find . -name "*.yaml" -exec python tools/converters/yaml_to_json.py {} {}.json \;
```

#### Validating Configurations
```bash
# Validate YAML syntax
python tools/validators/validate_yaml.py config.yaml

# Validate JSON with schema
python tools/validators/validate_json.py config.json schemas/app-config.schema.json

# Check for hardcoded secrets (CRITICAL before commit!)
python tools/validators/check_secrets.py config.yaml
```

#### Generating Templates
```bash
# Generate configuration template
python tools/generators/config_template.py --type database --format yaml > db-config.yaml

# Available types: database, server, api, cache
python tools/generators/config_template.py --help
```

### Integration with Your Project

#### Pre-commit Hook
Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
# Validate YAML files before commit

echo "Validating YAML files..."
for file in $(git diff --cached --name-only | grep -E '\.(yaml|yml)$'); do
    python tools/validators/validate_yaml.py "$file"
    if [ $? -ne 0 ]; then
        echo "❌ Validation failed for $file"
        exit 1
    fi

    python tools/validators/check_secrets.py "$file"
    if [ $? -ne 0 ]; then
        echo "❌ Secrets detected in $file"
        exit 1
    fi
done

echo "✅ All YAML files validated"
```

```bash
chmod +x .git/hooks/pre-commit
```

#### CI/CD Integration
Copy GitHub Actions workflow:
```bash
cp .github/workflows/validate.yml your-project/.github/workflows/
```

This automatically validates all YAML/JSON files on every commit.

#### Project Template Setup
```bash
# Quick project setup
mkdir my-app && cd my-app

# Copy templates
cp ../yaml-json-guide/templates/docker-compose.template.yml docker-compose.yml
cp ../yaml-json-guide/templates/kubernetes-deployment.template.yml k8s/deployment.yaml
cp ../yaml-json-guide/templates/github-actions.template.yml .github/workflows/ci.yml

# Customize for your project
# Edit the files with your specific values

# Validate
python ../yaml-json-guide/tools/validators/validate_yaml.py docker-compose.yml
```

---

## For Teachers - Educational Resources

### Course Structure

#### 3-Week Intensive Course

**Week 1: Foundations**
- Lecture: docs/getting-started.md
- Lab: exercises/beginner/ (1-5)
- Quiz: docs/interview-prep.md (questions 1-5)
- Assignment: Create a multi-environment config

**Week 2: Intermediate Concepts**
- Lecture: docs/quick-reference.md (advanced features)
- Lab: exercises/intermediate/ (6-10)
- Quiz: docs/interview-prep.md (questions 6-10)
- Assignment: Implement a Kubernetes deployment

**Week 3: Production Skills**
- Lecture: docs/common-errors.md
- Lab: exercises/advanced/ (11-16)
- Final Project: Build complete application config
- Code Review: Use examples/ as reference

#### Workshop Format (1 Day)

**Morning (9am-12pm): Fundamentals**
- Hour 1: Presentation from docs/getting-started.md
- Hour 2: Live coding exercises 1-3
- Hour 3: Group exercise - fix broken configs

**Afternoon (1pm-5pm): Real-World Applications**
- Hour 1: CI/CD pipeline examples
- Hour 2: Kubernetes configurations
- Hour 3: Security best practices (exercise 12)
- Hour 4: Build their own config + code review

### Teaching Materials

#### Slides Content
Use these as slide topics:
1. docs/getting-started.md → Introduction slides
2. docs/misconceptions.md → "Myths" slide
3. docs/common-errors.md → "Mistakes to Avoid" slides
4. examples/ → "Real-World Examples" slides

#### Lab Assignments
Each exercise includes:
- `task.md` - Assignment description
- `starter.*` - File for students to edit
- `solution.*` - Reference solution
- `test.py` - Automated grading script

```bash
# Distribute to students
cp -r exercises/beginner/exercise-01-basic-yaml student-folders/

# Students work on starter file
# Grading is automated
cd student-folders/exercise-01-basic-yaml
python test.py  # Shows pass/fail
```

#### Grading Rubric
| Criterion | Points | Check |
|-----------|--------|-------|
| YAML/JSON syntax valid | 30% | `python test.py` passes |
| Requirements met | 40% | Task completion |
| Best practices used | 20% | No secrets, proper formatting |
| Documentation | 10% | Comments where needed |

#### Discussion Questions
Use `docs/interview-prep.md` for:
- Class discussions
- Quiz questions
- Exam preparation
- Interview practice

### Live Demonstration Scripts

#### Demo 1: YAML Basics (15 minutes)
```bash
# Show simple YAML
cat examples/basic/simple-config.yaml

# Convert to JSON to show equivalence
python tools/converters/yaml_to_json.py examples/basic/simple-config.yaml output.json
cat output.json

# Show validation
python tools/validators/validate_yaml.py examples/basic/simple-config.yaml
```

#### Demo 2: Common Mistakes (20 minutes)
```bash
# Show broken file
cat exercises/beginner/exercise-03-fix-broken-yaml/broken.yaml

# Try to load it (fails)
python -c "import yaml; yaml.safe_load(open('broken.yaml'))"

# Show the errors
cat docs/common-errors.md | grep "Mixed Tabs and Spaces"

# Show the fix
cat exercises/beginner/exercise-03-fix-broken-yaml/solution.yaml
```

#### Demo 3: Real-World Config (20 minutes)
```bash
# Show production Kubernetes config
cat examples/kubernetes/basic-deployment/deployment.yaml

# Explain each section
# Discuss security (no hardcoded secrets)
cat examples/config-management/secret-management/kubernetes-secrets.yaml

# Show how to validate
kubectl apply --dry-run=client -f deployment.yaml
```

---

## Using the Exercises

### Exercise Structure
Every exercise follows the same pattern:

```
exercise-XX-name/
├── task.md           → Read this first (what to do)
├── starter.*         → Edit this file
├── solution.*        → Reference answer
└── test.py           → Run this to check your work
```

### Workflow for Each Exercise

#### Step 1: Read the Task
```bash
cd exercises/beginner/exercise-01-basic-yaml
cat task.md
```

The task file contains:
- **Objective** - What you'll learn
- **Difficulty** - Complexity level
- **Task** - What to do
- **Requirements** - Must-have features
- **Hints** - Helpful tips

#### Step 2: Work on the Starter File
```bash
# Open in your editor
nano starter.yaml
# or
code starter.yaml
# or
vim starter.yaml
```

Complete the requirements listed in task.md.

#### Step 3: Test Your Solution
```bash
python test.py
```

Output examples:
```
✅ All tests passed!
```
or
```
❌ Test failed: Missing required field 'database.host'
```

#### Step 4: Compare with Solution (if stuck)
```bash
cat solution.yaml
```

**Note:** Try to solve it yourself first! Only check the solution if you're stuck for more than 15 minutes.

#### Step 5: Understand Why
Read the solution comments to understand:
- Why certain choices were made
- What best practices are followed
- What mistakes to avoid

### Exercise Tips

#### Beginner Exercises (1-5)
- **Focus on:** Syntax, basic structure
- **Common issues:** Indentation, data types
- **Time per exercise:** 15-30 minutes
- **Help:** docs/getting-started.md

#### Intermediate Exercises (6-10)
- **Focus on:** Advanced features, validation
- **Common issues:** Anchor references, boolean coercion
- **Time per exercise:** 30-45 minutes
- **Help:** docs/quick-reference.md

#### Advanced Exercises (11-16)
- **Focus on:** Real-world scenarios, security
- **Common issues:** Complex debugging, architecture decisions
- **Time per exercise:** 45-90 minutes
- **Help:** docs/common-errors.md, examples/

### Getting Unstuck

If you're stuck on an exercise:

1. **Re-read the task** - Did you miss a requirement?
2. **Check error messages** - `python test.py` tells you what's wrong
3. **Review documentation** - Especially docs/common-errors.md
4. **Look at examples** - Similar patterns in examples/
5. **Check solution** - But understand WHY, don't just copy

---

## Using the Examples

### Example Categories

#### 1. Kubernetes Configurations
**Location:** `examples/kubernetes/`

```bash
# Basic deployment
cd examples/kubernetes/basic-deployment/
cat README.md                    # Overview
cat deployment.yaml              # App deployment
cat service.yaml                 # Load balancer
cat configmap.yaml               # Configuration
cat secret.yaml                  # Secrets

# Deploy to your cluster
kubectl apply -f .

# StatefulSet (databases)
cd examples/kubernetes/statefulset/
cat statefulset.yaml             # Persistent storage

# Ingress (routing)
cd examples/kubernetes/ingress/
cat ingress.yaml                 # HTTP routing

# CronJob (scheduled tasks)
cd examples/kubernetes/cronjob/
cat cronjob.yaml                 # Scheduled jobs
```

**When to use:**
- Setting up Kubernetes applications
- Understanding K8s resource structure
- Production-ready configurations

#### 2. Docker Compose Setups
**Location:** `examples/docker-compose/`

```bash
# Simple web application
cd examples/docker-compose/web-app/
cat docker-compose.yml
docker-compose up -d

# Full development environment
cd examples/docker-compose/development-environment/
cat docker-compose.yml           # Includes DB, cache, mail server
docker-compose up -d

# Microservices architecture
cd examples/docker-compose/microservices/
cat docker-compose.yml           # Complete microservices stack
docker-compose up -d
```

**When to use:**
- Local development setup
- Testing multi-container applications
- Learning microservices architecture

#### 3. CI/CD Pipelines
**Location:** `examples/ci-cd/`

```bash
# GitHub Actions
cd examples/ci-cd/github-actions/
cat node-ci.yml
# Copy to your repo: .github/workflows/

# CircleCI
cd examples/ci-cd/circleci/
cat config.yml
# Copy to your repo: .circleci/

# GitLab CI
cd examples/ci-cd/gitlab-ci/
cat .gitlab-ci.yml
# Copy to repo root

# Jenkins
cd examples/ci-cd/jenkins/
cat Jenkinsfile
# Copy to repo root
```

**When to use:**
- Setting up automated testing
- Implementing continuous deployment
- Learning CI/CD best practices

#### 4. Configuration Management
**Location:** `examples/config-management/`

```bash
# Database configurations
cd examples/config-management/database-configs/
cat mysql.yaml                   # MySQL setup
cat postgresql.yaml              # PostgreSQL setup
cat mongodb.yaml                 # MongoDB setup

# Multi-environment configs
cd examples/config-management/multi-environment/
cat config.dev.yaml              # Development
cat config.staging.yaml          # Staging
cat config.prod.yaml             # Production

# Secret management
cd examples/config-management/secret-management/
cat vault-config.yaml            # HashiCorp Vault
cat aws-secrets-manager.yaml     # AWS Secrets Manager
cat kubernetes-secrets.yaml      # Kubernetes Secrets
```

**When to use:**
- Setting up databases
- Managing multiple environments
- Implementing secure secret storage

### How to Adapt Examples

#### Step 1: Copy the Example
```bash
cp -r examples/docker-compose/web-app my-project/
cd my-project
```

#### Step 2: Identify Placeholders
Look for values to customize:
- `example.com` → your domain
- `myapp` → your app name
- `8080` → your port
- `${VARIABLES}` → your environment variables

#### Step 3: Customize
```bash
# Edit the file
nano docker-compose.yml

# Replace placeholders
sed -i 's/myapp/your-app-name/g' docker-compose.yml
```

#### Step 4: Validate
```bash
# Validate syntax
python ../yaml-json-guide/tools/validators/validate_yaml.py docker-compose.yml

# Test locally
docker-compose config  # Validates docker-compose syntax
docker-compose up -d   # Test it works
```

#### Step 5: Deploy
```bash
# For Docker Compose
docker-compose up -d

# For Kubernetes
kubectl apply -f deployment.yaml

# For CI/CD
git add .github/workflows/ci.yml
git commit -m "Add CI pipeline"
git push
```

---

## Using the Tools

### Tool Overview

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `yaml_to_json.py` | Convert YAML to JSON | .yaml file | .json file |
| `json_to_yaml.py` | Convert JSON to YAML | .json file | .yaml file |
| `validate_yaml.py` | Validate YAML syntax | .yaml file | Pass/fail + errors |
| `validate_json.py` | Validate JSON + schema | .json file | Pass/fail + errors |
| `check_secrets.py` | Find hardcoded secrets | .yaml/.json | List of secrets |
| `config_template.py` | Generate config templates | Type + format | Template file |

### Tool Usage

#### 1. YAML to JSON Converter
**File:** `tools/converters/yaml_to_json.py`

```bash
# Basic usage
python tools/converters/yaml_to_json.py input.yaml output.json

# Pretty print (indented)
python tools/converters/yaml_to_json.py input.yaml output.json --indent 2

# Example
python tools/converters/yaml_to_json.py examples/kubernetes/basic-deployment/deployment.yaml deployment.json
```

**Use cases:**
- API expects JSON, you have YAML
- Comparing formats
- JSON processing with jq

#### 2. JSON to YAML Converter
**File:** `tools/converters/json_to_yaml.py`

```bash
# Basic usage
python tools/converters/json_to_yaml.py input.json output.yaml

# Example
python tools/converters/json_to_yaml.py package.json package.yaml
```

**Use cases:**
- YAML is more readable
- Kubernetes requires YAML
- Adding comments (JSON doesn't support)

#### 3. YAML Validator
**File:** `tools/validators/validate_yaml.py`

```bash
# Validate single file
python tools/validators/validate_yaml.py config.yaml

# Validate multiple files
python tools/validators/validate_yaml.py *.yaml

# With detailed output
python tools/validators/validate_yaml.py config.yaml --verbose
```

**Checks for:**
- Syntax errors (tabs, indentation)
- Invalid structure
- Duplicate keys
- Type mismatches

#### 4. JSON Validator with Schema
**File:** `tools/validators/validate_json.py`

```bash
# Validate syntax only
python tools/validators/validate_json.py config.json

# Validate against schema
python tools/validators/validate_json.py config.json schemas/app-config.schema.json

# Example
python tools/validators/validate_json.py my-config.json schemas/database-config.schema.json
```

**Use cases:**
- Enforce configuration structure
- Catch missing required fields
- Type checking

#### 5. Secret Scanner
**File:** `tools/validators/check_secrets.py`

```bash
# Scan for secrets
python tools/validators/check_secrets.py config.yaml

# Scan entire directory
find . -name "*.yaml" -exec python tools/validators/check_secrets.py {} \;
```

**Detects:**
- Hardcoded passwords
- API keys
- AWS credentials
- Database credentials
- JWT tokens

**Output example:**
```
❌ SECRETS DETECTED in config.yaml:
  - Line 12: password: secret123
  - Line 18: api_key: sk_live_abc123

Use environment variables instead:
  password: ${DB_PASSWORD}
  api_key: ${API_KEY}
```

#### 6. Config Template Generator
**File:** `tools/generators/config_template.py`

```bash
# Generate database config
python tools/generators/config_template.py --type database --format yaml

# Generate server config
python tools/generators/config_template.py --type server --format json

# Save to file
python tools/generators/config_template.py --type api --format yaml > api-config.yaml
```

**Available types:**
- `database` - Database connection config
- `server` - Web server config
- `api` - API client config
- `cache` - Cache (Redis) config

### Automation Scripts

#### Validate All YAML Files
Create `scripts/validate-all.sh`:
```bash
#!/bin/bash
echo "Validating all YAML files..."
find . -name "*.yaml" -o -name "*.yml" | while read file; do
    echo "Checking $file..."
    python tools/validators/validate_yaml.py "$file"
    if [ $? -ne 0 ]; then
        echo "❌ Failed: $file"
        exit 1
    fi
done
echo "✅ All files valid"
```

#### Check for Secrets Before Commit
Create `scripts/pre-commit-check.sh`:
```bash
#!/bin/bash
echo "Scanning for secrets..."
find . -name "*.yaml" -o -name "*.yml" -o -name "*.json" | while read file; do
    python tools/validators/check_secrets.py "$file"
    if [ $? -ne 0 ]; then
        echo "❌ Secrets found in $file"
        echo "Fix before committing!"
        exit 1
    fi
done
echo "✅ No secrets detected"
```

---

## Common Workflows

### Workflow 1: Starting a New Project

**Scenario:** You're starting a new web application project.

```bash
# 1. Create project directory
mkdir my-web-app && cd my-web-app

# 2. Copy templates you need
cp path/to/yaml-json-guide/templates/docker-compose.template.yml docker-compose.yml
cp path/to/yaml-json-guide/templates/github-actions.template.yml .github/workflows/ci.yml

# 3. Customize templates
# Edit docker-compose.yml
# - Change service names
# - Update ports
# - Add your containers

# 4. Set up environment variables
cat > .env << EOF
DB_USERNAME=myuser
DB_PASSWORD=changeme
API_KEY=your_key_here
EOF

# Add to .gitignore
echo ".env" >> .gitignore

# 5. Validate configuration
python path/to/yaml-json-guide/tools/validators/validate_yaml.py docker-compose.yml

# 6. Test locally
docker-compose up -d

# 7. Check for secrets before committing
python path/to/yaml-json-guide/tools/validators/check_secrets.py docker-compose.yml

# 8. Commit
git init
git add .
git commit -m "Initial project setup"
```

### Workflow 2: Converting Existing JSON to YAML

**Scenario:** Your project uses JSON configs, you want to migrate to YAML.

```bash
# 1. Convert files
python tools/converters/json_to_yaml.py config.json config.yaml
python tools/converters/json_to_yaml.py database.json database.yaml

# 2. Add comments (YAML advantage)
nano config.yaml
# Add explanatory comments

# 3. Use environment variables for secrets
# Replace hardcoded values with ${VAR}

# 4. Validate
python tools/validators/validate_yaml.py config.yaml

# 5. Test in your application
# Update code to load .yaml instead of .json

# 6. Keep both for transition period
# Delete JSON files once YAML is stable
```

### Workflow 3: Deploying to Kubernetes

**Scenario:** Deploy your application to Kubernetes.

```bash
# 1. Start with the example
cp -r examples/kubernetes/basic-deployment my-k8s-config
cd my-k8s-config

# 2. Customize deployment.yaml
nano deployment.yaml
# - Change image name
# - Update resource limits
# - Set environment variables

# 3. Customize service.yaml
nano service.yaml
# - Change service name
# - Update ports

# 4. Create secrets (don't hardcode!)
kubectl create secret generic app-secrets \
  --from-literal=db-password=secretpass \
  --from-literal=api-key=myapikey

# 5. Update secret.yaml to reference these
nano secret.yaml

# 6. Validate locally
kubectl apply --dry-run=client -f deployment.yaml
kubectl apply --dry-run=server -f deployment.yaml

# 7. Deploy
kubectl apply -f .

# 8. Verify
kubectl get pods
kubectl get services
kubectl logs <pod-name>
```

### Workflow 4: Setting Up CI/CD

**Scenario:** Add automated testing to your repository.

```bash
# 1. Choose your CI platform
# For GitHub Actions:
mkdir -p .github/workflows
cp examples/ci-cd/github-actions/node-ci.yml .github/workflows/

# For GitLab CI:
cp examples/ci-cd/gitlab-ci/.gitlab-ci.yml .

# For CircleCI:
mkdir -p .circleci
cp examples/ci-cd/circleci/config.yml .circleci/

# 2. Customize for your project
nano .github/workflows/node-ci.yml
# - Update Node version
# - Add your test commands
# - Configure deployment

# 3. Add validation workflow
cp .github/workflows/validate.yml .github/workflows/
# This validates all YAML/JSON on every commit

# 4. Commit and push
git add .github/workflows/
git commit -m "Add CI/CD pipeline"
git push

# 5. Check pipeline
# Visit your repository's Actions/Pipelines tab
```

### Workflow 5: Managing Multiple Environments

**Scenario:** You need different configs for dev, staging, and production.

```bash
# 1. Copy multi-environment example
cp -r examples/config-management/multi-environment config/

# 2. Customize each environment
nano config/config.dev.yaml      # Development settings
nano config/config.staging.yaml  # Staging settings
nano config/config.prod.yaml     # Production settings

# 3. Use environment variable to select
export APP_ENV=development
# or
export APP_ENV=production

# 4. In your application
# Load config based on APP_ENV
# config_file = f"config/config.{os.getenv('APP_ENV')}.yaml"

# 5. Validate all configs
python tools/validators/validate_yaml.py config/*.yaml

# 6. Store secrets in environment-specific .env files
# .env.development
# .env.staging
# .env.production
# (Add all .env* to .gitignore!)
```

### Workflow 6: Learning Exercise Completion

**Scenario:** You're working through the exercises.

```bash
# 1. Start with beginner exercises
cd exercises/beginner/exercise-01-basic-yaml

# 2. Read the task
cat task.md
# - Note the objective
# - Understand requirements
# - Read hints

# 3. Work on the starter file
code starter.yaml
# Complete the requirements

# 4. Test your solution
python test.py

# If tests fail:
# - Read error message carefully
# - Check task.md requirements
# - Review docs/common-errors.md
# - Try again

# 5. When tests pass, move to next exercise
cd ../exercise-02-json-to-yaml
cat task.md
# Repeat process

# 6. If stuck, check solution
cat solution.yaml
# But understand WHY it works

# 7. Move to intermediate after completing all beginner
cd ../../intermediate/exercise-06-anchors-aliases
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: "YAML parsing error"
**Symptoms:**
```
yaml.scanner.ScannerError: while scanning a simple key
```

**Solutions:**
```bash
# Check for common issues:
1. Mixed tabs and spaces
   - Solution: Use only spaces (2 spaces per indent level)

2. Missing colons
   - Solution: Every key needs a colon: `key: value`

3. Wrong indentation
   - Solution: Use consistent 2-space indentation

# Validate file
python tools/validators/validate_yaml.py your-file.yaml

# Read common errors guide
cat docs/common-errors.md | grep "Indentation"
```

#### Issue 2: "Exercise test fails"
**Symptoms:**
```
❌ Test failed: Missing required field
```

**Solutions:**
```bash
# 1. Re-read the task carefully
cat task.md

# 2. Check exactly what the test expects
python test.py  # Read error message

# 3. Compare with requirements
# Make sure you have all required fields

# 4. Check data types
# YAML is sensitive to types:
port: 8080      # Integer
port: "8080"    # String (wrong!)

# 5. Still stuck? Check solution
cat solution.yaml
# But understand the differences
diff starter.yaml solution.yaml
```

#### Issue 3: "Boolean conversion issue"
**Symptoms:**
```
country: NO    # Becomes false!
enabled: yes   # Becomes true (unexpected)
```

**Solution:**
```bash
# Read the boolean exercise
cat exercises/intermediate/exercise-10-boolean-types/task.md

# Fix: Always quote strings that look like booleans
country: "NO"      # String
enabled: true      # Explicit boolean
answer: "yes"      # String (not boolean)

# Check docs
cat docs/common-errors.md | grep -A 20 "Boolean Type Coercion"
```

#### Issue 4: "Secrets detected in config"
**Symptoms:**
```
❌ Secrets found: password: secret123
```

**Solution:**
```bash
# Never hardcode secrets!

# Wrong:
database:
  password: secret123

# Right:
database:
  password: ${DB_PASSWORD}

# Set environment variable:
export DB_PASSWORD=secret123

# Or use .env file (don't commit it!)
echo "DB_PASSWORD=secret123" >> .env
echo ".env" >> .gitignore

# Read security guide
cat exercises/advanced/exercise-12-secure-config/task.md
```

#### Issue 5: "Kubernetes deployment fails"
**Symptoms:**
```
Error from server: error validating deployment
```

**Solution:**
```bash
# 1. Validate locally first
kubectl apply --dry-run=client -f deployment.yaml

# 2. Check for common issues:
#    - Labels match selectors
#    - Required fields present
#    - Resource limits set

# 3. Study the example
cat examples/kubernetes/basic-deployment/deployment.yaml

# 4. Use kubectl explain
kubectl explain deployment.spec.template.spec.containers

# 5. Do the exercise
cd exercises/advanced/exercise-13-kubernetes
cat task.md
```

#### Issue 6: "Docker Compose validation fails"
**Symptoms:**
```
ERROR: yaml.parser.ParserError
```

**Solution:**
```bash
# 1. Validate Docker Compose syntax
docker-compose config

# 2. Check YAML syntax
python tools/validators/validate_yaml.py docker-compose.yml

# 3. Common Docker Compose issues:
#    - Version not specified
#    - Wrong indentation under services
#    - Missing required fields

# 4. Compare with example
cat examples/docker-compose/web-app/docker-compose.yml

# 5. Validate and show result
docker-compose config
# This shows the final parsed config
```

#### Issue 7: "Can't find tool/example"
**Symptoms:**
```
bash: tools/converters/yaml_to_json.py: No such file or directory
```

**Solution:**
```bash
# 1. Check you're in the repository root
pwd
# Should show: /path/to/yaml-json-guide

# 2. List what's available
ls tools/
ls examples/
ls exercises/

# 3. Use absolute paths or navigate to root
cd /path/to/yaml-json-guide
python tools/converters/yaml_to_json.py input.yaml output.json

# 4. Or add to PATH (optional)
export PATH="$PATH:$(pwd)/tools/converters"
export PATH="$PATH:$(pwd)/tools/validators"
```

### Getting Help

#### 1. Check Documentation
```bash
# Start here
cat docs/faq.md

# Common errors
cat docs/common-errors.md

# Misconceptions
cat docs/misconceptions.md

# Interview questions (covers edge cases)
cat docs/interview-prep.md
```

#### 2. Study Examples
```bash
# Find similar use case
ls examples/
cd examples/relevant-category/
cat README.md
```

#### 3. Review Exercise Solutions
```bash
# If stuck on exercise
cd exercises/level/exercise-name/
cat solution.yaml
cat task.md  # Re-read requirements
```

#### 4. Run Validators
```bash
# Let tools tell you what's wrong
python tools/validators/validate_yaml.py your-file.yaml
python tools/validators/check_secrets.py your-file.yaml
```

---

## Quick Reference Card

### File Locations
```
📖 Learning:      docs/getting-started.md
📚 Reference:     docs/quick-reference.md
❓ FAQ:           docs/faq.md
🐛 Errors:        docs/common-errors.md

🎯 Exercises:     exercises/{beginner,intermediate,advanced}/
💡 Examples:      examples/{kubernetes,docker-compose,ci-cd,config-management}/
🔧 Tools:         tools/{converters,validators,generators}/
📋 Templates:     templates/
```

### Essential Commands
```bash
# Validate YAML
python tools/validators/validate_yaml.py file.yaml

# Convert YAML ↔ JSON
python tools/converters/yaml_to_json.py input.yaml output.json
python tools/converters/json_to_yaml.py input.json output.yaml

# Check for secrets
python tools/validators/check_secrets.py config.yaml

# Run exercise test
cd exercises/path/to/exercise
python test.py

# Generate template
python tools/generators/config_template.py --type database --format yaml
```

### Learning Path
```
1. Read:      docs/getting-started.md
2. Practice:  exercises/beginner/ (1-5)
3. Study:     examples/kubernetes/basic-deployment/
4. Practice:  exercises/intermediate/ (6-10)
5. Apply:     Use templates/ for your project
6. Master:    exercises/advanced/ (11-16)
```

### Quick Tips
- ✅ Always use spaces (never tabs)
- ✅ 2 spaces per indentation level
- ✅ Quote strings that look like booleans: `"NO"`, `"yes"`
- ✅ Use `${VARS}` for secrets (never hardcode)
- ✅ Validate before committing
- ✅ Test with `--dry-run` before deploying

---

## Next Steps

Now that you understand how to use this repository, here's what to do next:

### If You're Learning
1. ✅ Start with `docs/getting-started.md`
2. ✅ Complete beginner exercises (1-5)
3. ✅ Study examples while doing intermediate exercises (6-10)
4. ✅ Master advanced exercises (11-16)
5. ✅ Build a real project using templates

### If You're Developing
1. ✅ Copy relevant templates to your project
2. ✅ Set up validation in your CI pipeline
3. ✅ Use tools for conversion and validation
4. ✅ Reference examples for patterns
5. ✅ Scan for secrets before every commit

### If You're Teaching
1. ✅ Review all exercises and solutions
2. ✅ Customize the curriculum for your students
3. ✅ Use examples for live demonstrations
4. ✅ Assign progressive exercises as homework
5. ✅ Use interview-prep.md for assessments

---

## Support and Contribution

### Found an Issue?
1. Check `docs/faq.md` first
2. Review `docs/common-errors.md`
3. Open a GitHub issue if it's a bug

### Want to Contribute?
1. Read `docs/contributing.md`
2. Add your own examples
3. Create new exercises
4. Improve documentation

### Share Your Success!
- Built something cool with these templates?
- Created your own exercise?
- Found a better way to explain something?

Share it with the community!

---

**Happy Learning! 🚀**

Remember: The best way to learn is by doing. Start with the exercises, experiment with the examples, and build real projects with the templates.

**Questions?** Check `docs/faq.md` or `docs/common-errors.md`

**Ready to start?**
```bash
cd exercises/beginner/exercise-01-basic-yaml
cat task.md
```
