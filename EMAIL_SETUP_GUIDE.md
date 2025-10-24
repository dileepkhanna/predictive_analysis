# Gmail Email Setup Guide for Django

## How to Get EMAIL_HOST_USER and EMAIL_HOST_PASSWORD

### EMAIL_HOST_USER
This is simply your Gmail address.
Example: `youremail@gmail.com`

### EMAIL_HOST_PASSWORD
This is **NOT** your regular Gmail password. You need to generate an **App Password**.

## Step-by-Step: Generate Gmail App Password

### 1. Enable 2-Factor Authentication (Required)
1. Go to your Google Account: https://myaccount.google.com/
2. Click **Security** in the left menu
3. Under "How you sign in to Google", click **2-Step Verification**
4. Follow the steps to enable 2FA (if not already enabled)

### 2. Generate App Password
1. Go to: https://myaccount.google.com/apppasswords
   - Or: Google Account → Security → 2-Step Verification → App passwords
2. You may need to sign in again
3. Under "Select app", choose **Mail**
4. Under "Select device", choose **Other (Custom name)**
5. Type a name like "Django App" or "Railway Deployment"
6. Click **Generate**
7. Google will show you a 16-character password like: `abcd efgh ijkl mnop`
8. **Copy this password** (remove spaces: `abcdefghijklmnop`)

### 3. Use in Railway Environment Variables

In Railway dashboard → Your Service → Variables:

```
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```

## Important Notes

### Security:
- ✅ **Never commit** email credentials to Git
- ✅ **Use environment variables** only
- ✅ **App passwords** are safer than regular passwords
- ✅ **Revoke** app passwords you're not using

### Current Configuration:
Your settings.py currently has hardcoded credentials:
```python
EMAIL_HOST_USER = "dileeplekkala23@gmail.com"
EMAIL_HOST_PASSWORD = "vyoglyupukxzfabn"
```

⚠️ **Security Risk**: These credentials are exposed in your code!

## Recommended: Update Settings for Production

Update your `settings.py` to use environment variables:

```python
# Email Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'dileeplekkala23@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'vyoglyupukxzfabn')
EMAIL_USE_TLS = True
```

This way:
- **Production** (Railway): Uses environment variables
- **Local Development**: Falls back to default values

## Alternative Email Services

If you have issues with Gmail, consider:

### 1. SendGrid (Recommended for Production)
- Free tier: 100 emails/day
- More reliable for production
- Setup: https://sendgrid.com/

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')
EMAIL_USE_TLS = True
```

### 2. Mailgun
- Free tier: 5,000 emails/month
- Setup: https://www.mailgun.com/

### 3. AWS SES
- Very cheap and reliable
- Good for high volume

## Testing Email Configuration

Test your email setup locally:

```python
# In Django shell
python manage.py shell

from django.core.mail import send_mail

send_mail(
    'Test Email',
    'This is a test email from Django.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

## Troubleshooting

### "Username and Password not accepted"
- Make sure 2FA is enabled
- Use App Password, not regular password
- Remove spaces from app password

### "SMTPAuthenticationError"
- Check if "Less secure app access" is OFF (it should be)
- Verify app password is correct
- Try generating a new app password

### Emails not sending
- Check spam folder
- Verify EMAIL_USE_TLS = True
- Check Railway logs for errors
- Ensure port 587 is not blocked

## Quick Setup Checklist

- [ ] Enable 2-Factor Authentication on Gmail
- [ ] Generate App Password
- [ ] Copy the 16-character password (remove spaces)
- [ ] Add to Railway environment variables
- [ ] Update settings.py to use environment variables
- [ ] Test email sending
- [ ] Remove hardcoded credentials from code

## Current Status

Your current email credentials in the code:
- Email: `dileeplekkala23@gmail.com`
- Password: `vyoglyupukxzfabn` (appears to be an app password)

⚠️ **Action Required**: 
1. Move these to environment variables
2. Remove from settings.py
3. Add to Railway dashboard only