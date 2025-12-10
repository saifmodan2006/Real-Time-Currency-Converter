# 🚀 Deployment Guide for Real-Time Currency Converter

This guide covers multiple deployment options for the Real-Time Currency Converter application.

## Table of Contents
- [Local Deployment](#local-deployment)
- [Heroku Deployment](#heroku-deployment)
- [PythonAnywhere Deployment](#pythonanywhere-deployment)
- [AWS Deployment](#aws-deployment)
- [Docker Deployment](#docker-deployment)

---

## Local Deployment

### Development Server

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the development server**
   ```bash
   python app.py
   ```

3. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

### Production Server (using Gunicorn)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Parameters explained:**
- `-w 4`: Number of worker processes (adjust based on CPU cores)
- `-b 0.0.0.0:5000`: Bind to all interfaces on port 5000

---

## Heroku Deployment

### Prerequisites
- Heroku account (sign up at [heroku.com](https://www.heroku.com))
- Heroku CLI installed

### Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create a Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Deploy the application**
   ```bash
   git push heroku main
   ```

4. **View your app**
   ```bash
   heroku open
   ```

5. **Check logs**
   ```bash
   heroku logs --tail
   ```

### Environment Variables (if needed)
```bash
heroku config:set FLASK_ENV=production
```

---

## PythonAnywhere Deployment

### Prerequisites
- PythonAnywhere account (sign up at [pythonanywhere.com](https://www.pythonanywhere.com))

### Steps

1. **Upload your project**
   - Use the Files section in PythonAnywhere
   - Upload all project files

2. **Create a virtual environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 currency_converter
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to Web tab
   - Create a new web app
   - Choose Manual configuration
   - Select Python 3.10

5. **Configure WSGI file**
   - Edit the WSGI file and replace content with:
   ```python
   import sys
   path = '/home/yourusername/currency_converter'
   if path not in sys.path:
       sys.path.append(path)
   from app import app as application
   ```

6. **Reload the app**
   - Click Reload button
   - Your app will be live at `https://yourusername.pythonanywhere.com`

---

## AWS Deployment (EC2)

### Prerequisites
- AWS account
- EC2 instance running Ubuntu 20.04 or later

### Steps

1. **Connect to your EC2 instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

2. **Install system dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Real-Time-Currency-Converter.git
   cd Real-Time-Currency-Converter
   ```

4. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Create a Gunicorn service file**
   ```bash
   sudo nano /etc/systemd/system/currency-converter.service
   ```

   Add the following content:
   ```ini
   [Unit]
   Description=Currency Converter Flask Application
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/Real-Time-Currency-Converter
   Environment="PATH=/home/ubuntu/Real-Time-Currency-Converter/venv/bin"
   ExecStart=/home/ubuntu/Real-Time-Currency-Converter/venv/bin/gunicorn -w 4 -b localhost:8000 app:app

   [Install]
   WantedBy=multi-user.target
   ```

7. **Start the service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start currency-converter
   sudo systemctl enable currency-converter
   ```

8. **Configure Nginx**
   ```bash
   sudo nano /etc/nginx/sites-available/currency-converter
   ```

   Add the following content:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

9. **Enable the site**
   ```bash
   sudo ln -s /etc/nginx/sites-available/currency-converter /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

---

## Docker Deployment

### Create a Dockerfile

Create a `Dockerfile` in your project root:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

### Create a .dockerignore file

```
__pycache__
*.pyc
.env
.git
.gitignore
venv/
.vscode/
.idea/
```

### Build and Run

```bash
# Build the image
docker build -t currency-converter:latest .

# Run the container
docker run -p 5000:5000 currency-converter:latest

# Access at http://localhost:5000
```

### Docker Compose

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      FLASK_ENV: production
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

---

## DigitalOcean App Platform Deployment

### Prerequisites
- DigitalOcean account
- GitHub repository connected

### Steps

1. **Create new App**
   - Go to DigitalOcean dashboard
   - Click "Create" → "App"

2. **Connect GitHub**
   - Select your GitHub account
   - Choose the Currency Converter repository

3. **Configure the app**
   - Set Build Command: `pip install -r requirements.txt`
   - Set Run Command: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`
   - Set HTTP Port: `5000`

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete

---

## Performance Optimization Tips

1. **Use a production-grade WSGI server**
   - Gunicorn with multiple workers
   - Waitress or uWSGI as alternatives

2. **Enable caching headers**
   - Cache static files (CSS, JS)
   - Set appropriate Cache-Control headers

3. **Use a CDN**
   - CloudFlare for static assets
   - Reduces server load

4. **Monitor performance**
   - Use tools like Sentry for error tracking
   - Use New Relic for performance monitoring

5. **Database optimization**
   - If adding database, use connection pooling
   - Index frequently queried fields

---

## Troubleshooting

### Application won't start
- Check logs: `heroku logs --tail` (Heroku) or `systemctl status currency-converter` (AWS)
- Verify all dependencies are installed
- Check Python version compatibility

### Slow performance
- Increase number of Gunicorn workers
- Use a CDN for static files
- Enable gzip compression in Nginx

### API errors
- Verify internet connectivity
- Check API rate limits
- Implement retry logic with exponential backoff

### SSL/HTTPS issues
- Use Let's Encrypt for free SSL certificates
- Configure automatic renewal with Certbot

---

## Monitoring and Logging

### Application Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

### Health Check Endpoint (Optional)
```python
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200
```

---

## Security Checklist

- [ ] Set `FLASK_DEBUG=False` in production
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS/SSL
- [ ] Set up firewall rules
- [ ] Keep dependencies updated
- [ ] Implement rate limiting
- [ ] Add CORS headers if needed
- [ ] Validate and sanitize all inputs
- [ ] Use secure session cookies
- [ ] Regular security audits

---

## Support & Resources

- [Flask Documentation](https://flask.palletsprojects.com)
- [Heroku Documentation](https://devcenter.heroku.com)
- [Gunicorn Documentation](https://gunicorn.org)
- [Docker Documentation](https://docs.docker.com)

---

**Last Updated:** December 2024
