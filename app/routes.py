from app import app, db
from flask import render_template, flash, url_for, redirect
from .forms.login import Login as LoginForm
from .forms.registration import Registration as RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models.user import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'name': 'World'}
    return render_template('index.html', title='Index', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        if user.save():
            flash('Congratulations, you are now a registered user!')
        else:
            flash('Sorry something went wrong, Registration failed')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)