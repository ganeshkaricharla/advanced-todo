from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
from models.User import User

user_bp = Blueprint("user_routes", __name__)  # Define Blueprint

@user_bp.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ["username", "email", "password", "first_name", "last_name"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Check if username or email already exists
        if User.objects(username=data["username"]).first() or User.objects(email=data["email"]).first():
            return jsonify({"error": "Username or Email already exists"}), 409

        # Create new user
        user = User(
            username=data["username"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            be_anonymous=data.get("be_anonymous", False)  # Defaults to False
        )

        # Assign anonymous name automatically
        user.anonymous_name = User.generate_unique_anonymous_username()

        # Hash the password before storing
        user.set_password(data["password"])

        # Save to database
        user.save()
        print(f"User {user.username} registered successfully.")
        return jsonify({"message": "User registered successfully", "user": user.to_json()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500



