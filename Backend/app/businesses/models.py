from app import db
from datetime import datetime

class Business(db.Model):
    __tablename__ = 'businesses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Links to User model


    owner = db.relationship('User', back_populates='businesses')

    def __repr__(self):
        return f'<Business {self.name}, Owned by {self.owner.username}>'
