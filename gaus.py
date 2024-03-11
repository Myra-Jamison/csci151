import sys
import stdarray
import random

n = 400

nStore = stdarray.create1D(20,0)
for i in range(int(n)):
    j = 0
    randomValue = random.random()
    while j*0.05 > randomValue > (j+1)*0.05:
        j += 1
    for k in range(j):
        nStore[k] += 1

print(nStore)
