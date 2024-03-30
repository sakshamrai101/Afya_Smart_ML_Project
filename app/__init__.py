from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes (after app creation to avoid circular imports)
from app import routes