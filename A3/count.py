from tasks import count, add
import os

path = ''
files= os.listdir(path)

count = 0
word = 'han'
for file in files:
    f = open(path+"/"+file)
    result = count.delay(word, f)