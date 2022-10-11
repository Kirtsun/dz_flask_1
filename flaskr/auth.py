import functools

from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)


from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/names/')
def names():
    db = get_db()
    names_ = db.execute(
        'SELECT COUNT(DISTINCT artist) FROM tracks'
    ).fetchone()
    for res in names_:
        names_in_tracks = res
    return render_template('auth/names.html', names_=names_in_tracks)

@bp.route('/tracks/')
def tracks():
    db = get_db()
    tracks_ = db.execute(
        'SELECT COUNT(id) FROM tracks'
    ).fetchone()
    for res in tracks_:
        tracks_number = res
    return render_template('auth/tracks.html', tracks_=tracks_number)

@bp.route('/tracks/<genre>')
def tracks_genre():
    genre = request.form(['genre'])
    db = get_db()
    trackss = db.execute(
        'SELECT COUNT(id) FROM tracks WHERE genre =?', (genre, )
    )

    return render_template('auth/genre.html', trackss=trackss)



