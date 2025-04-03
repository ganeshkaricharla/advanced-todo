# config.py
import os
from datetime import timedelta

class Config:
    """Base configuration class for Flask app"""
    MONGODB_SETTINGS = {
        "db": "advanmced_todo_test",
        "host": "localhost",
        "port": 27017
    }

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")  # Secret key for JWT
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRY", 15)))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv("REFRESH_TOKEN_EXPIRY", 7)))
    JWT_BLACKLIST_ENABLED = True  # Enable blacklisting
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"] 
