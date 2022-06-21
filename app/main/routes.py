from app import db
from app.main import bp
from flask import render_template, flash, url_for, redirect
from flask_login import current_user, login_required
from datetime import datetime

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Index')