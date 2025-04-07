from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token, 
    jwt_required, get_jwt_identity, get_jwt
)
from token_blacklist import blacklisted_tokens
from datetime import datetime, timedelta
from models.User import User
from flask import current_app 
auth_bp = Blueprint('auth_routes', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """Authenticate user and return JWT tokens"""
    data = request.get_json()

    if "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.objects(username=data["username"]).first()
    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid username or password"}), 401

    # Update last login time
    user.update(last_login=datetime.utcnow())

    # Generate access and refresh tokens
    access_token = create_access_token(identity=str(user.id), expires_delta=current_app.config["JWT_ACCESS_TOKEN_EXPIRES"])
    refresh_token = create_refresh_token(identity=str(user.id), expires_delta=current_app.config["JWT_REFRESH_TOKEN_EXPIRES"])

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "message": "Login successful"
    }), 200



@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """Invalidate the current token (logout)"""
    jti = get_jwt()["jti"]  # Get the token's unique ID
    blacklisted_tokens.add(jti)  # Add to blacklist

    return jsonify({"message": "Logged out successfully!"}), 200


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Generate a new access token using a refresh token"""
    user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=user_id, expires_delta=app.config["JWT_ACCESS_TOKEN_EXPIRES"])
    
    return jsonify({
        "access_token": new_access_token,
        "message": "Access token refreshed successfully"
    }), 200

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get details of the logged-in user"""
    user_id = get_jwt_identity()
    user = User.objects(id=user_id).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }), 200
