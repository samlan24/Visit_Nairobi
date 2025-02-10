from app import db
from datetime import datetime


users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f'<Role {self.name}>'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    roles = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))


    businesses = db.relationship('Business', back_populates='owner', lazy='dynamic')
    reviews = db.relationship('Review', back_populates='user', lazy=True)
    events = db.relationship('Event', back_populates='user', lazy=True)

    def has_role(self, role_name):
        return any(role.name == role_name for role in self.roles)

    def add_role(self, role):
        if not self.has_role(role.name):
            self.roles.append(role)
            db.session.commit()

    def remove_role(self, role):
        if self.has_role(role.name):
            self.roles.remove(role)
            db.session.commit()

    def __repr__(self):
        roles_str = ', '.join(role.name for role in self.roles)
        return f'<User {self.username}, Roles: {roles_str}>'
