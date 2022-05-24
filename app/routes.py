from app import app
from flask import render_template
from .forms.login import Login as LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'World'}
    return render_template('index.html', title='Index', user=user)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)