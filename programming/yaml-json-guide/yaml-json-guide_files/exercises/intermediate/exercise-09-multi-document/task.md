# Exercise 9: YAML Multi-Document Files

## Objective
Learn to work with multiple YAML documents in a single file.

## Difficulty
Intermediate (⭐⭐☆)

## What You'll Learn
- Multi-document YAML syntax
- Using `---` as document separator
- When to use multi-document files
- Loading all documents

## Task
Create a single YAML file with multiple Kubernetes resources.

### Requirements
Create a file with 3 documents separated by `---`:
1. A Deployment
2. A Service
3. A ConfigMap

### Multi-Document Syntax
```yaml
---
# Document 1
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  key: value
---
# Document 2
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  ports:
  - port: 80
---
# Document 3
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
spec:
  replicas: 2
```

## When to Use Multi-Document

✅ **Good use cases:**
- Kubernetes manifests (multiple resources)
- Related configurations
- Deployment bundles

❌ **Avoid for:**
- Unrelated data
- Large files (hard to maintain)
- When single document is clearer

## Loading Multi-Document Files

### Python
```python
import yaml

with open('multi.yaml') as f:
    docs = list(yaml.safe_load_all(f))

for doc in docs:
    print(doc['kind'])
```

### Kubernetes
```bash
kubectl apply -f multi.yaml  # Applies all documents
```

## Validation
```bash
python test.py
```

## Hints
- Use `---` to separate documents
- Optional `---` at start of first document
- `...` marks end (optional)
- Each document is independent

## Solution
Check `solution.yaml` when ready.
