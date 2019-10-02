from tasks import count, add
import os

p = '/home/ubuntu/data'
word = 'han'
files= os.listdir(p)

# count = 0
for file in files:
    path = p + "/" + file
    result = count.delay(word, path)