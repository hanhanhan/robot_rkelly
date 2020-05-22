import re
from random import randint, sample
import functools

import markovify
from flask import render_template, url_for, redirect, make_response, session
from flask import current_app

from .songmaker import Song
from ..models import SongLyrics
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/image')
def image():
    return render_template('image.html')


@main.route('/song-lyrics/')
def lyrics():
    song = Song()
    song.build()

    try:
        song_id = song.save()
        return redirect(url_for('.linked_lyrics', id=song_id))

    except Exception:
        return render_template('lyrics.html', song=song)


@main.route('/song-lyrics/<int:id>', methods=['GET'])
def linked_lyrics(id, song=None):
    if not song:
        song = SongLyrics.query.get_or_404(id)
    return render_template('lyrics.html', song=song)


@main.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
