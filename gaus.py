#----------------------------
# Assignment 8
# --------------------------
# Myra Jamison, March 30, CSCI 151

#this script generates numbers according to a gaussian distribution, then creates a histogram
#using those numbers

import sys
import stdarray
import random
import math
import stddraw

#get command line input, create array for later
n = int(sys.argv[1])
nStore = stdarray.create1D(20,0)

#trish's gaussian generator
def gaussian():
    r = 0.0
    while (r >= 1.0) or (r == 0.0):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        r = x*x + y*y
    return x * math.sqrt(-2.0 * math.log(r) / r)

#iteratively generate numbers and check to see if they meet the requirements specified in the assignment
for i in range(n):
    randomValue = gaussian()
    for j in range(20):
        if j*0.05 <= randomValue <= (j+1)*0.05:
            nStore[j] += 1
            continue
        else: continue

#print a histogram showing the occurence of numbers, binned into 0.05 sized bins
stddraw.setYscale(0,n)
stddraw.setXscale(0,20)
count = 0
for j in nStore:
    stddraw.filledRectangle(count,1,0.9,j)
    count += 1
stddraw.show()

#the bell curve is chopped in half because the assignment specified to check only positive numbers,
#while the script to generate numbers includes negative numbers as well
