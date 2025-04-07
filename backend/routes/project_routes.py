from flask import Blueprint, request, jsonify
from datetime import datetime, timezone

from flask_jwt_extended import get_jwt_identity, jwt_required
from models.Project import Project
from models.User import User

project_bp = Blueprint("project_routes", __name__)  # Define Blueprint

@project_bp.route("/create", methods=["POST"])
@jwt_required()
def create_project():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        # Fetch user id from JWT token
        user_id = get_jwt_identity()
        data["user_id"] = user_id

        # Validate required fields
        required_fields = ["project_name", "user_id","visibility"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        if data["project_name"] == "":
            return jsonify({"error": "Project name cannot be empty"}), 400
        
        if data["project_name"] == "Backlog":
            return jsonify({"error": "Project name cannot be 'Backlog'"}), 400

        if data["visibility"] not in ["private", "public"]:
            return jsonify({"error": "Visibility must be 'private' or 'public'"}), 400
        
        # Check if project name already exists
        if Project.objects(user_id=user_id, project_name=data["project_name"]).first():
            return jsonify({"error": "Project name already exists"}), 409
        # Create new project
        project = Project(
            project_name=data["project_name"],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
            visibility=data["visibility"] or "private",
            user_id=data["user_id"]
        )
        # Save to database
        project.save()
        print(f"Project {project.project_name} created successfully.")
        return jsonify({"message": "Project created successfully", "project": project.to_json()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500