# Kubernetes Ingress Example

Complete Ingress setup with SSL/TLS, multiple hosts, and path-based routing.

## What is Ingress?

Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. It provides:
- **Host-based routing** - Route by domain name
- **Path-based routing** - Route by URL path
- **SSL/TLS termination** - Handle HTTPS
- **Load balancing** - Distribute traffic
- **Name-based virtual hosting** - Multiple domains on one IP

## Architecture

```
                    Internet
                        │
                    ┌───▼───┐
                    │ Ingress│
                    │ (LB)   │
                    └───┬───┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
myapp.example.com  api.myapp.com  admin.myapp.com
        │               │               │
   ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
   │Frontend │     │ Backend │     │  Admin  │
   │ Service │     │ Service │     │ Service │
   └────┬────┘     └────┬────┘     └────┬────┘
        │               │               │
   ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
   │Frontend │     │ Backend │     │  Admin  │
   │  Pods   │     │  Pods   │     │  Pods   │
   └─────────┘     └─────────┘     └─────────┘
```

## Prerequisites

### 1. Install Ingress Controller

```bash
# Install Nginx Ingress Controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Verify installation
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```

### 2. Configure DNS (Optional for local testing)

Add to `/etc/hosts`:
```
<INGRESS_IP>  myapp.example.com
<INGRESS_IP>  api.myapp.example.com
```

Get Ingress IP:
```bash
kubectl get svc -n ingress-nginx ingress-nginx-controller
```

## Quick Start

```bash
# Deploy the example
kubectl apply -f ingress.yaml

# Check Ingress
kubectl get ingress myapp-ingress

# Test routing
curl http://myapp.example.com
curl http://api.myapp.example.com
```

## Components Explained

### Ingress Resource

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
```

### TLS Configuration

```yaml
spec:
  tls:
  - hosts:
    - myapp.example.com
    - api.myapp.example.com
    secretName: myapp-tls  # TLS certificate
```

### Routing Rules

```yaml
rules:
- host: myapp.example.com
  http:
    paths:
    - path: /
      pathType: Prefix
      backend:
        service:
          name: frontend-service
          port:
            number: 80
