
import tweepy
import time
import json
import random



# Twitter API Keys
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
# Quotes to Tweet
ToPost = [
    "This is one status",
    "Hola",
    "Ca Va",
    "Bonjour",
    "Hullo",
    "hi",
    "Hello"]


def tweetout(tweet_number):
    ToPost = random.choice(ToPost)
    api.update_status(ToPost)
    
counter=0
while(True):
    tweetout(counter)
    time.sleep(60)
    counter = counter + 1
