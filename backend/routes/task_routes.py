from flask import Blueprint, request, jsonify
from datetime import datetime, timezone

from flask_jwt_extended import get_jwt_identity, jwt_required
from models.Project import Project
from models.User import User
from models.Task import Task


task_bp = Blueprint('task_routes', __name__)
@task_bp.route('/create', methods=['POST'])
@jwt_required()
def create_task():
    """Create a new task"""
    data = request.get_json()
    user_id = get_jwt_identity()

    # Validate input data
    required_fields = ["task_name", "task_description", "project_id", "status", "priority"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # Check if the project exists and if the user is a member of it
    project = Project.objects(id=data["project_id"]).first()
    if not project:
        return jsonify({"error": "Project not found"}), 404

    # Check if the user is a member of the project
    if not user_id == project.user_id:
        return jsonify({"error": "User is not a member of the project"}), 403
    
    # Create the task
    task = Task(
        task_name=data["task_name"],
        task_description=data["task_description"],
        visibility=data["visibility"],
        creator_id=user_id,
        project_id=data["project_id"],
        status=data["status"],
        priority=data["priority"],
        due_date=datetime.strptime(data.get("due_date"), '%Y-%m-%d %H:%M:%S') if data.get("due_date") else None,
        completion_date=datetime.strptime(data.get("completion_date"), '%Y-%m-%d %H:%M:%S') if data.get("completion_date") else None,
        comments=data.get("comments", [])
    )
    task.save()

    return jsonify(task.to_json()), 201

# GET all tasks in a project
@task_bp.route('/project/<project_id>', methods=['GET'])
@jwt_required()
def get_tasks_by_project(project_id):
    """Get all tasks in a project"""
    user_id = get_jwt_identity()
    project = Project.objects(id=project_id).first()
    if not project:
        return jsonify({"error": "Project not found"}), 404

    # Check if the user is a member of the project
    if not user_id == project.user_id:
        return jsonify({"error": "User is not a member of the project"}), 403

    tasks = Task.objects(project_id=project_id)
    return jsonify([task.to_json() for task in tasks]), 200


@task_bp.route('/<task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    """Get a task by its ID"""
    task = Task.objects(id=task_id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task.to_json()), 200

@task_bp.route('/<task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    """Update a task by its ID"""
    data = request.get_json()
    task = Task.objects(id=task_id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    # Update task fields
    for key, value in data.items():
        if hasattr(task, key):
            setattr(task, key, value)

    task.save()

    return jsonify(task.to_json()), 200

@task_bp.route('/<task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    """Delete a task by its ID"""
    task = Task.objects(id=task_id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    task.delete()

    return jsonify({"message": "Task deleted successfully"}), 200
