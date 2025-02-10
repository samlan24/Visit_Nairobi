from app import db
from datetime import datetime

class Chat(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)

    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


    user = db.relationship('User', backref=db.backref('chats', lazy=True))
    business = db.relationship('Business', backref=db.backref('chats', lazy=True))

    def __repr__(self):
        return f'<Chat {self.id} - {self.user_id} to {self.business_id}>'
