from flask import Flask
from config import Config  # Import config
from extensions import db, bcrypt # Import extensions
from token_blacklist import setup_jwt  # Import JWT setup function


# Initialize Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)


# Initialize extensions with app
db.init_app(app)
bcrypt.init_app(app)
setup_jwt(app)

# Import and register Blueprints after db is initialized
from routes.user_routes import user_bp 
from routes.auth_routes import auth_bp   
app.register_blueprint(user_bp, url_prefix="/api/users")  
app.register_blueprint(auth_bp, url_prefix="/api/auth")
# Run the app
if __name__ == "__main__":
    app.run(debug=True)
