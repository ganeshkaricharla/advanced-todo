from flask import Flask
from config import Config  # Import config
from extensions import db, bcrypt  # Import extensions

# Initialize Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)


# Initialize extensions with app
db.init_app(app)
bcrypt.init_app(app)

# Import and register Blueprints after db is initialized
from routes.user_routes import user_bp  
app.register_blueprint(user_bp, url_prefix="/api/users")  

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
