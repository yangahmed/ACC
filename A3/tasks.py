from celery import Celery
import sys
import json
import re

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

# @app.task
# def add(x, y):
#     return x + y

@app.task
def count(word, data):
    count = 0
    for line in data:
        # parse the tweets
        try:
            tweet = json.loads(line)
        except:
            continue
        # disregard the "retweets"
        if 'retweeted_status' not in tweet:
            # read the text
            text = tweet['text']
            if re.search(word, text, re.I):
                count += 1

    return count