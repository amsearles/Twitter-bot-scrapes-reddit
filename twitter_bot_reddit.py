#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
from twitter import *
#holds reddit data
reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='', \
                     username='', \
                     password='')



#I'm choosing to scrape from TIL
subreddit = reddit.subreddit('NBA')

#sorting by new and getting data from there
new_subreddit = subreddit.hot(limit=25)
token = ''
token_secret = ''
consumer_key= ''
consumer_secret= ''

twit = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

#loops through top 25 hot posts and posts the urls to twiter
for new_submission in new_subreddit:
  twit.statuses.update(status=new_submission.url)
