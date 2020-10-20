from tests.conftest import app, db
import json
from flask_marshmallow import Marshmallow
from app import bp, views
from app.models import Url

link = 'https://mail.ru/'

def test_index(app):
    ma = Marshmallow(app)
    views.index
    app.register_blueprint(bp)
    with app.test_client() as client:
        resp = client.get('/index')
        data = json.loads(resp.data.decode())
        db.session.remove()
        assert resp.status_code == 200


def test_api(app):
    ma = Marshmallow(app)
    views.create_short_url
    app.register_blueprint(bp)
    with app.test_client() as client:
        response = client.post(
            '/long_to_short',
            data=json.dumps(dict(
                long_url=link
            )),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        db.session.remove()
        assert response.status_code == 201
        assert 'localhost' in data['short_link']

def test_count(app):
    ma = Marshmallow(app)
    views.create_short_url
    app.register_blueprint(bp)
    with app.test_client() as client:
        test_link = Url.query.filter_by(long_url=link).delete()
        db.session.commit()
        db.session.remove()
        assert Url.query.filter_by(long_url=link).first() == None