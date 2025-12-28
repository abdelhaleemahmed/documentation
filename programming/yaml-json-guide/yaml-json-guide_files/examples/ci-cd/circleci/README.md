# CircleCI Configuration Example

Complete CircleCI pipeline for Node.js applications with linting, testing, building, and deployment.

## Features

- Dependency caching for faster builds
- Parallel job execution
- Workspace persistence
- Code coverage reporting
- Staging and production deployments
- Manual approval for production

## Setup

### 1. Add to Your Repository

```bash
mkdir -p .circleci
cp config.yml .circleci/config.yml
git add .circleci/config.yml
git commit -m "Add CircleCI configuration"
git push
```

### 2. Enable Project in CircleCI

1. Go to [CircleCI](https://circleci.com/)
2. Sign in with GitHub
3. Click "Set Up Project"
4. Select your repository
5. CircleCI will detect `.circleci/config.yml`

### 3. Add Environment Variables

In Project Settings > Environment Variables:
- `CODECOV_TOKEN` - For code coverage
- Add deployment credentials as needed

## Pipeline Workflow

```
┌─────────┐
│ Install │
└────┬────┘
     │
     ├──────┬──────┐
     ▼      ▼      ▼
  ┌──────┐ ┌──────┐
  │ Lint │ │ Test │
  └──┬───┘ └──┬───┘
     │        │
     └────┬───┘
          ▼
     ┌────────┐
     │ Build  │
     └───┬────┘
         │
    ┌────┴─────┐
    ▼          ▼
┌─────────┐ ┌────────────┐
│ Staging │ │ Production │
└─────────┘ └────────────┘
```

## Jobs Explained

### Install Job
- Checks out code
- Restores dependency cache
- Installs dependencies with `npm ci`
- Saves cache for future builds
- Persists workspace for other jobs

### Lint Job
- Attaches workspace from install
- Runs ESLint for code quality

### Test Job
- Runs test suite
- Generates coverage report
- Uploads to Codecov
- Stores test results and artifacts

### Build Job
- Creates production build
- Persists build artifacts

### Deploy Jobs
- Deploys to staging (develop branch)
- Deploys to production (main branch, with approval)

## Configuration Details

### Orbs Used

```yaml
orbs:
  node: circleci/node@5.1.0    # Node.js helper commands
  codecov: codecov/codecov@3.2.4  # Code coverage upload
```

### Caching

```yaml
restore_cache:
  keys:
    - v1-dependencies-{{ checksum "package-lock.json" }}
    - v1-dependencies-  # Fallback
```

### Workspace Persistence

```yaml
persist_to_workspace:
  root: ~/project
  paths:
    - .  # Persist everything
```

## Required package.json Scripts

```json
{
  "scripts": {
    "lint": "eslint src/",
    "test": "jest",
    "test:coverage": "jest --coverage",
    "build": "webpack --mode production",
    "deploy:staging": "./deploy-staging.sh",
    "deploy:production": "./deploy-production.sh"
  }
}
```

## Customization

### Add Database Service

```yaml
executors:
  node-with-postgres:
    docker:
      - image: cimg/node:18.18
      - image: cimg/postgres:15.3
        environment:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: testdb
```

### Change Node Version

```yaml
orbs:
  node: circleci/node@5.1.0

executors:
  node-executor:
    docker:
      - image: cimg/node:20.9  # Change version here
```

### Add Matrix Testing

```yaml
jobs:
  test:
    parameters:
      node-version:
        type: string
    docker:
      - image: cimg/node:<< parameters.node-version >>
    steps:
      - checkout
      - run: npm test

workflows:
  test-matrix:
    jobs:
      - test:
          matrix:
            parameters:
              node-version: ["16.20", "18.18", "20.9"]
```

## Monitoring

### View Pipeline

1. Go to CircleCI dashboard
2. Select your project
3. View pipeline runs and job details

### Rerun Failed Jobs

```bash
# Click "Rerun" in CircleCI UI
# Or use CLI:
circleci run-job <job-name>
```

## Best Practices

1. **Cache dependencies** - Speeds up builds
2. **Use workspaces** - Share data between jobs
3. **Parallel execution** - Run jobs concurrently
4. **Manual approval** - For production deployments
5. **Store artifacts** - Keep test results and coverage

## Troubleshooting

### Cache Not Working

```yaml
# Bump cache version
restore_cache:
  keys:
    - v2-dependencies-{{ checksum "package-lock.json" }}
```

### Job Timeout

```yaml
jobs:
  test:
    steps:
      - run:
          name: Run tests
          command: npm test
          no_output_timeout: 20m  # Increase timeout
```

### Out of Memory

```yaml
executors:
  node-executor:
    docker:
      - image: cimg/node:18.18
    resource_class: large  # Use larger instance
```

## Cost Optimization

### Free Tier
- 30,000 credits/month
- ~1,500 build minutes

### Reduce Credit Usage
1. Cache dependencies effectively
2. Use smaller Docker images
3. Run jobs in parallel
4. Skip unnecessary jobs

```yaml
workflows:
  build-test-deploy:
    jobs:
      - test:
          filters:
            branches:
              ignore: /feature-.*/  # Skip feature branches
```

## References

- [CircleCI Documentation](https://circleci.com/docs/)
- [Configuration Reference](https://circleci.com/docs/configuration-reference/)
- [Orb Registry](https://circleci.com/developer/orbs)
