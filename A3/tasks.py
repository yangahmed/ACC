from celery import Celery
import sys
import json
import re
import os

app = Celery('tasks', backend='rpc://', broker='pyamqp://jiayi:123@130.238.28.94/jiayi_master')

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
def count(words, path):
    count = [0] * len(words)
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
            textwords = text.split(' ')
            for i in range(len(words)):
                if words[i] in textwords:
                    count[i] += 1
    return count
 
# @app.task
# def count(word, path):
#     count = 0
#     f = open(path)
#     for line in f:
#         # parse the tweets
#         try:
#             tweet = json.loads(line)
#         except:
#             continue
#         # disregard the "retweets"
#         if 'retweeted_status' not in tweet:
#             # read the text
#             text = tweet['text']
#             if re.search(word, text, re.I):
#                 count += 1

#     return count