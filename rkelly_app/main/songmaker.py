import re
from random import randint, sample
import functools

import markovify
from flask import render_template, url_for, redirect

from ..models import SongLyrics
from .. import db
from . import main

# i'd or i'm -- to capitalize as I'd or I'm
pattern = r'\b(i)(\'[dm])?\b'
reg_abbrev = re.compile(pattern)


def get_lyrics_model():
    with open('all_lyrics.txt', 'r') as f:
        all_lyrics = f.read()
    return MultiSplit(all_lyrics)


class MultiSplit(markovify.Text):
    """Define where to split sentences for Markovify:
    Newlines, commas, periods
    """

    def sentence_split(self, text):
        return re.split(r"\s*\n\s*|\,|\.", text)


def repl(m):
    capitalized = m.group(1)
    if m.group(2):
        capitalized += m.group(2)
    return capitalized


class Song:
    """Song builder.
    """

    lyrics_model = get_lyrics_model()

    def __init__(self):
        self.verses = randint(2, 3)
        self.verse_length = randint(3, 4)
        self.chorus_length = randint(1, 3)
        self.repeat_chorus = randint(0, 1)
        self.title = None
        self.song_lyrics = None

    def pronoun_fix(self, section):
        """Capitalize I'd and I'm."""
        return re.sub(reg_abbrev, repl, section)

    def add_line(self, section):
        line = Song.lyrics_model.make_sentence(
            max_overlap_ratio=0.95, max_overlap_total=20)
        if line:
            line = line.lstrip()
            line = line.capitalize()
            line = self.pronoun_fix(line)
            section = section + "<br>" + line
        return section

    def make_section(self, length, section):
        for i in range(length):
            section = self.add_line(section)
        return section + "<br>"

    def make_title(self, song_lyrics):
        lyrics_words = re.split(r'\s*<br>\s*|\W', song_lyrics)
        title_word = sample(lyrics_words[:50], 1)[0]

        if len(title_word) > 3:
            end = lyrics_words.index(title_word) + 1
            start = randint(end - 3, end - 1)
            if start < 0:
                start = 0
            title_list = lyrics_words[start:end]
            title = " ".join(title_list).title()
            return title

        return self.make_title(song_lyrics)

    def build(self):
        lyrics = ""
        chorus = None

        for v in range(self.verses):
            lyrics = self.make_section(self.verse_length, lyrics)

            if not chorus or not self.repeat_chorus:
                chorus = self.make_section(self.chorus_length, "")

            lyrics = lyrics + chorus

        self.song_lyrics = lyrics
        self.title = self.make_title(lyrics)

    def save(self):
        song_lyrics = SongLyrics(
            title=self.title, song_lyrics=self.song_lyrics)
        song_lyrics.save()
        return song_lyrics.id
