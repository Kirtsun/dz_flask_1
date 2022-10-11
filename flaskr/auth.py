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
    ).fetchone()
    for res in trackss:
        trackss_ = res

    return render_template('auth/genre.html', trackss=trackss_)

@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    tracks_title = db.execute(
        'SELECT title, lenght FROM tracks'
    ).fetchall()
    return render_template('auth/tracks_sec.html', tracks_title=tracks_title)

@bp.route('/tracks-sec/statistics')
def statistics():
    db = get_db()
    statistics = db.execute(
        'SELECT AVG(lenght) as avg, SUM(lenght) as sum FROM tracks'
    ).fetchall()
    return render_template('auth/statistics.html', statistics=statistics)