```

## Path Types

### Prefix

```yaml
pathType: Prefix
path: /api
# Matches: /api, /api/, /api/users, /api/users/123
```

### Exact

```yaml
pathType: Exact
path: /api
# Matches: /api only (not /api/ or /api/users)
```

### ImplementationSpecific

```yaml
pathType: ImplementationSpecific
path: /api/*
# Behavior depends on Ingress Controller
```

## SSL/TLS Setup

### Option 1: Manual Certificate

```bash
# Create TLS secret from certificate files
kubectl create secret tls myapp-tls \
  --cert=path/to/cert.crt \
  --key=path/to/key.key
```

### Option 2: Cert-Manager (Automatic Let's Encrypt)

```bash
# Install cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml

# Create ClusterIssuer
kubectl apply -f - <<EOF
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your-email@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
EOF
```

Certificate automatically created when Ingress is deployed!

## Advanced Routing

### Path-Based Routing

```yaml
rules:
- host: myapp.example.com
  http:
    paths:
    - path: /
      pathType: Prefix
      backend:
        service:
          name: frontend
          port:
            number: 80
    - path: /api
      pathType: Prefix
      backend:
        service:
          name: backend
          port:
            number: 8080
    - path: /admin
      pathType: Prefix
      backend:
        service:
          name: admin
          port:
            number: 3000
```

### Multiple Hosts

```yaml
rules:
- host: myapp.example.com
  http:
    paths:
    - path: /
      backend:
        service:
          name: frontend
- host: api.myapp.example.com
  http:
    paths:
    - path: /
      backend:
        service:
          name: backend
- host: admin.myapp.example.com
  http:
    paths:
    - path: /
      backend:
        service:
          name: admin
```

## Useful Annotations

### Nginx Ingress Controller

```yaml
annotations:
  # Rewrite target URL
  nginx.ingress.kubernetes.io/rewrite-target: /$2

  # Force SSL redirect
  nginx.ingress.kubernetes.io/ssl-redirect: "true"

  # CORS settings
  nginx.ingress.kubernetes.io/enable-cors: "true"
  nginx.ingress.kubernetes.io/cors-allow-origin: "https://example.com"

  # Rate limiting
  nginx.ingress.kubernetes.io/limit-rps: "100"

  # Whitelist IPs
  nginx.ingress.kubernetes.io/whitelist-source-range: "10.0.0.0/8"

  # Custom timeouts
  nginx.ingress.kubernetes.io/proxy-connect-timeout: "60"
  nginx.ingress.kubernetes.io/proxy-send-timeout: "60"
  nginx.ingress.kubernetes.io/proxy-read-timeout: "60"

  # Basic auth
  nginx.ingress.kubernetes.io/auth-type: basic
  nginx.ingress.kubernetes.io/auth-secret: basic-auth
  nginx.ingress.kubernetes.io/auth-realm: "Authentication Required"
```

## Testing

### Test HTTP

```bash
curl -H "Host: myapp.example.com" http://<INGRESS_IP>/
```

### Test HTTPS

```bash
curl -k https://myapp.example.com/
```

### Test Path Routing

```bash
curl https://myapp.example.com/api/health
```

### Check TLS Certificate

```bash
openssl s_client -connect myapp.example.com:443 -servername myapp.example.com
```

## Monitoring

### View Ingress Details

```bash
kubectl describe ingress myapp-ingress
```

### Check Nginx Ingress Controller Logs

```bash
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx -f
```

### View Configuration

```bash
# Get Nginx config from controller
kubectl exec -n ingress-nginx <nginx-pod> -- cat /etc/nginx/nginx.conf
```

## Troubleshooting

### 404 Not Found

```bash
# Check backend service exists
kubectl get svc frontend-service

# Check service selector matches pods
kubectl get pods -l app=frontend

# Check Ingress rules
kubectl describe ingress myapp-ingress
```

### 502 Bad Gateway

```bash
# Backend pods not ready
kubectl get pods -l app=backend

# Check pod logs
kubectl logs <backend-pod>

# Verify service endpoints
kubectl get endpoints backend-service
```

### 503 Service Unavailable

```bash
# No backend pods available
kubectl get pods -l app=backend

# Scale deployment
kubectl scale deployment backend --replicas=2
```

### SSL Certificate Issues

```bash
# Check cert-manager logs
kubectl logs -n cert-manager -l app=cert-manager

# Check certificate status
kubectl get certificate
kubectl describe certificate myapp-tls

# Check secret exists
kubectl get secret myapp-tls
```

## Best Practices

1. **Use TLS** - Always enable SSL/TLS for production
2. **Use cert-manager** - Automate certificate management
3. **Set resource limits** - Prevent resource exhaustion
4. **Enable rate limiting** - Protect against abuse
5. **Use health checks** - Ensure backend availability
6. **Monitor metrics** - Track request rates and errors
7. **Whitelist IPs** - For admin/sensitive endpoints

## Comparison with LoadBalancer

| Feature | Ingress | LoadBalancer Service |
|---------|---------|---------------------|
| **Cost** | One LB for all services | One LB per service |
| **SSL/TLS** | Built-in support | Manual configuration |
| **Host routing** | Yes | No |
| **Path routing** | Yes | No |
| **Annotations** | Rich feature set | Limited |
| **Use case** | Multiple services | Single service |

## When to Use Ingress

✅ **Use Ingress for:**
- Multiple services needing external access
- Host-based routing (multi-tenant)
- Path-based routing
- SSL/TLS termination
- Cost optimization (one LB vs many)

❌ **Don't use Ingress for:**
- Non-HTTP/HTTPS protocols (use LoadBalancer)
- Very simple single-service exposures (can use LoadBalancer)

## References

- [Kubernetes Ingress Documentation](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Nginx Ingress Controller](https://kubernetes.github.io/ingress-nginx/)
- [Cert-Manager Documentation](https://cert-manager.io/docs/)
