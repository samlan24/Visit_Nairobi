from app import db

business_categories = db.Table(
    'business_categories',
    db.Column('business_id', db.Integer, db.ForeignKey('businesses.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)
