# Jenkins Pipeline Configuration Example

Complete Jenkins pipeline for Node.js applications using Jenkinsfile and declarative pipeline syntax.

## Features

- Declarative pipeline syntax
- Parallel test execution
- Manual deployment approval
- Code coverage reporting
- Artifact archiving
- Security scanning
- Branch-specific deployments

## Setup

### Prerequisites

1. **Jenkins Plugins Required:**
   - Pipeline
   - NodeJS Plugin
   - JUnit Plugin
   - HTML Publisher Plugin
   - Git Plugin

2. **Configure NodeJS:**
   - Manage Jenkins > Global Tool Configuration
   - Add NodeJS installation named "Node 18"
   - Set version to 18.x

### Add to Your Repository

```bash
cp Jenkinsfile Jenkinsfile
git add Jenkinsfile
git commit -m "Add Jenkins pipeline configuration"
git push
```

### Create Pipeline Job

1. Go to Jenkins > New Item
2. Enter name and select "Pipeline"
3. Under "Pipeline" section:
   - Definition: Pipeline script from SCM
   - SCM: Git
   - Repository URL: your-repo-url
   - Script Path: Jenkinsfile
4. Save

## Pipeline Flow

```
┌───────────┐
│ Checkout  │ - Clone repository
└─────┬─────┘
      │
┌─────▼─────┐
│  Install  │ - npm ci
└─────┬─────┘
      │
┌─────▼─────┐
│   Lint    │ - ESLint
└─────┬─────┘
      │
┌─────┴──────────┐
│                │
▼                ▼
┌──────────┐  ┌──────────────┐
│   Unit   │  │ Integration  │ - Parallel
└────┬─────┘  └──────┬───────┘
     │               │
     └───────┬───────┘
             │
      ┌──────▼────────┐
      │   Security    │ - npm audit
      └──────┬────────┘
             │
      ┌──────▼────────┐
      │     Build     │ - Production build
      └──────┬────────┘
             │
        ┌────┴────┐
        │         │
        ▼         ▼
  ┌──────────┐ ┌─────────────┐
  │ Staging  │ │ Production  │ - Manual approval
  └──────────┘ └─────────────┘
```

## Pipeline Sections Explained

### Agent

```groovy
agent any  // Run on any available agent
```

Or specify specific agent:
```groovy
agent {
    label 'linux'
}
```

### Options

```groovy
options {
    buildDiscarder(logRotator(numToKeepStr: '10'))  // Keep last 10 builds
    disableConcurrentBuilds()  // Prevent concurrent builds
    timeout(time: 1, unit: 'HOURS')  // 1 hour timeout
    timestamps()  // Add timestamps to console output
}
```

### Environment

```groovy
environment {
    NODE_VERSION = '18'
    CI = 'true'
}
```

### Stages

Each stage represents a phase:

```groovy
stage('Test') {
    steps {
        sh 'npm test'
    }
}
```

### Parallel Execution

```groovy
stage('Test') {
    parallel {
        stage('Unit Tests') {
            steps {
                sh 'npm run test:unit'
            }
        }
        stage('Integration Tests') {
            steps {
                sh 'npm run test:integration'
            }
        }
    }
}
```

### Conditional Stages

```groovy
stage('Deploy') {
    when {
        branch 'main'  // Only on main branch
    }
    steps {
        sh 'npm run deploy'
    }
}
```

### Manual Approval

```groovy
steps {
    input message: 'Deploy to production?',
          ok: 'Deploy',
          submitter: 'admin'  // Only admin can approve
    sh 'npm run deploy'
}
```

## Required package.json Scripts

```json
{
  "scripts": {
    "lint": "eslint src/",
    "test:unit": "jest --reporters=default --reporters=jest-junit",
    "test:integration": "jest --config jest.integration.config.js",
    "build": "webpack --mode production",
    "deploy:staging": "./deploy-staging.sh",
    "deploy:production": "./deploy-production.sh"
  },
  "devDependencies": {
    "jest-junit": "^15.0.0"
  },
  "jest-junit": {
    "outputDirectory": "test-results",
    "outputName": "junit.xml"
  }
}
```

## Advanced Configuration

### Using Docker Agent

```groovy
agent {
    docker {
        image 'node:18-alpine'
        args '-v $HOME/.npm:/.npm'
    }
}
```

### Multiple Node Versions

```groovy
stage('Test') {
    matrix {
        axes {
            axis {
                name 'NODE_VERSION'
                values '16', '18', '20'
            }
        }
        stages {
            stage('Test') {
                steps {
                    nodejs(nodeJSInstallationName: "Node ${NODE_VERSION}") {
                        sh 'npm test'
                    }
                }
            }
        }
    }
}
```

### Environment-Specific Credentials

```groovy
environment {
    STAGING_CREDS = credentials('staging-credentials-id')
    PROD_CREDS = credentials('production-credentials-id')
}

stage('Deploy') {
    steps {
        sh 'deploy.sh --key $PROD_CREDS'
    }
}
```

### Post Actions

```groovy
post {
    always {
        cleanWs()  // Clean workspace
    }
    success {
        emailext(
            subject: "Build Successful: ${env.JOB_NAME}",
            body: "Build ${env.BUILD_NUMBER} succeeded",
            to: "team@example.com"
        )
    }
    failure {
        emailext(
            subject: "Build Failed: ${env.JOB_NAME}",
            body: "Build ${env.BUILD_NUMBER} failed",
            to: "team@example.com"
        )
    }
}
```

## Monitoring

### Blue Ocean UI

1. Install Blue Ocean plugin
2. Access at: `/blue`
3. Visual pipeline view

### Build Artifacts

Archived artifacts accessible from build page:
- Click on build number
- "Build Artifacts" link

### Test Results

JUnit test results automatically parsed and displayed:
- Test trend graph
- Failed test details

### Code Coverage

HTML reports published using HTML Publisher plugin:
- Coverage report link on build page

## Troubleshooting

### Node Not Found

```groovy
// Ensure NodeJS plugin is configured
nodejs(nodeJSInstallationName: 'Node 18') {
    sh 'node --version'
}
```

### Permission Denied

```groovy
// Make scripts executable
sh 'chmod +x deploy.sh'
sh './deploy.sh'
```

### Workspace Issues

```groovy
// Clean workspace before build
stage('Checkout') {
    steps {
        cleanWs()
        checkout scm
    }
}
```

## Best Practices

1. **Use declarative syntax** - Easier to read and maintain
2. **Parallel stages** - Speed up builds
3. **Manual approval** - For production deployments
4. **Archive artifacts** - Keep build outputs
5. **Clean workspace** - Prevent conflicts
6. **Timeout** - Prevent hanging builds
7. **Notifications** - Alert on failures

## Security

### Use Credentials

```groovy
withCredentials([string(credentialsId: 'api-key', variable: 'API_KEY')]) {
    sh 'curl -H "Authorization: $API_KEY" api.example.com'
}
```

### SSH Credentials

```groovy
sshagent(['ssh-credentials-id']) {
    sh 'ssh user@server "deploy.sh"'
}
```

### Secrets Scanning

```groovy
stage('Security') {
    steps {
        sh 'npm audit'
        sh 'git secrets --scan'  // Check for committed secrets
    }
}
```

## References

- [Jenkins Pipeline Documentation](https://www.jenkins.io/doc/book/pipeline/)
- [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [NodeJS Plugin](https://plugins.jenkins.io/nodejs/)
- [Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)
