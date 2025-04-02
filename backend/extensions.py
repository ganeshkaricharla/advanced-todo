# extensions.py

from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt


# Initialize extensions
db = MongoEngine()
bcrypt = Bcrypt()
