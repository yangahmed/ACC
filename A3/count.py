from tasks import count, add
import os

path = '/home/ubuntu/datadisk/data'
word = 'han'
files= os.listdir(path)

# count = 0
for file in files:
    f = open(path+"/"+file)
    result = count.delay(word, f)