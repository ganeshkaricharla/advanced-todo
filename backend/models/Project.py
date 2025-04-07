import uuid
import random
from datetime import datetime, timezone
from extensions import db, bcrypt



class Project(db.Document):
    project_name = db.StringField(required=True)
    created_at = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    visibility = db.StringField(required=True)
    user_id = db.StringField(required=True)

    def save(self, *args, **kwargs):
        """ Auto-update 'updated_at' field before saving """
        self.updated_at = datetime.now(timezone.utc)
        return super(Project, self).save(*args, **kwargs)

    def to_json(self):
        """Return a dictionary representation of the user, respecting anonymity"""
        project_data = {
            "id": str(self.id),
            "project_name": self.project_name,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "visibility": self.visibility,
            "user_id": self.user_id
        }

        return project_data
    

