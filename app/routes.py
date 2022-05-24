from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'name': app.config['SECRET_KEY']}
    return render_template('index.html', title='Index', user=user)