from app import app
from flask import render_template
__author__ = 'dtsyganov'


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Dima'}
    return render_template('index.html', user=user)
