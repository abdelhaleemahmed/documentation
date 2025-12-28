# Exercise 13: Kubernetes Manifest Debugging

## Objective
Learn to debug and deploy Kubernetes YAML manifests.

## Difficulty
Advanced (⭐⭐⭐)

## What You'll Learn
- Kubernetes YAML structure
- Common manifest errors
- kubectl validation
- Resource dependencies

## Task
Fix broken Kubernetes manifests and deploy them properly.

### Common Issues
```yaml
# ❌ Wrong indentation
spec:
containers:
  - name: app

# ✓ Correct indentation
spec:
  containers:
    - name: app

# ❌ Missing required fields
apiVersion: v1
kind: Service
metadata:
  name: my-service

# ✓ Complete
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - port: 80
```

## Kubernetes Best Practices

### 1. Resource Limits
```yaml
resources:
  requests:
    memory: "64Mi"
    cpu: "250m"
  limits:
    memory: "128Mi"
    cpu: "500m"
```

### 2. Health Checks
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### 3. Labels and Selectors
```yaml
metadata:
  labels:
    app: myapp
    version: v1
    environment: prod
spec:
  selector:
    matchLabels:
      app: myapp
```

## Validation
```bash
# Dry-run validation
kubectl apply --dry-run=client -f deployment.yaml

# Server-side validation
kubectl apply --dry-run=server -f deployment.yaml

# Detailed diff
kubectl diff -f deployment.yaml
```

## Task Requirements
1. Fix all syntax errors in `broken-deployment.yaml`
2. Add missing required fields
3. Add resource limits and health checks
4. Ensure labels match selectors
5. Pass kubectl validation

## Hints
- Use `kubectl explain deployment.spec` for field documentation
- Check indentation carefully (2 spaces)
- Match labels in metadata and selector
- Always set resource limits

## Solution
Check `deployment.yaml` when ready.
