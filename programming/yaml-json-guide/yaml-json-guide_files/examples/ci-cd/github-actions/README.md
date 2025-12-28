# GitHub Actions CI/CD Example

Complete CI/CD pipeline for Node.js applications with linting, testing, building, and deployment.

## Pipeline Workflow

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│  Lint   │────▶│  Test   │────▶│  Build  │────▶│ Deploy  │
└─────────┘     └─────────┘     └─────────┘     └─────────┘
     ↓               ↓               ↓               ↓
  ESLint      Matrix Testing    npm build      Production
                Node 16/18/20    Artifacts
```

## Features

- **Linting** - ESLint code quality checks
- **Testing** - Matrix testing across Node versions
- **Coverage** - Code coverage upload to Codecov
- **Building** - Production build
- **Artifacts** - Build artifact management
- **Deployment** - Automatic deployment on main branch

## Usage

### 1. Add to Your Repository

```bash
mkdir -p .github/workflows
cp node-ci.yml .github/workflows/
git add .github/workflows/node-ci.yml
git commit -m "Add CI/CD pipeline"
git push
```

### 2. Required package.json Scripts

Ensure your `package.json` has these scripts:

```json
{
  "scripts": {
    "lint": "eslint src/",
    "test": "jest",
    "build": "webpack --mode production"
  }
}
```

### 3. Set Up Secrets

In GitHub repository settings > Secrets and variables > Actions:

- `CODECOV_TOKEN` - For code coverage (optional)
- Add deployment secrets as needed

## Workflow Triggers

### Automatic Triggers

```yaml
on:
  push:
    branches: [main, develop]   # On push to main or develop
  pull_request:
    branches: [main, develop]   # On PR to main or develop
```

### Manual Trigger

Add `workflow_dispatch` to run manually:

```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:  # Enables manual trigger
```

## Jobs Explained

### 1. Lint Job

Checks code quality with ESLint:

```yaml
lint:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v3
    - run: npm ci
    - run: npm run lint
```

### 2. Test Job

Runs tests across multiple Node versions:

```yaml
test:
  strategy:
    matrix:
      node-version: [16, 18, 20]
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v3
    - run: npm ci
    - run: npm test
```

### 3. Build Job

Creates production build:

```yaml
build:
  needs: [lint, test]  # Runs after lint and test
  steps:
    - uses: actions/checkout@v4
    - run: npm run build
    - uses: actions/upload-artifact@v3
```

### 4. Deploy Job

Deploys to production (main branch only):

```yaml
deploy:
  needs: build
  if: github.ref == 'refs/heads/main'
  steps:
    - uses: actions/download-artifact@v3
    - run: ./deploy.sh
```

## Customization

### Change Node Version

```yaml
env:
  NODE_VERSION: '20'  # Change to desired version
```

### Add More Test Versions

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20, 21]  # Add more versions
```

### Add Database Service

```yaml
services:
  postgres:
    image: postgres:15
    env:
      POSTGRES_PASSWORD: postgres
    options: >-
      --health-cmd pg_isready
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5
```

### Add Environment Variables

```yaml
env:
  NODE_ENV: test
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

## Monitoring Workflow

### View Workflow Runs

1. Go to repository on GitHub
2. Click "Actions" tab
3. See all workflow runs

### Check Job Status

```bash
# Using GitHub CLI
gh run list
gh run view <run-id>
gh run watch
```

### Debug Failed Jobs

1. Click on failed job in Actions tab
2. Expand failed step
3. View logs
4. Re-run if needed

## Optimization Tips

### Cache Dependencies

```yaml
- uses: actions/setup-node@v3
  with:
    node-version: 18
    cache: 'npm'  # Caches npm dependencies
```

### Conditional Jobs

```yaml
deploy:
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
```

### Parallel Jobs

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
  test:
    runs-on: ubuntu-latest
  # Both run in parallel
```

### Sequential Jobs

```yaml
build:
  needs: [lint, test]  # Waits for lint and test
```

## Common Patterns

### Pull Request Checks

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  pr-check:
    steps:
      - run: npm run lint
      - run: npm test
```

### Scheduled Runs

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight

jobs:
  nightly-build:
    steps:
      - run: npm run build
```

### Multiple Operating Systems

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
runs-on: ${{ matrix.os }}
```

## Security Best Practices

### 1. Use Pinned Action Versions

```yaml
# ❌ Bad - uses latest
- uses: actions/checkout@v4

# ✅ Better - pinned version
- uses: actions/checkout@v4.1.0

# ✅ Best - pinned to SHA
- uses: actions/checkout@8f4b7f84864484a7bf31766abe9204da3cbe65b3
```

### 2. Limit Token Permissions

```yaml
permissions:
  contents: read
  pull-requests: write
```

### 3. Use Secrets for Sensitive Data

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}  # Never hardcode
```

### 4. Scan for Vulnerabilities

```yaml
- name: Run security audit
  run: npm audit --audit-level=moderate
```

## Troubleshooting

### npm ci Fails

```yaml
# Clear cache and retry
- run: npm cache clean --force
- run: npm ci
```

### Tests Timeout

```yaml
- run: npm test
  timeout-minutes: 10  # Add timeout
```

### Artifact Not Found

```yaml
# Ensure upload happens before download
build:
  steps:
    - uses: actions/upload-artifact@v3
      if: always()  # Upload even if previous steps fail
```

## Cost Optimization

### Free Tier Limits

- 2,000 minutes/month for private repos
- Unlimited for public repos

### Reduce Minutes Usage

1. Cache dependencies
2. Use smaller runners
3. Cancel redundant runs
4. Skip unnecessary jobs

```yaml
- name: Cancel previous runs
  uses: styfle/cancel-workflow-action@0.11.0
```

## Next Steps

- Add Docker build and push
- Implement staging deployment
- Add performance testing
- Set up notification webhooks
- Integrate with Slack/Discord

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Actions Marketplace](https://github.com/marketplace?type=actions)
