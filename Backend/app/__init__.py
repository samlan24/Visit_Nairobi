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

    from app.auth import auth
    app.register_blueprint(auth)

    return app


