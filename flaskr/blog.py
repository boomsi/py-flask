from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)



@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('POST', 'GET'))
def create():
    if request.method == 'POST':
        author_id = g.user['id']
        title = request.form['title']
        body = request.form['body']

        if not author_id:
            return redirect(url_for('auth.login'))

        error = None
        if not title:
            error = 'Title is required.'
        if not body:
            error = 'Body is required.'
        
        if not error:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES(?, ?, ?)',
                (title, body, author_id)
            )
            db.commit()
            return redirect(url_for('blog.index'))
        flash(error)
    return render_template('blog/create.html')

@bp.route('/update', methods=('GET', 'POST'))
def update():
    pass