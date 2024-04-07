# config.py

# Flask app configuration
# DEBUG = True

import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)  # Generate a random hexadecimal string of 16 bytes (32 characters)
    OPENAI_API_KEY = ""
    ACCOUNT_SID = ""
    AUTH_TOKEN = ""
    TWILIO_NUMBER = ""
    TARGET_NUMBER = ""

