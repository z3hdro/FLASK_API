import pytest
from config import Config
from app import create_app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

@pytest.fixture
def app():
    app = create_app()
    db.init_app(app)
    app.config.from_object(Config)
    with app.app_context():
        db.create_all()
        return app