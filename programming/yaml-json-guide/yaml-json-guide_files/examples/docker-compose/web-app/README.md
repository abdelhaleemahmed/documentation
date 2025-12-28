# Docker Compose Web Application Example

Complete web application stack with frontend (Nginx), backend (Node.js), and database (PostgreSQL).

## Architecture

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ HTTP
       │
┌──────▼──────────┐
│  Nginx (80/443) │  Frontend
└──────┬──────────┘
       │
┌──────▼──────────┐
│  Node.js (3000) │  Backend API
└──────┬──────────┘
       │
┌──────▼──────────┐
│ PostgreSQL (5432│  Database
└─────────────────┘
```

## Services

### Frontend (Nginx)
- Serves static HTML/CSS/JS
- Reverse proxy to backend
- Ports: 80 (HTTP), 443 (HTTPS)

### Backend (Node.js)
- REST API
- Port: 3000
- Connects to PostgreSQL

### Database (PostgreSQL)
- Persistent data storage
- Port: 5432 (internal only)
- Automatic initialization

## Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+

## Quick Start

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Check status
docker-compose ps

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## Project Structure

```
web-app/
├── docker-compose.yml
├── frontend/
│   ├── html/
│   │   └── index.html
│   └── nginx.conf
├── backend/
│   ├── package.json
│   ├── index.js
│   └── ...
└── database/
    └── init.sql
```

## Setup Instructions

### 1. Create Frontend Files

```bash
mkdir -p frontend/html
```

Create `frontend/html/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Web App</title>
</head>
<body>
    <h1>Welcome to the Web App</h1>
    <div id="content"></div>
    <script>
        fetch('/api/data')
            .then(r => r.json())
            .then(data => {
                document.getElementById('content').innerHTML =
                    '<p>API Response: ' + JSON.stringify(data) + '</p>';
            });
    </script>
</body>
</html>
```

Create `frontend/nginx.conf`:
```nginx
events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;

    upstream backend {
        server backend:3000;
    }

    server {
        listen 80;
        server_name localhost;

        location / {
            root /usr/share/nginx/html;
            index index.html;
            try_files $uri $uri/ =404;
        }

        location /api/ {
            proxy_pass http://backend/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }

        location /health {
            access_log off;
            return 200 "healthy\n";
        }
    }
}
```

### 2. Create Backend Files

```bash
mkdir -p backend
```

Create `backend/package.json`:
```json
{
  "name": "web-backend",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.18.0",
    "pg": "^8.11.0"
  }
}
```

Create `backend/index.js`:
```javascript
const express = require('express');
const { Pool } = require('pg');

const app = express();
const port = process.env.PORT || 3000;

const pool = new Pool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD
});

app.get('/health', (req, res) => {
  res.send('OK');
});

app.get('/data', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW()');
    res.json({
      message: 'Hello from backend!',
      timestamp: result.rows[0].now
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(port, () => {
  console.log(`Backend listening on port ${port}`);
});
```

### 3. Create Database Init Script

```bash
mkdir -p database
```

Create `database/init.sql`:
```sql
-- Initialize database schema
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO users (username, email) VALUES
  ('alice', 'alice@example.com'),
  ('bob', 'bob@example.com')
ON CONFLICT DO NOTHING;
```

## Usage

### Start the Stack

```bash
docker-compose up -d
```

### Verify Services

```bash
# Check all services are running
docker-compose ps

# Should show:
# NAME            STATUS    PORTS
# web-frontend    Up        0.0.0.0:80->80/tcp
# web-backend     Up        0.0.0.0:3000->3000/tcp
# web-database    Up        5432/tcp
```

### Test the Application

```bash
# Test frontend
curl http://localhost/

# Test backend API
curl http://localhost:3000/data

# Test through nginx proxy
curl http://localhost/api/data

# Check health endpoints
curl http://localhost/health
curl http://localhost:3000/health
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend

# Last 100 lines
docker-compose logs --tail=100
```

### Execute Commands

```bash
# Connect to database
docker-compose exec database psql -U webuser -d webapp

# Run queries
docker-compose exec database psql -U webuser -d webapp -c "SELECT * FROM users;"

# Backend shell
docker-compose exec backend sh

# Install backend dependencies
docker-compose exec backend npm install
```

## Development Workflow

### Make Code Changes

1. Edit files in `backend/` or `frontend/`
2. Changes are reflected immediately (volume mounted)
3. For backend, restart service: `docker-compose restart backend`

### Rebuild Services

```bash
# Rebuild specific service
docker-compose up -d --build backend

# Rebuild all services
docker-compose up -d --build
```

### Database Management

```bash
# Backup database
docker-compose exec database pg_dump -U webuser webapp > backup.sql

# Restore database
docker-compose exec -T database psql -U webuser webapp < backup.sql

# Reset database
docker-compose down -v
docker-compose up -d
```

## Troubleshooting

### Service Won't Start

```bash
# Check logs
docker-compose logs backend

# Check service health
docker-compose ps

# Restart service
docker-compose restart backend
```

### Database Connection Issues

```bash
# Verify database is healthy
docker-compose exec database pg_isready -U webuser

# Check backend can connect
docker-compose exec backend ping database

# View database logs
docker-compose logs database
```

### Port Already in Use

```bash
# Find process using port 80
lsof -i :80

# Or change port in docker-compose.yml
# ports:
#   - "8080:80"  # Use port 8080 instead
```

## Production Considerations

1. **Use environment variables file**
   ```bash
   # Create .env file
   echo "POSTGRES_PASSWORD=secure_password" > .env
   echo ".env" >> .gitignore
   ```

2. **Enable SSL/TLS**
   - Add SSL certificates to nginx
   - Configure HTTPS in nginx.conf

3. **Add persistent logging**
   ```yaml
   volumes:
     - ./logs:/var/log/nginx
   ```

4. **Use secrets for passwords**
   - Docker Swarm secrets
   - HashiCorp Vault
   - AWS Secrets Manager

5. **Add monitoring**
   - Prometheus + Grafana
   - ELK Stack
   - Health check endpoints

## Cleanup

```bash
# Stop and remove containers
docker-compose down

# Remove volumes (deletes database data!)
docker-compose down -v

# Remove images
docker-compose down --rmi all
```

## Next Steps

- Add Redis for caching
- Implement authentication
- Set up CI/CD pipeline
- Add monitoring and logging
- Implement backup strategy

## References

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
