# Troubleshooting 502 Bad Gateway Error on Railway

## What is a 502 Error?

A 502 Bad Gateway error means Railway can't connect to your application. This usually happens when:
- The app failed to start
- The app crashed during startup
- The app is listening on the wrong port
- There's an error in your code

## How to Fix:

### Step 1: Check Railway Logs

1. Go to Railway Dashboard
2. Click on your service
3. Go to **"Deployments"** tab
4. Click on the latest deployment
5. Check the **logs** for errors

### Step 2: Common Issues and Fixes

#### Issue 1: Missing Environment Variables
**Symptom:** App crashes on startup
**Fix:** Add these variables in Railway:
```
SECRET_KEY=WWYdj4YNaKUwCod_DFwNraNZp14fNCg1Wz_GktsJq1fTvuB6u28HQW_fVDMvNkXxu9w
DEBUG=False
EMAIL_HOST_USER=dileeplekkala14@gmail.com
EMAIL_HOST_PASSWORD=yrhhsukcqcogphgz
```

#### Issue 2: Static Files Error
**Symptom:** Error during collectstatic
**Fix:** The static directory might be missing files

Let me check if we need to create a dummy static file...

#### Issue 3: Database Migration Error
**Symptom:** Migration fails during startup
**Fix:** This shouldn't happen with SQLite, but check logs

#### Issue 4: Port Binding Issue
**Symptom:** App starts but Railway can't connect
**Fix:** Ensure Dockerfile uses `$PORT` variable (already configured)

### Step 3: Quick Fixes to Try

#### Fix 1: Update Dockerfile to handle static files better
The collectstatic command might be failing. Let's make it optional.

#### Fix 2: Ensure ALLOWED_HOSTS is set correctly
Railway needs the app to accept connections from any host.

#### Fix 3: Add a health check endpoint
This helps Railway know when the app is ready.

## What to Look For in Logs:

### Good Signs:
```
✓ Collecting static files
✓ Running migrations
✓ Starting gunicorn
✓ Listening on 0.0.0.0:PORT
```

### Bad Signs:
```
✗ ModuleNotFoundError
✗ ImproperlyConfigured
✗ OperationalError
✗ Address already in use
```

## Most Likely Issue:

Based on the 502 error, the most common cause is:
1. **Static files collection failing** - The static directory might be empty
2. **Missing environment variables** - SECRET_KEY or DEBUG not set
3. **Database migration issue** - Though unlikely with SQLite

## Let Me Fix This:

I'll update the Dockerfile to make static collection more robust and add better error handling.