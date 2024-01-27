import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


access_key = "************"
access_secret = "***************"
consumer_key = "*****************"
consumer_secret = "*************"

#Twitter Authentication
auth =tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_secret)

#Creating an API Obj
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = '@elonmusk',
                            count = 200,
                            include_rts = False,
                            tweet_mode = 'extended')

print(tweets)