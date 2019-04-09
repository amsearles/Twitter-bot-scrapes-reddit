#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
from twitter import *

#Twitter Access Tokens
token = ''
token_secret = ''
consumer_key= ''
consumer_secret= ''

#Reddit Access Tokens
reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='', \
                     username='', \
                     password='')

#Customization
sub_name = "NBA"
hash_tag_name = "#NBA"
delay_of_tweets = 1
 
subreddit = reddit.subreddit(sub_name)
new_subreddit = subreddit.hot(limit=25)


twit = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

#loops through top 25 hot posts and posts the urls to twiter
for new_submission in new_subreddit:
  twit.statuses.update(status=new_submission.url)
