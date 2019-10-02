from celery import Celery
import sys
import json
import re
import os

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def sum(word, p):
    c = 0
    files= os.listdir(p)
    for file in files:
        path = p + "/" + file
        result = count.delay(word, path)
        c += result.get()
    return c

@app.task
def count(word, path):
    count = 0
    f = open(path)
    for line in f:
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
