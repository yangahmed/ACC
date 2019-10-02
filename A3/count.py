from tasks import count
import os

p = '/home/ubuntu/data'
word = 'han'
files= os.listdir(p)

result = []
for file in files:
    path = p + "/" + file
    result.append(count.delay(word, path))

c = 0
for i in range(len(result)):
    c += result[i].get()

print(c)
