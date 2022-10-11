import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/names/')
def names():
    db = get_db()
    names_ = db.execute(
        'SELECT COUNT(DISTINCT artist) FROM tracks'
    )
    return render_template('auth/names.html', names_=names_)

@bp.route('/tracks/')
def tracks():
    db = get_db()
    tracks_ = db.execute(
        'SELECT COUNT(id) FROM tracks'
    )
    return render_template

@bp.route('/tracks/<genre>')
def tracks_genre():
    genre = request.form(['genre'])
    db = get_db()
    tracks = db.execute(
        'SELECT COUNT(id) FROM tracks WHERE genre =?', (genre, )
    )
    return render_template('auth/genre.html')



