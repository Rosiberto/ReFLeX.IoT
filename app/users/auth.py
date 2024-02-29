import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


from db.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():

    #print( request.form['name'] +"\n" +
    #      request.form['username'] +"\n" +
    #      request.form['password'] )

    if request.method == 'POST':
        
        name     = request.form['name']
        username = request.form['username']
        password = request.form['password']

        db = get_db()

        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO users (name, username, password) VALUES (?, ?, ?)",
                    (name, username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = "User {username} is already registered."
            else:
                return  redirect(url_for("auth.login"))

        flash(error)
        
    return render_template('./auth/login.html')


@bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        #print(username + " "+ password)

        db = get_db()
        
        error = None

        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']

            print(user['id'] , " "+user['username'] + " "+ user['password'])
            

            return redirect(url_for('pages.index'))

        flash(error)

    return render_template('./auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view