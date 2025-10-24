#!/usr/bin/env python
"""
Generate a new Django SECRET_KEY for production use.
Run this script to generate a secure secret key for Railway deployment.
"""

import secrets

def generate_secret_key():
    """Generate a secure secret key using Python's secrets module."""
    return secrets.token_urlsafe(50)

def generate_django_key():
    """Generate a secret key using Django's method (if Django is installed)."""
    try:
        from django.core.management.utils import get_random_secret_key
        return get_random_secret_key()
    except ImportError:
        return None

if __name__ == '__main__':
    print("=" * 70)
    print("Django SECRET_KEY Generator")
    print("=" * 70)
    print()
    
    # Method 1: Using secrets module
    key1 = generate_secret_key()
    print("Method 1 - Using Python secrets module:")
    print(f"SECRET_KEY={key1}")
    print()
    
    # Method 2: Using Django's method
    key2 = generate_django_key()
    if key2:
        print("Method 2 - Using Django's get_random_secret_key:")
        print(f"SECRET_KEY={key2}")
        print()
    
    print("=" * 70)
    print("Instructions:")
    print("=" * 70)
    print("1. Copy one of the SECRET_KEY values above")
    print("2. Go to Railway Dashboard → Your Service → Variables")
    print("3. Add a new variable:")
    print("   Name: SECRET_KEY")
    print("   Value: <paste the key here>")
    print()
    print("4. Also add these variables:")
    print("   DEBUG=False")
    print("   EMAIL_HOST_USER=dileeplekkala14@gmail.com")
    print("   EMAIL_HOST_PASSWORD=yrhhsukcqcogphgz")
    print()
    print("⚠️  IMPORTANT: Never commit this SECRET_KEY to Git!")
    print("=" * 70)