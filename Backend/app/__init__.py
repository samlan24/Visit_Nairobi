from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    csrf = CSRFProtect(app)
    csrf.init_app(app)

    from app.auth.models import User, Role
    from app.businesses.models import Business


    from app.auth import auth
    app.register_blueprint(auth)

    from app.businesses import business
    app.register_blueprint(business)

    from app.chats import chats
    app.register_blueprint(chats)

    from app.events import events
    app.register_blueprint(events)

    from app.categories import categories
    app.register_blueprint(categories)

    from app.location import location
    app.register_blueprint(location)

    from app.reviews import reviews
    app.register_blueprint(reviews)

    from app.search import search
    app.register_blueprint(search)

    return app


