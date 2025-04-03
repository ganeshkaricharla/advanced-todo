from flask_jwt_extended import JWTManager

blacklisted_tokens = set()  # Store revoked tokens

def check_if_token_revoked(jwt_header, jwt_data):
    """Check if the token is in the blacklist"""
    return jwt_data["jti"] in blacklisted_tokens

def setup_jwt(app):
    """Initialize JWTManager and set up the blacklist check"""
    jwt = JWTManager(app)
    jwt.token_in_blocklist_loader(check_if_token_revoked)
    return jwt
