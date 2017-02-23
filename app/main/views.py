import os
import re
from random import randint, sample

import markovify
from flask import render_template, url_for, redirect

from ..models import SongLyrics
from .. import db
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/image')
def image():
    return render_template('image.html')

# some way to combine with created link? make song upon link click at index?
@main.route('/song-lyrics/')
def lyrics():
    # move to init app + import?
    with open('all_lyrics.txt', 'r') as f:
        all_lyrics = f.read()

    lyrics_model = Multi_Split(all_lyrics)

    verse_length = randint(3, 6)
    # verse_length = randint(20, 20)
    chorus_length = randint(1, 3)
    verses = randint(2, 4)
    # verses = randint(10, 14)
    repeat_chorus = randint(0, 1)
    chorus = None
    lyrics = ""

    def add_line(section):
        line = lyrics_model.make_sentence(
            max_overlap_ratio=0.95, max_overlap_total=20)
        if line:
            line = line.lstrip()
            line = line.capitalize()
            section = section + "<br>" + line
        return section

    def make_section(length, section):
        for i in range(length):
            section = add_line(section)
        return section + "<br>"

    def make_title(lyrics):
        lyrics_words = re.split('\s*<br>\s*|\W', lyrics)
        title_word = sample(lyrics_words[:50], 1)[0]
        if len(title_word) > 3:
            end = lyrics_words.index(title_word) + 1
            start = randint(end - 3, end - 1)
            if start < 0:
                start = 0
            title_list = lyrics_words[start:end]
            title = " ".join(title_list).title()
            print('\nmake_title()', title_word, 'title_word', title_list, 'title_list', title, 'title', type(title))
            return title
        else:
            make_title(lyrics)

    for v in range(verses):
        lyrics = make_section(verse_length, lyrics)

        if not chorus or not repeat_chorus:
            chorus = make_section(chorus_length, "")

        lyrics = lyrics + chorus 


    title = make_title(lyrics)
    print(title, 'Title', type(title))

    lyrics_db_item = SongLyrics(title=title, song_lyrics=lyrics)

    db.session.add(lyrics_db_item)
    db.session.commit()

    return redirect(url_for('.linked_lyrics', id=lyrics_db_item.id))


@main.route('/song-lyrics/<int:id>', methods=['GET'])
def linked_lyrics(id):
    song = SongLyrics.query.get_or_404(id)
    print('\nlinked_lyrics route song title: ', song.title)
    return render_template('lyrics.html', song=song)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


class Multi_Split(markovify.Text):
    def sentence_split(self, text):
        return re.split(r"\s*\n\s*|\,|\.", text)