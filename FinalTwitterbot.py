import pandas as pd
import tweepy
import time
import json
import random

# Twitter API Keys
from APITweeter2 import consumer_key
from APITweeter2 import consumer_secret
from APITweeter2 import access_token
from APITweeter2 import access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]


def tweetout(tweet_number):
    happy_quote = random.choice(xhappy_quotes)
    api.update_status(happy_quote)
    
counter=0
while(True):
    tweetout(counter)
    time.sleep(60)
    counter = counter + 1
