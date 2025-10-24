# Railway Deployment Guide

## Prerequisites
1. Railway account (sign up at railway.app)
2. GitHub repository with your code

## Step-by-Step Deployment

### 1. Push your code to GitHub
```bash
git add .
git commit -m "Prepare for Railway deployment with Docker"
git push origin main
```

### 2. Test Docker Build Locally (Optional but Recommended)
```bash
# Test the Docker build
chmod +x test-docker.sh
./test-docker.sh
```

### 3. Create Railway Project
1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will automatically detect the Dockerfile
6. **Important**: If Railway tries to use Nixpacks, go to Settings → Environment and set `RAILWAY_DOCKERFILE_PATH=Dockerfile`

### 4. Database Configuration
**Using SQLite** - No separate database service needed!
- ✅ SQLite database is built into the deployment
- ✅ No additional database addon required
- ✅ Simpler and faster deployment
- ⚠️ Note: For high-traffic production apps, consider PostgreSQL

### 5. Set Environment Variables
In Railway dashboard, go to your service → Variables tab and add:

**Required Variables:**
- `SECRET_KEY`: Generate a new Django secret key
- `DEBUG`: Set to `false` for production

**Email Variables:**
- `EMAIL_HOST_USER`: dileeplekkala14@gmail.com
- `EMAIL_HOST_PASSWORD`: yrhhsukcqcogphgz

### 6. Deploy
Railway will automatically deploy when you push to your connected branch.

### 7. Deploy
Railway will automatically deploy when you push to your connected branch.

## Important Notes

### Database Migration
The app will automatically run migrations on deployment via the start command.

### Static Files
Static files are collected automatically during deployment.

### Environment Variables for Local Development
Create a `.env` file in your project root:
```
SECRET_KEY=your-local-secret-key
DEBUG=True
DB_NAME=predictive_analysis
DB_USER=root
DB_PASSWORD=your-local-password
DB_HOST=localhost
DB_PORT=3306
```

### Custom Domain (Optional)
1. In Railway dashboard → Settings → Domains
2. Add your custom domain
3. Update DNS records as instructed

## Troubleshooting

### Build Fails
- Check the build logs in Railway dashboard
- Ensure all dependencies are in requirements.txt
- Docker build may take 10-15 minutes due to ML dependencies (TensorFlow, OpenCV)
- If build times out, try deploying again - Railway has generous build timeouts

### Database Connection Issues
- Ensure MySQL addon is added to your project
- Check that DATABASE_URL is automatically provided
- Verify migrations are running

### Static Files Not Loading
- Ensure STATIC_ROOT is set correctly
- Check that collectstatic runs during deployment

## Monitoring
- View logs in Railway dashboard
- Monitor resource usage
- Set up alerts for downtime

Your Django app with ML capabilities should now be live on Railway!
## Force 
Docker Build on Railway

If Railway still tries to use Nixpacks instead of Docker:

1. **Method 1**: Set environment variable in Railway dashboard:
   - Go to your service → Variables
   - Add: `RAILWAY_DOCKERFILE_PATH=Dockerfile`

2. **Method 2**: Delete and recreate the service:
   - Remove the current service
   - Create new service from GitHub repo
   - Ensure only Dockerfile exists (no Procfile, nixpacks.toml, etc.)

3. **Method 3**: Use Railway CLI:
   ```bash
   npm install -g @railway/cli
   railway login
   railway link
   railway up --detach
   ```

## Alternative: Manual Docker Deployment

If Railway continues to have issues, you can deploy to other platforms:

- **DigitalOcean App Platform**: Supports Dockerfile directly
- **Google Cloud Run**: Excellent for containerized Django apps
- **AWS App Runner**: Simple container deployment
- **Render**: Similar to Railway with good Docker support

All these platforms will work with your Dockerfile without modification.