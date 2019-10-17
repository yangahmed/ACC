from tasks import count
import os
from flask import Flask, jsonify
from flask import request
import time

app = Flask(__name__)

p = '/home/ubuntu/data'

@app.route('/count', methods=['GET'])
def count_word():
    t_start = time.time()
    words = request.args.get("words")
    wordlist = words.split(',')
    files= os.listdir(p)
    res = [0] * len(wordlist)
    result = []
    for file in files:
        path = p + "/" + file
        result.append(count.delay(wordlist, path))

    for i in range(len(result)):
        temp = result[i].get()
        for j in range(len(res)):
            res[j] += temp[j]

    d = {}
    for ii in range(len(wordlist)):
        d[wordlist[ii]] = res[ii]

    t_end = time.time()
    print('time:', t_end - t_start, 's')

    return jsonify(d)

@app.route('/scalemeasure', methods=['GET'])
def scale_measure():
    t_start = time.time()
    words = request.args.get("words")
    workers = request.args.get("workers")
    int(workers)
    wordlist = words.split(',')
    files= os.listdir(p)
    res = [0] * len(wordlist)
    result = []
    for ii in range(len(files)/workers):
        path = p + "/" + files[ii]
        result.append(count.delay(wordlist, path))

    for i in range(len(result)):
        temp = result[i].get()
        for j in range(len(res)):
            res[j] += temp[j]

    d = {}
    for ii in range(len(wordlist)):
        d[wordlist[ii]] = res[ii]

    t_end = time.time()
    print('time:', t_end - t_start, 's')

    return jsonify(d)

# @app.route('/count', methods=['GET'])
# def count_word():
#     words = request.args.get("words")
#     wordlist = words.split(',')
#     files= os.listdir(p)
#     res = []
#     for word in wordlist:
#         result = []
#         for file in files:
#             path = p + "/" + file
#             result.append(count.delay(word, path))

#         c = 0
#         for i in range(len(result)):
#             c += result[i].get()
#         res.append({word: c})
#     return jsonify(result=res)

if __name__ == '__main__':
    app.run(debug = True)