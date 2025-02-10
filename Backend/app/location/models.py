from app import db
from datetime import datetime

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(200), nullable=False)  # Name of the town
    county = db.Column(db.String(100), nullable=False,)  # County
    area = db.Column(db.String(100), nullable=False)  # Area within the county

    businesses = db.relationship('Business', back_populates='location', lazy=True)
    events = db.relationship('Event', back_populates='location', lazy=True)


    def __repr__(self):
        return f'<Location {self.name}, {self.area}, {self.county}>'

