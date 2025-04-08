
from datetime import datetime, timezone
from extensions import db


class Task(db.Document):
    task_name = db.StringField(required=True)
    task_description = db.StringField(required=True)
    created_at = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    visibility = db.StringField(required=True)
    creator_id = db.StringField(required=True)
    project_id = db.StringField(required=True)
    status = db.StringField(required=True, choices=["Pending", "In Progress", "Completed","Deferred"])
    priority = db.StringField(required=True, choices=["Low", "Medium", "High"])
    due_date = db.DateTimeField()
    completion_date = db.DateTimeField()
    comments = db.ListField(db.StringField())
    

    def save(self, *args, **kwargs):
        """ Auto-update 'updated_at' field before saving """
        self.updated_at = datetime.now(timezone.utc)
        return super(Task, self).save(*args, **kwargs)

    def to_json(self):
        """Return a dictionary representation of the user, respecting anonymity"""
        task_data = {
            "id": str(self.id),
            "task_name": self.task_name,
            "task_description": self.task_description,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "visibility": self.visibility,
            "creator_id": self.creator_id,
            "project_id": self.project_id,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date.strftime('%Y-%m-%d %H:%M:%S'),
            "completion_date": self.completion_date.strftime('%Y-%m-%d %H:%M:%S') if self.completion_date else None,
            "comments": self.comments
        }

        return task_data
    
    def add_comment(self, comment):
        """Add a comment to the task"""
        self.comments.append(comment)
        self.save()
