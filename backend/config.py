import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'