# Railway Environment Variables Setup

## Required Environment Variables for Your Project

When you deploy to Railway, add these environment variables in the Railway dashboard:

### How to Add Variables in Railway:
1. Go to your Railway project
2. Click on your service
3. Go to **Variables** tab
4. Click **+ New Variable**
5. Add each variable below

---

## Environment Variables to Add:

### 1. Django Secret Key
```
SECRET_KEY=your-new-secret-key-here
```

**How to generate a new secret key:**
```python
# Run this in Python shell
import secrets
print(secrets.token_urlsafe(50))
```

Or use this one (generate a new one for production):
```
SECRET_KEY=django-insecure-CHANGE-THIS-IN-PRODUCTION-xyz123abc456
```

### 2. Debug Mode
```
DEBUG=False
```
⚠️ **Important**: Always set to `False` in production!

### 3. Email Configuration
```
EMAIL_HOST_USER=dileeplekkala14@gmail.com
EMAIL_HOST_PASSWORD=yrhhsukcqcogphgz
```

✅ These are your Gmail app password credentials (already configured)

---

## Optional Variables (Railway provides these automatically):

### Database
Using SQLite - no DATABASE_URL needed!
```
Database: db.sqlite3 (included in deployment)
```
✅ **No database configuration required**

### Port (Automatic)
Railway automatically provides:
```
PORT=8080
```
❌ **Don't add this manually** - Railway sets this automatically

### Railway Environment (Automatic)
Railway automatically sets:
```
RAILWAY_ENVIRONMENT=production
```
❌ **Don't add this manually**

---

## Complete Setup Checklist:

### Step 1: No Database Setup Needed!
- ✅ Using SQLite - built into the app
- ✅ No separate database service required
- ✅ Database file included in deployment

### Step 2: Add Environment Variables
- [ ] `SECRET_KEY` - Generate a new one for production
- [ ] `DEBUG=False` - Disable debug mode
- [ ] `EMAIL_HOST_USER=dileeplekkala14@gmail.com`
- [ ] `EMAIL_HOST_PASSWORD=yrhhsukcqcogphgz`

### Step 3: Deploy
- [ ] Push code to GitHub
- [ ] Railway will automatically deploy
- [ ] Check logs for any errors

---

## Summary of Your Configuration:

### ✅ Already Configured in Code:
- Django settings use environment variables
- Database supports Railway's `DATABASE_URL`
- Static files configured
- Email settings with fallback values

### ✅ Your Email Credentials:
- **Email**: dileeplekkala14@gmail.com
- **App Password**: yrhhsukcqcogphgz
- **Status**: Ready to use

### 🔒 Security Notes:
- ✅ Email credentials use environment variables
- ✅ Fallback values for local development
- ✅ Production uses Railway environment variables
- ⚠️ Generate a new SECRET_KEY for production

---

## Testing After Deployment:

### 1. Check if app is running:
Visit your Railway URL (e.g., `https://your-app.railway.app`)

### 2. Test email functionality:
```python
# Using Railway CLI
railway run python manage.py shell

# Then in shell:
from django.core.mail import send_mail
send_mail(
    'Test from Railway',
    'Email is working!',
    'dileeplekkala14@gmail.com',
    ['recipient@example.com'],
)
```

### 3. Create superuser:
```bash
railway run python manage.py createsuperuser
```

### 4. Access admin:
Visit: `https://your-app.railway.app/admin`

---

## Quick Copy-Paste for Railway:

```
SECRET_KEY=django-insecure-GENERATE-NEW-KEY-HERE
DEBUG=False
EMAIL_HOST_USER=dileeplekkala14@gmail.com
EMAIL_HOST_PASSWORD=yrhhsukcqcogphgz
```

**Remember**: Generate a new SECRET_KEY before deploying!