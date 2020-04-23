import re
from random import randint, sample
import functools

import markovify
from flask import render_template, url_for, redirect

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

    try:
        song_id = song.save()
        return redirect(url_for('.linked_lyrics', song=song, id=song_id))

    except Exception as e:
        print("song didn't save to db")
        print(dir(main))
        # app.logger.warn("Song did not save to database")
        # main.logger.info("Just so you know,Song did not save to database")
        return render_template('lyrics.html', song=song)

    return redirect(url_for('.index'))


@main.route('/song-lyrics/<int:id>', methods=['GET'])
def linked_lyrics(id, song=None):
    if not song:
        song = SongLyrics.query.get_or_404(id)
    return render_template('lyrics.html', song=song)


@main.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
