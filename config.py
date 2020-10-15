import os



class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = "1234"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

