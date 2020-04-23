import re
from random import randint, sample
import functools

import markovify
from flask import render_template, url_for, redirect
from flask import current_app

from .songmaker import Song
from ..models import SongLyrics
from .. import db
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

    songlyrics = SongLyrics(
        title=song.title,
        song_lyrics=song.song_lyrics)

    try:
        songlyrics.save()
    except Exception as e:
        current_app.logger.warn('Song did not save to database\n {}'.format(e))
        return render_template('lyrics.html', song=song)
    else:
        return redirect(url_for('.linked_lyrics', song=song, id=songlyrics.id))

    return redirect(url_for('.index'))


@main.route('/song-lyrics/<int:id>', methods=['GET'])
def linked_lyrics(id, song=None):
    if not song:
        current_app.logger.warn('Song requested, 404 returned.'.format(id))
        song = SongLyrics.query.get_or_404(id)
    return render_template('lyrics.html', song=song)


@main.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
