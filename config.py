# config.py

# Flask app configuration
# DEBUG = True

import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)  # Generate a random hexadecimal string of 16 bytes (32 characters)
    OPENAI_API_KEY = "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"
    ACCOUNT_SID = "ACb50ea229c1a56b5f5a9134a1331d5d5f"
    AUTH_TOKEN = "667150a8b0451a3d4001ba36a04ba0b7"
    TWILIO_NUMBER = "+18449605383"
    TARGET_NUMBER = '+14085135080'
