from app import db
from datetime import datetime

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False, default="Nairobi")
    country = db.Column(db.String(100), nullable=False, default="Kenya")

    def __repr__(self):
        return f'<Location {self.name}, {self.city}, {self.country}>'
