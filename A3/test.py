from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

p = '/home/ubuntu/data'
# word = 'han'

@app.route('/count', methods=['GET'])
def count_word():
    # files= os.listdir(p)
    # result = []
    # for file in files:
    #     path = p + "/" + file
    #     result.append(count.delay(word, path))

    # c = 0
    # for i in range(len(result)):
    #     c += result[i].get()

    # print(c)
    words = request.args.get("words")
    wordlist = words.split(',')
    res = []
    for word in wordlist:
        c=1
        res.append({word: c})
    return jsonify(result=res)
    # return wordlist[0]

if __name__ == '__main__':
    app.run()