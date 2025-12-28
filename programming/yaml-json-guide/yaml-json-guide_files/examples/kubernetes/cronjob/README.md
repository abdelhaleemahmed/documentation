# Kubernetes CronJob Examples

Complete CronJob examples for scheduled tasks like backups, cleanup, and reports.

## What is a CronJob?

CronJobs run Jobs on a schedule using cron syntax. Perfect for:
- **Backups** - Database dumps, file backups
- **Cleanup** - Delete old logs, temp files
- **Reports** - Generate daily/weekly reports
- **Maintenance** - Health checks, data updates
- **Batch processing** - ETL jobs, data sync

## Examples Included

1. **database-backup** - Daily database backup at 2 AM
2. **cleanup-old-logs** - Weekly log cleanup on Sundays
3. **send-daily-report** - Weekday reports at 9 AM

## Cron Schedule Syntax

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday=0)
│ │ │ │ │
│ │ │ │ │
* * * * *
```

### Common Schedules

```yaml
# Every hour
schedule: "0 * * * *"

# Every day at midnight
schedule: "0 0 * * *"

# Every day at 2:30 AM
schedule: "30 2 * * *"

# Every Monday at 9 AM
schedule: "0 9 * * 1"

# Every weekday at 6 PM
schedule: "0 18 * * 1-5"

# First day of month at midnight
schedule: "0 0 1 * *"

# Every 15 minutes
schedule: "*/15 * * * *"

# Every 6 hours
schedule: "0 */6 * * *"
```

## Quick Start

```bash
# Deploy all CronJobs
kubectl apply -f cronjob.yaml

# List CronJobs
kubectl get cronjobs

# View CronJob details
kubectl describe cronjob database-backup

# View Jobs created by CronJob
kubectl get jobs -l job-name

# View Job logs
kubectl logs job/database-backup-<timestamp>
```

## Configuration Details

### Basic CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: database-backup
spec:
  schedule: "0 2 * * *"  # 2 AM daily
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: postgres:15-alpine
            command: ["pg_dump", "..."]
          restartPolicy: OnFailure
```

### Concurrency Policy

```yaml
concurrencyPolicy: Forbid  # Don't start if previous job still running
# Options:
# - Allow: Allow concurrent jobs
# - Forbid: Skip if previous job running
# - Replace: Cancel previous and start new
```

### History Limits

```yaml
successfulJobsHistoryLimit: 3  # Keep last 3 successful jobs
failedJobsHistoryLimit: 3      # Keep last 3 failed jobs
```

### Timezone (Kubernetes 1.25+)

```yaml
timeZone: "America/New_York"
# Or: "UTC", "Europe/London", "Asia/Tokyo"
```

## Job Restart Policy

```yaml
restartPolicy: OnFailure  # Restart on failure
# Options:
# - OnFailure: Restart container on failure
# - Never: Don't restart (create new pod)
```

## Using Secrets

```yaml
env:
- name: DB_PASSWORD
  valueFrom:
    secretKeyRef:
      name: db-credentials
      key: password
```

## Persistent Storage

```yaml
volumes:
- name: backup-storage
  persistentVolumeClaim:
    claimName: backup-pvc

volumeMounts:
- name: backup-storage
  mountPath: /backup
```

## Testing CronJobs

### Manual Trigger

```bash
# Create a Job manually from CronJob
kubectl create job --from=cronjob/database-backup manual-backup-1

# View created job
kubectl get jobs

# View logs
kubectl logs job/manual-backup-1
```

### Suspend CronJob

```bash
# Suspend (stop creating new jobs)
kubectl patch cronjob database-backup -p '{"spec":{"suspend":true}}'

# Resume
kubectl patch cronjob database-backup -p '{"spec":{"suspend":false}}'
```

### Change Schedule

```bash
# Update schedule
kubectl patch cronjob database-backup -p '{"spec":{"schedule":"0 3 * * *"}}'
```

## Monitoring

### View CronJob Status

