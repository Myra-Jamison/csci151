#----------------
# Random Integer Generator (assignment 6)
# ----------------
# Myra Jamison, February 19, CSCI151

#writes to stdout a sequence of integers, ready for tenperline.py filter to read and print

import stdio
import random
import sys

m = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(n):
    randomNum = random.randint(0, m-1)
    stdio.writeln(randomNum)