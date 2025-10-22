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

### 2. Create Railway Project
1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will automatically detect the Dockerfile and use Docker for deployment

### 3. Add MySQL Database
1. In your Railway project dashboard
2. Click "New" → "Database" → "Add MySQL"
3. Railway will automatically create a MySQL instance

### 4. Set Environment Variables
In Railway dashboard, go to your service → Variables tab and add:

**Required Variables:**
- `SECRET_KEY`: Generate a new Django secret key
- `DEBUG`: Set to `false` for production
- `DJANGO_SETTINGS_MODULE`: Set to `main_project.settings`

**Email Variables (if using email features):**
- `EMAIL_HOST_USER`: Your Gmail address
- `EMAIL_HOST_PASSWORD`: Your Gmail app password

### 5. Database Connection
Railway automatically provides `DATABASE_URL` when you add MySQL addon.
Your app is already configured to use this.

### 6. Deploy
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