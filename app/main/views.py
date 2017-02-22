import os, re, markovify
from random import randint
from flask import render_template, abort, url_for, redirect, current_app
from ..models import SongLyrics
from .. import db
from . import main 


@main.route('/')
def index():
    return render_template('index.html')

# some way to combine with created link? make song upon link click at index?
@main.route('/song-lyrics/')
def lyrics():
    # move to init app + import?
    with open('all_lyrics.txt', 'r') as f:
        all_lyrics = f.read()

    lyrics_model = Multi_Split(all_lyrics)

    verse_length = randint(3,6)
    chorus_length = randint(1,3)
    verses = randint(2,4)
    repeat_chorus = randint(0,1)
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
        return section


    for v in range(verses):
        verse = make_section(verse_length, "")

        if not chorus or not repeat_chorus: 
            chorus = make_section(chorus_length, "")
        if lyrics is "":
            lyrics = verse + "<br>" + chorus
        else:
            lyrics = lyrics + "<br>" + verse + "<br>" + chorus

    title = "this one"

    lyrics_db_item = SongLyrics(title=title, song_lyrics=lyrics)    
    db.session.add(lyrics_db_item)
    db.session.commit()
    return redirect(url_for('.linked_lyrics', id=lyrics_db_item.id))


@main.route('/song-lyrics/<int:id>', methods=['GET'])
def linked_lyrics(id):
    song = SongLyrics.query.get_or_404(id)
    return render_template('lyrics.html', song=song)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

class Multi_Split(markovify.Text):
    def sentence_split(self, text):
        return re.split(r"\s*\n\s*|\,|\.", text)