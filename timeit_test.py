import os, json
import timeit
import markovify

LYRICS_FOLDER = 'lyrics'
NGRAM_LENGTH = 3
LYRICS_MODEL = 'lyrics_model.json'

def open_file():
  with open(LYRICS_MODEL, 'r') as f:
    lyrics_json = f.read()
    lyrics_model = markovify.Text.from_json(lyrics_json)  

def make_file():
    all_lyrics = make_corpus()
    lyrics_model = markovify.NewlineText(all_lyrics)

def make_corpus():
    all_lyrics = ''

    for song in os.listdir(path=LYRICS_FOLDER):
        if not song.startswith('.'):
            song_file_path = os.path.join(LYRICS_FOLDER, song)
            with open(song_file_path, 'r') as f:
                lyrics = f.read()

            all_lyrics = all_lyrics + '\n' + lyrics

    return all_lyrics

def main():

    print(timeit.timeit(open_file, number=20))
    print(timeit.timeit(make_file, number=20))
    # opening the file is much slower than re-creating!
    # (scrape) etta:rkelly_scrape hannah$ python test.py
    # 4.746850703959353
    # 1.8148139060358517
    # (scrape) etta:rkelly_scrape hannah$ python test.py
    # 9.743756326031871
    # 3.5046791509957984


if __name__ == '__main__':
    main()