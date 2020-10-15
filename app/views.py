from app import app
from app.models import Url
from flask import flash, redirect, url_for, request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/long_to_short/', methods = ['GET','POST'])
def create_short_url(request):
    return "JSON FILE"


@app.route('/<short_postfix>', methods = ['GET'])
def short_postfix(short_postfix):
    long_url = Url.query.filter_by(short_url = short_postfix).first()
    if long_url == None:
        flash('There is no long URL for ' + short_postfix)
        return redirect(url_for('index'))
    return redirect(long_url)


@app.route('/statistics/<short_postfix>', methods = ['GET'])
def counter(short_postfix):
    return {"counter": short_postfix}

