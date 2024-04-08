# config.py

# Flask app configuration
# DEBUG = True

import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)  # Generate a random hexadecimal string of 16 bytes (32 characters)
    OPENAI_API_KEY = "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"
    ACCOUNT_SID = ""
    AUTH_TOKEN = ""
    TWILIO_NUMBER = ""
    TARGET_NUMBER = ""

