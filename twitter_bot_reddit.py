#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
from twitter import *
#holds reddit data
reddit = praw.Reddit(client_id='enter your client id here', \
                     client_secret='enter your client secret here', \
                     user_agent='name of app', \
                     username='reddit username', \
                     password='reddit password')



#I'm choosing to scrape from the NBA subreddit
subreddit = reddit.subreddit('NBA')

#sorting by new and getting data from there
new_subreddit = subreddit.new()

#Twitter Application Auth
token = ''
token_secret = ''
consumer_key= ''
consumer_secret= ''
twit = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

#stores data
reddit_dict = { "title":[], \
                "score":[], \
                "id":[], \
                "url":[],  \
                "comms_num": [], \
                "created": [], \
                "body":[]}
                
#for loop that populates reddit_dict with data for each category
for new_submission in new_subreddit:
  reddit_dict["title"].append(new_submission.title)
  twit.statuses.update(status= new_submission.title)
  reddit_dict["score"].append(new_submission.score)
  reddit_dict["id"].append(new_submission.id)
  reddit_dict["url"].append(new_submission.url)
  reddit_dict["comms_num"].append(new_submission.num_comments)
  reddit_dict["created"].append(new_submission.created)
  reddit_dict["body"].append(new_submission.selftext)

#using pandas module to make our data readable and pretty
reddit_data = pd.DataFrame(reddit_dict)

#converting reddit's unix timestamp
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = reddit_data["created"].apply(get_date)
reddit_data = reddit_data.assign(timestamp = _timestamp)

#exporting data to csv
reddit_data.to_csv('reddit_til_data.csv', index=False)

