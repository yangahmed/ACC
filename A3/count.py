from tasks import count
import os
from flask import Flask
app = Flask(__name__)

p = '/home/ubuntu/data'
# word = 'han'

@app.route('/count/<str:word>', methods=['GET'])
def count_word(word, p):
    files= os.listdir(p)
    result = []
    for file in files:
        path = p + "/" + file
        result.append(count.delay(word, path))

    c = 0
    for i in range(len(result)):
        c += result[i].get()

    print(c)

if __name__ == '__main__':
    app.run()