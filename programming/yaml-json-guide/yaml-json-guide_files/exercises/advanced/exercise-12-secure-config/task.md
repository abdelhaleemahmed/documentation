# Exercise 12: Secure Configuration Management

## Objective
Learn to handle secrets securely in YAML/JSON configurations.

## Difficulty
Advanced (⭐⭐⭐)

## What You'll Learn
- Never hardcode secrets
- Environment variable substitution
- Secret management best practices
- Detecting hardcoded secrets

## Task
Convert an insecure configuration to a secure one.

### Insecure (DO NOT DO THIS)
```yaml
database:
  host: prod.db.example.com
  username: admin
  password: SuperSecret123!  # ❌ NEVER!
  api_key: sk_live_abc123def456  # ❌ NEVER!
```

### Secure (DO THIS)
```yaml
database:
  host: prod.db.example.com
  username: ${DB_USERNAME}
  password: ${DB_PASSWORD}
  api_key: ${API_KEY}
```

## Security Best Practices

### 1. Environment Variables
```yaml
password: ${DB_PASSWORD}  # Read from env at runtime
```

### 2. Secret Management Tools
- **HashiCorp Vault** - Enterprise secrets
- **AWS Secrets Manager** - AWS integration
- **Azure Key Vault** - Azure integration
- **Kubernetes Secrets** - K8s native

### 3. Encrypted Secrets
- **SOPS** (Secrets OPerationS)
- **Sealed Secrets** (Kubernetes)
- **git-crypt** - Transparent encryption

### 4. .env Files (Local Only)
```bash
# .env (NEVER commit to git!)
DB_PASSWORD=secret123
API_KEY=sk_live_abc123
```

Add to `.gitignore`:
```
.env
*.secret
*secret.yaml
```

## Detection
```bash
# Use the secret scanner
python ../../tools/validators/check_secrets.py config.yaml
```

## Task Requirements
1. Convert `insecure.yaml` to `secure.yaml`
2. Replace all hardcoded secrets with ${VAR} placeholders
3. Create example `.env` file
4. Verify with secret scanner

## Solution
Check `secure.yaml` and `.env.example` when ready.
