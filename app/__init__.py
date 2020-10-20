from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_marshmallow import Marshmallow

bp = Blueprint('api_url', __name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

app = create_app()
db=SQLAlchemy(app)
ma = Marshmallow(app)

from app import views
app.register_blueprint(bp)