```bash
# List all CronJobs with last schedule time
kubectl get cronjobs

# Detailed status
kubectl describe cronjob database-backup
```

### View Jobs and Pods

```bash
# Jobs created by CronJob
kubectl get jobs -l job-name=database-backup

# Pods created by jobs
kubectl get pods -l job-name=database-backup

# Logs from specific job
kubectl logs -l job-name=database-backup-27854400
```

### Check Next Run Time

```bash
kubectl get cronjob database-backup -o=jsonpath='{.status.lastScheduleTime}'
```

## Error Handling

### Backoff Limit

```yaml
jobTemplate:
  spec:
    backoffLimit: 3  # Retry up to 3 times
```

### Active Deadline

```yaml
jobTemplate:
  spec:
    activeDeadlineSeconds: 3600  # Kill job after 1 hour
```

### TTL After Finished

```yaml
jobTemplate:
  spec:
    ttlSecondsAfterFinished: 86400  # Delete job after 24 hours
```

## Real-World Examples

### Database Backup with Compression

```yaml
command:
- /bin/sh
- -c
- |
  BACKUP_FILE="/backup/db-$(date +%Y%m%d-%H%M%S).sql.gz"
  pg_dump -h $DB_HOST -U $DB_USER $DB_NAME | gzip > $BACKUP_FILE
  echo "Backup saved: $BACKUP_FILE"
  ls -lh /backup/
```

### Upload to S3

```yaml
command:
- /bin/sh
- -c
- |
  BACKUP_FILE="db-$(date +%Y%m%d).sql"
  pg_dump ... > $BACKUP_FILE
  aws s3 cp $BACKUP_FILE s3://my-bucket/backups/
  echo "Uploaded to S3"
```

### Send Notification on Failure

```yaml
command:
- /bin/sh
- -c
- |
  if ! ./run-backup.sh; then
    curl -X POST $SLACK_WEBHOOK \
      -d '{"text":"Backup failed!"}'
    exit 1
  fi
```

### Cleanup with Size Limit

```yaml
command:
- /bin/sh
- -c
- |
  # Delete files older than 30 days OR larger than 100MB
  find /logs -mtime +30 -delete
  find /logs -size +100M -delete
  du -sh /logs
```

## Troubleshooting

### CronJob Not Running

```bash
# Check schedule is correct
kubectl get cronjob database-backup -o yaml | grep schedule

# Check if suspended
kubectl get cronjob database-backup -o yaml | grep suspend

# Check for errors
kubectl describe cronjob database-backup
```

### Job Failing

```bash
# View job status
kubectl describe job database-backup-<timestamp>

# Check pod logs
kubectl logs <pod-name>

# Check pod events
kubectl get events --sort-by='.lastTimestamp'
```

### No Jobs Being Created

```bash
# Check CronJob controller logs
kubectl logs -n kube-system -l component=kube-controller-manager
```

## Best Practices

1. **Set resource limits** - Prevent resource exhaustion
2. **Use PersistentVolumes** - For backups and logs
3. **Set concurrencyPolicy** - Avoid job overlap
4. **Limit job history** - Prevent accumulation
5. **Use secrets** - Never hardcode credentials
6. **Test schedules** - Verify cron expressions
7. **Monitor failures** - Set up alerts
8. **Set deadlines** - Prevent hung jobs

## Comparison with Job

| Feature | CronJob | Job |
|---------|---------|-----|
| **Runs** | On schedule | Once |
| **Creates** | Multiple Jobs | One Pod |
| **Use case** | Recurring tasks | One-time tasks |
| **Schedule** | Cron syntax | Immediate |

## When to Use CronJobs

✅ **Use CronJobs for:**
- Scheduled backups
- Periodic cleanup tasks
- Daily/weekly reports
- Batch data processing
- Health checks
- Certificate renewal

❌ **Don't use CronJobs for:**
- Continuous running services (use Deployment)
- Event-driven tasks (use Jobs or workflows)
- Real-time processing

## References

- [Kubernetes CronJob Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
- [Cron Expression Generator](https://crontab.guru/)
- [Job Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
