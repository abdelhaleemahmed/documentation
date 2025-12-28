# Kubernetes Basic Deployment Example

Complete Kubernetes deployment with Deployment, Service, ConfigMap, and Secret.

## Files

- `deployment.yaml` - Nginx deployment with 3 replicas
- `service.yaml` - LoadBalancer service
- `configmap.yaml` - Configuration files
- `secret.yaml` - Sensitive data (base64 encoded)

## What This Example Demonstrates

1. **Deployment** - Running multiple replicas of an application
2. **Service** - Exposing the application
3. **ConfigMap** - Storing configuration data
4. **Secret** - Storing sensitive information
5. **Resource Limits** - CPU and memory constraints
6. **Labels** - Organizing and selecting resources

## Prerequisites

- Kubernetes cluster (minikube, kind, or cloud provider)
- kubectl configured

## Quick Start

```bash
# Apply all manifests
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml

# Or apply all at once
kubectl apply -f .

# Check status
kubectl get all

# View pods
kubectl get pods -l app=nginx

# View service
kubectl get service nginx-service

# Check logs
kubectl logs -l app=nginx

# Get service URL (for LoadBalancer)
kubectl get service nginx-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

## Step-by-Step Deployment

### 1. Create the Deployment

```bash
kubectl apply -f deployment.yaml
```

This creates 3 nginx pods with resource limits.

### 2. Create the Service

```bash
kubectl apply -f service.yaml
```

This exposes the deployment via a LoadBalancer.

### 3. Create ConfigMap

```bash
kubectl apply -f configmap.yaml
```

This stores non-sensitive configuration data.

### 4. Create Secret

```bash
kubectl apply -f secret.yaml
```

This stores sensitive data (username/password).

## Verification

```bash
# Check deployment status
kubectl rollout status deployment/nginx-deployment

# Describe deployment
kubectl describe deployment nginx-deployment

# Check pods are running
kubectl get pods -l app=nginx -o wide

# Test the service
kubectl port-forward service/nginx-service 8080:80
# Then visit http://localhost:8080
```

## Updating the Deployment

### Update Image

```bash
kubectl set image deployment/nginx-deployment nginx=nginx:1.22
kubectl rollout status deployment/nginx-deployment
```

### Scale Replicas

```bash
kubectl scale deployment nginx-deployment --replicas=5
kubectl get pods -l app=nginx
```

### Update ConfigMap

```bash
# Edit configmap
kubectl edit configmap nginx-config

# Restart pods to pick up changes
kubectl rollout restart deployment/nginx-deployment
```

## Cleanup

```bash
# Delete all resources
kubectl delete -f .

# Or delete individually
kubectl delete deployment nginx-deployment
kubectl delete service nginx-service
kubectl delete configmap nginx-config
kubectl delete secret nginx-secret
```

## Common Issues

### Pods Not Starting

```bash
# Check pod status
kubectl get pods -l app=nginx

# View pod events
kubectl describe pod <pod-name>

# Check logs
kubectl logs <pod-name>
```

### Service Not Accessible

```bash
# Check service endpoints
kubectl get endpoints nginx-service

# Verify service selector matches pod labels
kubectl get pods -l app=nginx --show-labels
```

### ConfigMap Not Mounted

```bash
# Verify configmap exists
kubectl get configmap nginx-config

# Check pod volume mounts
kubectl describe pod <pod-name> | grep -A5 Mounts
```

## Key Concepts

### Deployment
- Manages ReplicaSets and Pods
- Handles rolling updates
- Ensures desired state

### Service
- Provides stable endpoint
- Load balances across pods
- Types: ClusterIP, NodePort, LoadBalancer

### ConfigMap
- Stores non-sensitive configuration
- Can be mounted as files or environment variables
- Plain text storage

### Secret
- Stores sensitive data
- Base64 encoded (not encrypted!)
- Should be used with encryption at rest

### Resource Limits
- **requests** - Minimum guaranteed resources
- **limits** - Maximum allowed resources
- Important for cluster scheduling

## Best Practices

1. **Always set resource requests and limits**
2. **Use specific image tags** (not `latest`)
3. **Store configuration in ConfigMaps**
4. **Store secrets in Secrets** (with encryption at rest)
5. **Use labels** for organization and selection
6. **Add health checks** (liveness, readiness)
7. **Use namespaces** for isolation

## Next Steps

- Try the statefulset example
- Explore ingress configuration
- Learn about persistent volumes
- Set up horizontal pod autoscaling

## References

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
