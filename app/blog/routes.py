from app import db
from app.blog import bp
from flask import render_template, flash, url_for, redirect
from app.blog.forms.post import Post as PostForm
from flask_login import current_user, login_required
from app.models.post import Post
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
    post = Post()
    posts = post.all()
    return render_template('index.html', title='Index', posts=posts)

@bp.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=current_user)
        if post.add():
            flash('post added')
        else:
            flash('Sorry something went wrong')
        return redirect(url_for('blog.index'))
    return render_template("blog/new_post.html", title="Add New Post", form=form)