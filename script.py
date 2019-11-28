#! usr/bin/env python3

from os.path import isfile
import pprint, praw
import pandas as pd
from time import sleep# Get credentials from DEFAULT instance in praw.ini
reddit = praw.Reddit()

ids = []
numcomments = 5000
data = {"comment_body":[], "upvotes": []}

def addTo(subreddit, data, ids, numcomments):
        for submission in subreddit:
                if (submission.id not in ids):
                        ids.append(submission.id)
                        submission.comments.replace_more(limit=None)
                        all_comments = submission.comments.list()
                        length = len(data["comment_body"])
                        if (length>numcomments):
                                print(length)
                                numcomments=numcomments*2
                        if (length > 200000):
                                break
                        for comment in all_comments:
                                data["comment_body"].append(comment.body)
                                data["upvotes"].append(comment.score)

addTo(reddit.subreddit('marvelstudios').hot(limit=None), data, ids, numcomments)
addTo(reddit.subreddit('marvelstudios').top(limit=None), data, ids, numcomments)
data_f = pd.DataFrame(data)
newdata = data_f.drop_duplicates(subset="comment_body", keep=False, inplace=False)
newdata.to_csv('data.csv', mode = "w", index=False) 
print(len(data_f))