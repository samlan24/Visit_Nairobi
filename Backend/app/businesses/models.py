from app import db
from datetime import datetime
from app.models.associations import business_categories

class Business(db.Model):
    __tablename__ = 'businesses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    location = db.relationship('Location', back_populates='businesses')
    categories = db.relationship('Category', secondary=business_categories, backref=db.backref('businesses', lazy='dynamic'))
    reviews = db.relationship('Review', back_populates='business', lazy=True)
    events = db.relationship('Event', back_populates='business', lazy=True)

    owner = db.relationship('User', back_populates='businesses')

    def __repr__(self):
        return f'<Business {self.name}, Owned by {self.owner.username}>'
