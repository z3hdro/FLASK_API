from app import app, db, bp
import string
import random
from app.models import Url
from app.schemas import UrlSchema 
from flask import flash, redirect, url_for, request, jsonify
from marshmallow import ValidationError

@bp.route('/')
@bp.route('/index', methods = ['GET'])
def index():
    menu1 = '1)localhost:5000/long_to_short - send the long_url with request and get back the short version'
    menu2 = '2)localhost:5000/<short_postfix> - redirect to long_url comparing with short version'
    menu3 = '3)localhost:5000/statistics/<short_postfix> - get the counting of transition to short_url'
    return jsonify(op1=menu1,op2=menu2,op3=menu3), 200


@bp.route('/long_to_short', methods = ['POST'])
def create_short_url():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    schema = UrlSchema()
    try:
        data = schema.load(json_data)
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(6))
        link = Url(long_url=data['long_url'],short_url=result_str)
        db.session.add(link)
        db.session.commit()
        return jsonify(short_link="http://localhost:5000/{}".format(result_str)), 201
    except ValidationError as err:
        return err.messages, 422



@bp.route('/<short_postfix>/', methods = ['GET'])
def short_postfix(short_postfix):
    link = Url.query.filter_by(short_url = short_postfix).first()
    if link == None:
        flash('There is no long URL for ' + short_postfix)
        return redirect(url_for('index'))
    link.count = link.count + 1
    db.session.commit()
    return redirect(link.long_url)


@bp.route('/statistics/<short_postfix>/', methods = ['GET'])
def counter(short_postfix):
    link = Url.query.filter_by(short_url=short_postfix).first()
    if link == None:
        flash('There is no long URL for ' + short_postfix)
        return redirect(url_for('index'))
    return jsonify(count=link.count), 201

