from tasks import count, add
import os

# path = '/home/ubuntu/data'
word = 'han'
# files= os.listdir(path)

# count = 0
# for file in files:
#     f = open(path+"/"+file)
#     result = count.delay(word, f)

data = open('data/4fe89313-8c7a-4c95-9b3b-155435d25c1a')
result = count.delay(word, data)