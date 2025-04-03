# extensions.py
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
import os

# Initialize extensions
db = MongoEngine()
bcrypt = Bcrypt()
