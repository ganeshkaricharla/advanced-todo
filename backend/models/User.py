import uuid
import random
from datetime import datetime, timezone
from extensions import db, bcrypt


STYLISH_NAMES = [
    "Shadow", "Phantom", "Neon", "Cyber", "Glitch", "Blaze",
    "Storm", "Rogue", "Frost", "Venom", "Inferno", "Spectre"
]


class User(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.StringField(required=True, unique=True)
    password_hash = db.StringField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    created_at = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    last_login = db.DateTimeField()
    anonymous_name = db.StringField(required=True)
    be_anonymous = db.BooleanField(default=False)

    def set_password(self, password):
        """ Hashes and sets the password """
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """ Checks if password matches the stored hash """
        return bcrypt.check_password_hash(self.password_hash, password)
    
    @staticmethod
    def generate_unique_anonymous_username():
        """Generate a unique, stylish anonymous username"""
        while True:
            name = random.choice(STYLISH_NAMES)
            unique_id = uuid.uuid4().hex[:6].upper()
            anon_name = f"{name}_{unique_id}"

            # Ensure uniqueness in the database
            if not User.objects(anonymous_name=anon_name).first():
                return anon_name
    
    def save(self, *args, **kwargs):
        """ Auto-update 'updated_at' field before saving """
        if not self.anonymous_name:
            self.anonymous_name = self.generate_unique_anonymous_username()
        self.updated_at = datetime.now(timezone.utc)
        return super(User, self).save(*args, **kwargs)

    def to_json(self):
        """Return a dictionary representation of the user, respecting anonymity"""
        user_data = {
            "id": str(self.id),
            "username": self.anonymous_name if self.be_anonymous else self.username,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "last_login": self.last_login.strftime('%Y-%m-%d %H:%M:%S') if self.last_login else None,
        }

        # Show extra details only if user is NOT anonymous
        if not self.be_anonymous:
            user_data.update({
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
            })

        return user_data

