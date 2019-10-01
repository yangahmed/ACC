from celery import Celery
import sys
import json
import re

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

def count(word, file):
    data = file.read()
    count = 0
    for line in data:
        # parse the tweets
        try:
            tweet = json.loads(line)
        except:
            return
        # disregard the "retweets"
        if 'retweeted_status' not in tweet:
            # read the text
            text = tweet['text']
        
        if re.search(word, text, re.I):
            count += 1

    return count