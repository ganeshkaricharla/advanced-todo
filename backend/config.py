# config.py

class Config:
    """Base configuration class for Flask app"""
    MONGODB_SETTINGS = {
        "db": "advanmced_todo_test",
        "host": "localhost",
        "port": 27017
    }
