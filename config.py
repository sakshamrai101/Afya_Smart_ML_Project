# config.py

# Flask app configuration
# DEBUG = True

import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)  # Generate a random hexadecimal string of 16 bytes (32 characters)
    OPENAI_API_KEY = "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"
    ACCOUNT_SID = "ACb50ea229c1a56b5f5a9134a1331d5d5f"
    AUTH_TOKEN = "3f4a3d2961f08b86500f40be8552ebe9"
    TWILIO_NUMBER = "+18449605383"
    TARGET_NUMBER = '+14085135080'