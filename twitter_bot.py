import re
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tweepy

from time import sleep
import os

URL = 'https://rkelly.hanhanhan.org/song-lyrics'
TWEET_LENGTH = 140
TWITTER_LINK_LENGTH = 23 + 1


def make_config_dict(f):
  
  d = {}

  with open(f) as info:
    for line in info:
      var = line.strip().split('=')
      if len(var) == 2:
        d[var[0]] = var[1]

    return d


def get_db_uri():
  postgres_config = make_config_dict('rkelly.env')
  database = postgres_config['DATABASE']
  user = postgres_config['DATABASE_USER']
  password = postgres_config['DATABASE_PASSWORD']

  database_uri = 'postgresql://{}:{}@localhost/{}'.format(database, password, user) 

  # database_uri ='postgresql://rkelly:hello@localhost/rkelly'
  return database_uri 


def authenticate_twitter():
  twitter_config = make_config_dict('twitter.env')

  consumer_key = twitter_config['consumer_key']
  consumer_secret = twitter_config['consumer_secret']
  key = twitter_config['access_token']
  secret = twitter_config['access_token_secret']

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(key, secret)

  api = tweepy.API(auth)
  return api


def generate_song():
  # generate new robot kelly song, and return its url

  r = requests.get(URL)
  song_url = r.url
  return song_url


def get_lyrics(song_id, database_uri):
  if song_id is None:
    song_id=5

  engine = create_engine(database_uri)
  connection = engine.connect()

  sql_query = "SELECT * FROM lyrics WHERE id = {}".format(song_id)
  result = connection.execute(sql_query)
  lyrics = result.first()[1]

  # necessary? would this close on exiting the function?
  connection.close()

  return lyrics


def twitterify_lyrics(lyrics):
  formatted_lyrics = re.sub('<br>(<br>)?','\n',lyrics).strip()
  lyrics_length = TWEET_LENGTH - TWITTER_LINK_LENGTH - 4
  lines = formatted_lyrics.split('\n')

  short_lyrics = ''
  running_length = 0

  for line in lines:
    running_length += len(line) + 1
    if running_length >= lyrics_length:
      break
    else:    
      short_lyrics = short_lyrics + '\n' + line

  if short_lyrics == '':
    short_lyrics = formatted_lyrics[:lyrics_length]

  return short_lyrics


def tweet(short_lyrics, api, url):  

    tweet = short_lyrics + "...\n" + url

    print(tweet)
    try:
        api.update_status(tweet)
    except tweepy.TweepError as e:
        print('This happened :( {}'.format((e.api_code)))

def main():
  api = authenticate_twitter()
  song_url = generate_song()
  regex = '(?:{})(\d+)'.format(URL)
  song_id = re.search(regex, song_url)

  db_uri = get_db_uri()
  lyrics = get_lyrics(song_id, db_uri)

  short_lyrics = twitterify_lyrics(lyrics)
  tweet(short_lyrics, api, song_url)




# 23 characters in t.co link

if __name__ == '__main__':
  main()