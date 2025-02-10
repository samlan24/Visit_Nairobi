from app import db
from datetime import datetime



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'<Role {self.name}>'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    role = db.relationship('Role', backref='users', lazy=True)
    business = db.relationship('Business', back_populates='owner', lazy='dynamic')
    chats = db.relationship('Chat', backref='user', lazy=True)
    reviews = db.relationship('Review', back_populates='user', lazy=True)
    events = db.relationship('Event', back_populates='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}, Role {self.role.name}>'