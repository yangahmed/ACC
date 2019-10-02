from tasks import count, sum
import os

p = '/home/ubuntu/data'
word = 'han'
# files= os.listdir(p)

# for file in files:
#     path = p + "/" + file
#     result = count.delay(word, path)

tasks.sum.delay(word, path)