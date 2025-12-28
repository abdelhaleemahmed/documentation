# Configuration Templates

Production-ready YAML templates for common use cases.

## Available Templates

### 1. Docker Compose (`docker-compose.template.yml`)

Complete Docker Compose stack with:
- Frontend web server (Nginx)
- Backend API (Node.js)
- PostgreSQL database
- Redis cache
- Health checks
- Networking configuration
- Volume management

**Usage:**
```bash
cp docker-compose.template.yml docker-compose.yml
# Edit docker-compose.yml and create .env file
docker-compose up -d
```

### 2. GitHub Actions (`github-actions.template.yml`)

Complete CI/CD pipeline with:
- Linting and code quality checks
- Multi-version testing
- Build and artifact management
- Security scanning
- Staging and production deployment
- Automatic releases

**Usage:**
```bash
mkdir -p .github/workflows
cp github-actions.template.yml .github/workflows/ci-cd.yml
# Configure secrets in GitHub repository settings
git add .github/workflows/ci-cd.yml
git commit -m "Add CI/CD pipeline"
git push
```

### 3. Kubernetes Deployment (`kubernetes-deployment.template.yml`)

Production-ready Kubernetes manifests:
- Namespace
- ConfigMap for configuration
- Secret for sensitive data
- Deployment with 3 replicas
- Service (ClusterIP)
- Horizontal Pod Autoscaler
- Health checks (liveness, readiness, startup)
- Resource limits and requests
- Security contexts
- Affinity rules

**Usage:**
```bash
cp kubernetes-deployment.template.yml myapp-deployment.yml
# Edit myapp-deployment.yml with your application details
kubectl apply -f myapp-deployment.yml
kubectl get all -n myapp
```

### 4. Multi-Environment Config (`config-multi-env.template.yml`)

Single configuration file with environment-specific overrides:
- Development settings
- Staging configuration
- Production settings
- Testing environment
- Uses YAML anchors for DRY configuration
- Environment variable substitution

**Usage:**
```bash
cp config-multi-env.template.yml config.yml
# Set environment variables
export DB_PASSWORD=your_password
export APP_ENV=production
# Load in your application
python app.py --config config.yml --env production
```

## Template Customization

### Step 1: Copy Template
```bash
cp templates/[template-name].template.yml your-config.yml
```

### Step 2: Replace Placeholders

Common placeholders to replace:
- `myapp` - Your application name
- `${VARIABLE}` - Environment variables
- `localhost` - Your host/domain
- Port numbers - Your specific ports
- Image names - Your Docker images

### Step 3: Set Environment Variables

Create `.env` file (DO NOT commit to git):
```bash
# .env
APP_NAME=myapp
NODE_ENV=production
DB_USER=appuser
DB_PASSWORD=securepassword
JWT_SECRET=your-secret-key
```

### Step 4: Validate

```bash
# Validate YAML syntax
yamllint your-config.yml

# Validate with tool
python ../tools/validators/validate_yaml.py your-config.yml

# Check for secrets
python ../tools/validators/check_secrets.py your-config.yml
```

## Best Practices

### Security
- ✅ Use environment variables for secrets
- ✅ Never commit passwords or API keys
- ✅ Use `.env` files (add to `.gitignore`)
- ✅ Enable SSL/TLS in production
- ✅ Set proper resource limits
- ✅ Run containers as non-root user

### Configuration Management
- ✅ Use YAML anchors for shared config
- ✅ Separate dev/staging/prod configs
- ✅ Document all configuration options
- ✅ Validate before deploying
- ✅ Use version control for configs
- ✅ Keep templates updated

### Docker Compose
- ✅ Use specific image tags (not `latest`)
- ✅ Set resource limits
- ✅ Configure health checks
- ✅ Use named volumes for persistence
- ✅ Separate frontend/backend networks
- ✅ Enable restart policies

### Kubernetes
- ✅ Use namespaces for isolation
- ✅ Set resource requests and limits
- ✅ Configure health checks
- ✅ Use HorizontalPodAutoscaler
- ✅ Apply security contexts
- ✅ Use ConfigMaps and Secrets
- ✅ Enable pod anti-affinity

### CI/CD
- ✅ Run tests before deployment
- ✅ Use matrix testing for multiple versions
- ✅ Scan for security vulnerabilities
- ✅ Deploy to staging before production
- ✅ Use environment protection rules
- ✅ Keep artifacts for rollback

## Environment Variables

### Docker Compose
```bash
export APP_NAME=myapp
export NODE_ENV=production
export DB_USER=appuser
export DB_PASSWORD=securepassword
export DB_NAME=myapp
export REDIS_PASSWORD=redis-password
```

### Kubernetes
```bash
# Create secrets
kubectl create secret generic myapp-secret \
  --from-literal=database-password=yourpassword \
  --from-literal=jwt-secret=yoursecret \
  --from-literal=api-key=yourapikey \
  -n myapp
```

### GitHub Actions
Set in repository Settings > Secrets and variables > Actions:
- `CODECOV_TOKEN`
- `SNYK_TOKEN`
- `STAGING_DEPLOY_KEY`
- `PRODUCTION_DEPLOY_KEY`
- `DEPLOY_HOST`

## Troubleshooting

### Docker Compose Issues

```bash
# View logs
docker-compose logs -f

# Restart services
docker-compose restart

# Rebuild images
docker-compose up -d --build

# Check health
docker-compose ps
```

### Kubernetes Issues

```bash
# Check pod status
kubectl get pods -n myapp

# View logs
kubectl logs -n myapp -l app=myapp

# Describe deployment
kubectl describe deployment myapp-deployment -n myapp

# Check events
kubectl get events -n myapp --sort-by='.lastTimestamp'
```

### GitHub Actions Issues

- Check workflow file syntax in GitHub UI
- Review job logs in Actions tab
- Verify secrets are set correctly
- Check branch protection rules

## Additional Resources

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [YAML Specification](https://yaml.org/spec/)

## Contributing

Found an issue or want to improve a template?
1. Test your changes thoroughly
2. Update documentation
3. Submit a pull request

See [../docs/contributing.md](../docs/contributing.md) for details.
