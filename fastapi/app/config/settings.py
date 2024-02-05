# app/config/settings.py

import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

# Get the database URL from the environment variables or use a default value
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://ermuser:E3mu5eRpr@d@172.18.62.86/claim_qa")

# Other settings can be defined here
DEBUG = os.getenv("DEBUG", False)

# JWT secret key for authentication
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key")

# CORS (Cross-Origin Resource Sharing) settings
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
