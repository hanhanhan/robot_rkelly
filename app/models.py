from . import db
from datetime import datetime


class SongLyrics(db.Model):
    __tablename__ = 'lyrics'
    id = db.Column(db.Integer, primary_key=True)
    song_lyrics = db.Column(db.Text)
    title = db.Column(db.Text)
    created = db.Column(db.DateTime(), default=datetime.utcnow)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            print("saving the song didn't work")
        finally:
            db.session.close()
