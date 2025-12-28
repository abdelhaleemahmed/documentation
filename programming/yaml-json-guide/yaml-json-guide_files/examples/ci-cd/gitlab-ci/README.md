# GitLab CI/CD Configuration Example

Complete GitLab CI/CD pipeline for Node.js applications with testing, building, and deployment.

## Features

- Multi-stage pipeline (install, lint, test, build, deploy)
- Dependency caching for faster builds
- Parallel test execution (unit & integration)
- Code coverage reporting
- Security scanning
- Staging and production deployments
- GitLab Pages for documentation

## Setup

### 1. Add to Your Repository

```bash
cp .gitlab-ci.yml .gitlab-ci.yml
git add .gitlab-ci.yml
git commit -m "Add GitLab CI/CD configuration"
git push
```

GitLab automatically detects `.gitlab-ci.yml` and starts running pipelines.

### 2. Configure CI/CD Variables

In GitLab: Settings > CI/CD > Variables

Add these variables:
- `STAGING_DEPLOY_KEY` - SSH key for staging
- `PRODUCTION_DEPLOY_KEY` - SSH key for production
- `CODECOV_TOKEN` - Code coverage token (optional)

## Pipeline Stages

```
┌──────────┐
│ Install  │ - Install dependencies
└────┬─────┘
     │
┌────┴─────────────────┐
│                      │
▼                      ▼
┌──────┐         ┌──────────┐
│ Lint │         │   Test   │ - Unit & Integration
└──┬───┘         └────┬─────┘
   │                  │
   └────────┬─────────┘
            ▼
       ┌────────┐
       │ Build  │ - Production build
       └───┬────┘
           │
      ┌────┴────┐
      ▼         ▼
  ┌─────────┐ ┌────────────┐
  │ Staging │ │ Production │ - Manual deployment
  └─────────┘ └────────────┘
```

## Jobs Explained

### Install
- Caches npm dependencies
- Runs `npm ci` for consistent installs
- Creates artifacts for subsequent jobs

### Lint
- Runs ESLint for code quality
- Uses cached dependencies

### Test (Unit & Integration)
- Parallel execution
- Unit tests with coverage reporting
- Integration tests with PostgreSQL service
- JUnit report generation

### Build
- Creates production bundle
- Only runs on main/develop branches
- Artifacts expire in 1 week

### Security
- Runs `npm audit`
- Allowed to fail (warnings only)

### Deploy (Staging & Production)
- Manual trigger required
- Environment-specific deployments
- Tracks deployment history

## Configuration Details

### Caching Strategy

```yaml
.node_cache: &node_cache
  cache:
    key:
      files:
        - package-lock.json  # Cache based on lockfile
    paths:
      - .npm
      - node_modules
    policy: pull  # Most jobs only pull
```

### Job Templates

```yaml
.node_job:
  image: node:${NODE_VERSION}-alpine
  before_script:
    - node --version
```

Reused across all Node.js jobs.

### Services

```yaml
services:
  - postgres:15-alpine  # Database for integration tests

variables:
  POSTGRES_DB: testdb
  DATABASE_URL: "postgresql://user:pass@postgres:5432/testdb"
```

## Required package.json Scripts

```json
{
  "scripts": {
    "lint": "eslint src/",
    "test:unit": "jest --coverage",
    "test:integration": "jest --config jest.integration.config.js",
    "build": "webpack --mode production",
    "deploy:staging": "./deploy-staging.sh",
    "deploy:production": "./deploy-production.sh",
    "docs:build": "typedoc src/ --out docs"
  }
}
```

## Advanced Features

### Matrix Builds

```yaml
test:
  parallel:
    matrix:
      - NODE_VERSION: ["16", "18", "20"]
  image: node:${NODE_VERSION}-alpine
  script:
    - npm test
```

### Conditional Jobs

```yaml
deploy:production:
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
    - when: never
```

### Merge Request Pipelines

```yaml
test:
  script:
    - npm test
  only:
    - merge_requests
    - main
```

### Docker Build

```yaml
docker:build:
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA
```

## Monitoring

### View Pipeline

1. Go to CI/CD > Pipelines
2. Click on pipeline to see job details
3. View logs for each job

### Code Coverage

GitLab automatically parses coverage from test output:

```yaml
coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
```

Shows coverage percentage in merge requests.

### Artifacts

Download build artifacts from job page or use GitLab API.

## Troubleshooting

### Cache Not Working

```yaml
# Clear cache and rebuild
# In GitLab UI: CI/CD > Pipelines > Clear Runner Caches
```

### Job Timeout

```yaml
test:
  script:
    - npm test
  timeout: 2h  # Increase from default 1h
```

### Out of Memory

```yaml
variables:
  NODE_OPTIONS: "--max-old-space-size=4096"
```

### Failed Integration Tests

```yaml
services:
  - postgres:15-alpine

# Check service is ready
script:
  - until pg_isready -h postgres; do sleep 1; done
  - npm run test:integration
```

## Best Practices

1. **Use caching** - Speeds up builds significantly
2. **Parallel jobs** - Run tests concurrently
3. **Manual deploys** - Require approval for production
4. **Artifacts** - Keep build outputs and test reports
5. **Environment URLs** - Track deployment environments

## Cost Optimization

### Free Tier
- 400 CI/CD minutes/month
- Unlimited for public projects

### Reduce Minutes
1. Cache dependencies effectively
2. Use smaller Docker images (`alpine`)
3. Skip unnecessary jobs:

```yaml
test:
  rules:
    - if: '$CI_MERGE_REQUEST_TITLE =~ /^WIP:/'
      when: never  # Skip WIP merge requests
```

## GitLab Pages

Deploy documentation automatically:

```yaml
pages:
  script:
    - npm run docs:build
    - mv docs public
  artifacts:
    paths:
      - public
```

Access at: `https://username.gitlab.io/project`

## References

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [.gitlab-ci.yml Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)
