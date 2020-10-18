from app import db


class Url(db.Model):
    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(), index=True, unique=True)
    short_url = db.Column(db.String(), index=True, unique=True)
    count = db.Column(db.Integer, default=0)

