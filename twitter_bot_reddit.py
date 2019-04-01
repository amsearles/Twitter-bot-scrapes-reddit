#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
from twitter import *
#holds reddit data
reddit = praw.Reddit(client_id='S-FNWZ8XEqEA6Q', \
                     client_secret='XlxBCDr51d507sGur_V93faOymA', \
                     user_agent='til_scraper', \
                     username='sensitiverocketsfan', \
                     password='akiena')



#I'm choosing to scrape from TIL
subreddit = reddit.subreddit('NBA')

#sorting by new and getting data from there
new_subreddit = subreddit.hot(limit=25)
token = '1111285762639618054-9dC3FSKRMmlGCjyJth75qxMRIDgcuv'
token_secret = 'nUnfVi46s5nnGHaN5EXs9yaCVfw5w2AC03fsKrJduaDfN'
consumer_key= 'onn48otrr2iOxyCXS98V5gTQL'
consumer_secret= 'BJaXOhQ2OS2cNh7cnBDagAGxolYIKfjNvcAjeIdN2xUNtp4sxj'

twit = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

#loops through top 25 hot posts and posts the urls to twiter
for new_submission in new_subreddit:
  twit.statuses.update(status=new_submission.url)
