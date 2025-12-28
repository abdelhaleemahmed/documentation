# Kubernetes StatefulSet Example - MySQL Cluster

Complete MySQL StatefulSet deployment with persistent storage and replication.

## What is a StatefulSet?

StatefulSets are designed for stateful applications that require:
- **Stable network identities** - Predictable pod names (mysql-0, mysql-1, mysql-2)
- **Persistent storage** - Each pod gets its own PersistentVolumeClaim
- **Ordered deployment** - Pods are created/deleted in order
- **Stable hostnames** - DNS entries like mysql-0.mysql.default.svc.cluster.local

## Components

- **Headless Service** - Enables direct pod-to-pod communication
- **StatefulSet** - Manages MySQL pods with persistent storage
- **ConfigMap** - Configuration for primary and replica nodes
- **Secret** - MySQL root password
- **VolumeClaimTemplates** - Automatic PVC creation per pod

## Architecture

```
┌─────────────┐
│ mysql Service│ (Headless, ClusterIP: None)
└──────┬──────┘
       │
   ┌───┴────┬────────┬────────┐
   │        │        │        │
┌──▼──┐  ┌──▼──┐  ┌──▼──┐  ┌──▼──┐
│mysql│  │mysql│  │mysql│  │mysql│
│  -0 │  │  -1 │  │  -2 │  │  -3 │
│(PRI)│  │(REP)│  │(REP)│  │(REP)│
└──┬──┘  └──┬──┘  └──┬──┘  └──┬──┘
   │        │        │        │
┌──▼──┐  ┌──▼──┐  ┌──▼──┐  ┌──▼──┐
│ PVC │  │ PVC │  │ PVC │  │ PVC │
│ 10Gi│  │ 10Gi│  │ 10Gi│  │ 10Gi│
└─────┘  └─────┘  └─────┘  └─────┘
```

## Quick Start

```bash
# Deploy the StatefulSet
kubectl apply -f statefulset.yaml

# Check pods (they start in order)
kubectl get statefulset mysql
kubectl get pods -l app=mysql -w

# Check persistent volume claims
kubectl get pvc
```

## Pod Naming

StatefulSets create pods with predictable names:
- `mysql-0` - Primary (first pod)
- `mysql-1` - Replica
- `mysql-2` - Replica

Each pod has a stable DNS name:
```
mysql-0.mysql.default.svc.cluster.local
mysql-1.mysql.mysql.default.svc.cluster.local
```

## Key Features Demonstrated

### 1. Stable Network Identity

```yaml
serviceName: mysql  # Associates with headless service
```

### 2. Persistent Storage

```yaml
volumeClaimTemplates:
- metadata:
    name: data
  spec:
    accessModes: ["ReadWriteOnce"]
    resources:
      requests:
        storage: 10Gi
```

Each pod gets its own PVC automatically.

### 3. InitContainers

```yaml
initContainers:
- name: init-mysql
  command:
  - bash
  - "-c"
  - |
    # Generate server-id from pod ordinal
    [[ `hostname` =~ -([0-9]+)$ ]] || exit 1
    ordinal=${BASH_REMATCH[1]}
    echo server-id=$((100 + $ordinal)) >> /mnt/conf.d/server-id.cnf
```

Configures each MySQL instance differently based on pod ordinal.

### 4. Headless Service

```yaml
clusterIP: None  # Makes it headless
```

No load balancing - direct pod access via DNS.

## Usage

### Connect to Primary (mysql-0)

```bash
# Port-forward to primary
kubectl port-forward mysql-0 3306:3306

# Connect from local machine
mysql -h 127.0.0.1 -u root -ppassword123
```

### Connect from Another Pod

```bash
# Run temporary pod
kubectl run mysql-client --rm -it --image=mysql:8.0 -- bash

# Connect to primary
mysql -h mysql-0.mysql -u root -ppassword123

# Connect to replica
mysql -h mysql-1.mysql -u root -ppassword123
```

### Test Replication

```bash
# On primary (mysql-0)
kubectl exec -it mysql-0 -- mysql -u root -ppassword123 -e "
  CREATE DATABASE testdb;
  USE testdb;
  CREATE TABLE test (id INT);
  INSERT INTO test VALUES (1);
"

# On replica (mysql-1)
kubectl exec -it mysql-1 -- mysql -u root -ppassword123 -e "
  USE testdb;
  SELECT * FROM test;
"
```

## Scaling

### Scale Up

```bash
# Add more replicas
kubectl scale statefulset mysql --replicas=5

# Pods created in order: mysql-3, mysql-4
kubectl get pods -l app=mysql -w
```

### Scale Down

```bash
# Remove replicas
kubectl scale statefulset mysql --replicas=2

# Pods deleted in reverse order: mysql-4, mysql-3
```

## Updates

### Rolling Update

```yaml
# Change image version
kubectl set image statefulset/mysql mysql=mysql:8.0.34

# Pods updated in reverse order
```

### Update Strategy

```yaml
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 2  # Only update pods >= mysql-2
```

## Persistent Data

### Check PVCs

```bash
kubectl get pvc

# Output:
# data-mysql-0   Bound   10Gi
# data-mysql-1   Bound   10Gi
# data-mysql-2   Bound   10Gi
```

### Data Persistence

Even if you delete pods, data persists:

```bash
# Delete pod
kubectl delete pod mysql-0

# Pod recreated with same name
# PVC reattached - data intact
```

## Cleanup

### Delete StatefulSet (Keep PVCs)

```bash
kubectl delete statefulset mysql

# Pods deleted, PVCs remain
kubectl get pvc
```

### Delete Everything

```bash
# Delete all resources
kubectl delete -f statefulset.yaml

# PVCs must be deleted manually
kubectl delete pvc data-mysql-0 data-mysql-1 data-mysql-2
```

## Troubleshooting

### Pod Not Starting

```bash
# Check events
kubectl describe statefulset mysql
kubectl describe pod mysql-0

# Check logs
kubectl logs mysql-0 -c init-mysql
kubectl logs mysql-0 -c mysql
```

### PVC Pending

```bash
# Check PVC status
kubectl describe pvc data-mysql-0

# Ensure StorageClass exists
kubectl get storageclass
```

### Replication Not Working

```bash
# Check replication status on replica
kubectl exec -it mysql-1 -- mysql -u root -ppassword123 -e "SHOW SLAVE STATUS\G"
```

## Best Practices

1. **Always use headless service** for StatefulSets
2. **Set resource limits** to prevent resource exhaustion
3. **Use init containers** for pod-specific configuration
4. **Implement health checks** (liveness & readiness probes)
5. **Back up data regularly** - PVCs alone aren't backups
6. **Test failover** before production use

## Differences from Deployment

| Feature | StatefulSet | Deployment |
|---------|-------------|------------|
| **Pod names** | Predictable (mysql-0) | Random (mysql-abc123) |
| **Storage** | Per-pod PVC | Shared storage |
| **Ordering** | Sequential | Parallel |
| **Network** | Stable hostname | Dynamic |
| **Use case** | Databases, queues | Stateless apps |

## When to Use StatefulSets

✅ **Use StatefulSets for:**
- Databases (MySQL, PostgreSQL, MongoDB)
- Message queues (Kafka, RabbitMQ)
- Distributed systems requiring stable identity
- Applications needing persistent per-pod storage

❌ **Don't use StatefulSets for:**
- Stateless applications
- Applications not requiring stable identity
- Simple web applications

## References

- [Kubernetes StatefulSet Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [MySQL on Kubernetes](https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/)
