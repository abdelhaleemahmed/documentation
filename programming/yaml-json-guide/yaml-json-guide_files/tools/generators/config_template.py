#!/usr/bin/env python3
"""
Configuration Template Generator

Generates configuration file templates with common patterns and best practices.

Usage:
    python config_template.py --type <type> --format <yaml|json> [--output file]

Examples:
    python config_template.py --type database --format yaml
    python config_template.py --type api --format json --output config.json
    python config_template.py --type kubernetes --format yaml --output deployment.yaml
"""

import argparse
import json
import sys
from typing import Dict, Any

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Run: pip install PyYAML", file=sys.stderr)
    sys.exit(1)


TEMPLATES = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'database': 'myapp',
        'username': '${DB_USER}',
        'password': '${DB_PASSWORD}',
        'pool': {
            'min': 2,
            'max': 10,
            'idle_timeout': 30
        },
        'options': {
            'ssl': True,
            'connect_timeout': 10,
            'retry_attempts': 3
        }
    },
    'api': {
        'server': {
            'host': '0.0.0.0',
            'port': 8080,
            'debug': False
        },
        'cors': {
            'enabled': True,
            'origins': ['*'],
            'methods': ['GET', 'POST', 'PUT', 'DELETE']
        },
        'rate_limit': {
            'enabled': True,
            'requests_per_minute': 60
        },
        'logging': {
            'level': 'INFO',
            'format': 'json',
            'output': 'stdout'
        }
    },
    'application': {
        'app': {
            'name': 'myapp',
            'version': '1.0.0',
            'environment': 'development'
        },
        'features': {
            'authentication': True,
            'caching': True,
            'analytics': False
        },
        'settings': {
            'debug': True,
            'timeout': 30,
            'max_upload_size': '10MB'
        }
    },
    'kubernetes': {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {
            'name': 'myapp',
            'labels': {
                'app': 'myapp'
            }
        },
        'spec': {
            'replicas': 3,
            'selector': {
                'matchLabels': {
                    'app': 'myapp'
                }
            },
            'template': {
                'metadata': {
                    'labels': {
                        'app': 'myapp'
                    }
                },
                'spec': {
                    'containers': [{
                        'name': 'myapp',
                        'image': 'myapp:latest',
                        'ports': [{
                            'containerPort': 8080
                        }],
                        'env': [{
                            'name': 'ENV',
                            'value': 'production'
                        }],
                        'resources': {
                            'requests': {
                                'memory': '128Mi',
                                'cpu': '100m'
                            },
                            'limits': {
                                'memory': '256Mi',
                                'cpu': '200m'
                            }
                        }
                    }]
                }
            }
        }
    },
    'docker-compose': {
        'version': '3.8',
        'services': {
            'app': {
                'image': 'myapp:latest',
                'ports': ['8080:8080'],
                'environment': {
                    'ENV': 'production'
                },
                'volumes': ['./app:/app'],
                'depends_on': ['db']
            },
            'db': {
                'image': 'postgres:15',
                'environment': {
                    'POSTGRES_PASSWORD': '${DB_PASSWORD}',
                    'POSTGRES_DB': 'myapp'
                },
                'volumes': ['postgres_data:/var/lib/postgresql/data']
            }
        },
        'volumes': {
            'postgres_data': {}
        }
    },
    'ci-cd': {
        'name': 'CI/CD Pipeline',
        'on': {
            'push': {
                'branches': ['main']
            },
            'pull_request': {
                'branches': ['main']
            }
        },
        'jobs': {
            'test': {
                'runs-on': 'ubuntu-latest',
                'steps': [
                    {'uses': 'actions/checkout@v4'},
                    {'name': 'Run tests', 'run': 'npm test'}
                ]
            },
            'deploy': {
                'runs-on': 'ubuntu-latest',
                'needs': 'test',
                'if': "github.ref == 'refs/heads/main'",
                'steps': [
                    {'uses': 'actions/checkout@v4'},
                    {'name': 'Deploy', 'run': './deploy.sh'}
                ]
            }
        }
    }
}


def generate_template(template_type: str, output_format: str) -> str:
    """
    Generate a configuration template.

    Args:
        template_type: Type of template to generate
        output_format: Output format (yaml or json)

    Returns:
        Template as string
    """
    if template_type not in TEMPLATES:
        available = ', '.join(TEMPLATES.keys())
        raise ValueError(f"Unknown template type: {template_type}. Available: {available}")

    data = TEMPLATES[template_type]

    if output_format == 'yaml':
        return yaml.dump(data, default_flow_style=False, sort_keys=False, indent=2)
    elif output_format == 'json':
        return json.dumps(data, indent=2, ensure_ascii=False)
    else:
        raise ValueError(f"Unknown format: {output_format}. Use 'yaml' or 'json'")


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate configuration file templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Available template types:
  {', '.join(TEMPLATES.keys())}

Examples:
  %(prog)s --type database --format yaml
  %(prog)s --type api --format json --output config.json
  %(prog)s --type kubernetes --format yaml --output deployment.yaml
  %(prog)s --list
        """
    )
    parser.add_argument('--type', choices=list(TEMPLATES.keys()), help='Template type')
    parser.add_argument('--format', choices=['yaml', 'json'], default='yaml', help='Output format')
    parser.add_argument('--output', help='Output file (default: stdout)')
    parser.add_argument('--list', action='store_true', help='List available templates')

    args = parser.parse_args()

    # List templates
    if args.list:
        print("Available templates:")
        for name in TEMPLATES.keys():
            print(f"  - {name}")
        return 0

    # Validate arguments
    if not args.type:
        parser.error("--type is required (or use --list)")

    try:
        # Generate template
        template = generate_template(args.type, args.format)

        # Output
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(template)
            print(f"✓ Template generated: {args.output}", file=sys.stderr)
        else:
            print(template)

        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
