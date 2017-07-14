import tweepy
import re
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import SongLyrics


#

# generate new song

# check time
# get last song
# turn it into tweet
# get url of last song
# 

# sleep


# -- External connection approach
# tablename is 'lyrics'
# column name is 'song_lyrics'
result = connection.execute("select song_lyrics from lyrics order by id desc limit 1")
lyrics = result.fetchone()[0][:200]

# ------------- Part of app approach
from time import sleep
import os

def check_time_interval():
    now = time.time()
    now_str = int(now)

    last_tweet_time_str = os.getenv('LAST_TWEET_TIME', now_str)
    last_tweet_time = float(last_tweet_time_str)
    
    if now - last_tweet_time > tweet_interval:
        os.putenv('LAST_TWEET_TIME', now_str)
        return True

    return False

def get_song_query():
    song_id = os.getenv('SONG_ID', False)
    if song_id:
      sql_query = "select song_lyrics from lyrics where id = " + song_id
      return sql_query

def get_


def post_to_twitter(f):


    # Note: On some platforms, including FreeBSD and Mac OS X, 
    # setting environ may cause memory leaks. 
    # Refer to the system documentation for putenv.


    SQLALCHEMY_DATABASE_URI ='postgresql://rkelly:hello@localhost/rkelly'
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
      
    result = connection.execute(sql_query)
    lyrics = result.fetchone()[0][:200]


    time.sleep(tweet_interval)

    




# --------- Twitter

# to move
# twitter_config = {
#   'consumer_key':         
#   'consumer_secret':      
#   'access_token':         
#   'access_token_secret':  
#   'timeout_ms':           
# }

consumer_key = twitter_config['consumer_key']
consumer_secret = twitter_config['consumer_secret']
key = twitter_config['access_token']
secret = twitter_config['access_token_secret']

# do i need a callback url?
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
api = tweepy.API(auth)


def tweet(song):  
    # line = song
    line = "I got you got ya jumpin \n Hits lots of chips and trips on you and your time\nPeace our soldiers home\nJust keepin it real i'll be her #1 man\nWe We'll be making sweet love night till day\nAnd all these things for you"
    link = "http://rkelly.hanhanhan.org/"
    chars = 140 - 24
    line = line[:chars]
    tweet = line + " " + link
    tweet = tweet[:]
    print(tweet)
    # try:
    #     api.update_status(tweet)
    # except tweepy.TweepError as e:
    #     print('This happened :( {}'.format((e.api_code)))





# 23 characters in t.co link