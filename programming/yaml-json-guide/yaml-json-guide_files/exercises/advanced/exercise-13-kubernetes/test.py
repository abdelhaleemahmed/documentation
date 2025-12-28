#!/usr/bin/env python3
"""Test for Exercise 13: Kubernetes Manifest Debugging"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed")
    sys.exit(1)

def test_kubernetes_manifest():
    """Test that the deployment manifest is valid."""
    deployment_path = Path(__file__).parent / 'deployment.yaml'

    if not deployment_path.exists():
        print("❌ deployment.yaml not found")
        return False

    with open(deployment_path, 'r') as f:
        docs = list(yaml.safe_load_all(f))

    if len(docs) < 2:
        print("❌ Expected 2 documents (Deployment and Service)")
        return False

    deployment = docs[0]
    service = docs[1]

    # Check Deployment
    if deployment.get('kind') != 'Deployment':
        print("❌ First document should be a Deployment")
        return False

    print("✅ Found Deployment")

    # Check labels match selectors
    metadata_labels = deployment.get('metadata', {}).get('labels', {})
    selector_labels = deployment.get('spec', {}).get('selector', {}).get('matchLabels', {})
    template_labels = deployment.get('spec', {}).get('template', {}).get('metadata', {}).get('labels', {})

    if not selector_labels:
        print("❌ Missing selector.matchLabels")
        return False

    if selector_labels != template_labels:
        print(f"❌ Selector labels {selector_labels} don't match template labels {template_labels}")
        return False

    print("✅ Labels match selectors")

    # Check resources
    containers = deployment.get('spec', {}).get('template', {}).get('spec', {}).get('containers', [])
    if not containers:
        print("❌ No containers found")
        return False

    has_resources = any(
        'resources' in container and
        'limits' in container['resources'] and
        'requests' in container['resources']
        for container in containers
    )

    if not has_resources:
        print("❌ Missing resource limits/requests")
        return False

    print("✅ Resource limits configured")

    # Check health checks
    has_liveness = any('livenessProbe' in container for container in containers)
    has_readiness = any('readinessProbe' in container for container in containers)

    if not (has_liveness and has_readiness):
        print("❌ Missing health checks")
        return False

    print("✅ Health checks configured")

    # Check Service
    if service.get('kind') != 'Service':
        print("❌ Second document should be a Service")
        return False

    print("✅ Found Service")

    service_selector = service.get('spec', {}).get('selector', {})
    if not service_selector:
        print("❌ Service missing selector")
        return False

    print("✅ Service has selector")

    service_ports = service.get('spec', {}).get('ports', [])
    if not service_ports:
        print("❌ Service missing ports")
        return False

    print("✅ Service has ports")

    print("\n🎉 All Kubernetes manifest checks passed!")
    return True

if __name__ == '__main__':
    sys.exit(0 if test_kubernetes_manifest() else 1)
