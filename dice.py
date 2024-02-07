#----------------
# Boys and Girls Assignment
# ----------------
# Myra Jamison, Jan 31, CSCI151

import stdio
import sys
import stdarray
import random


#create empty array for the results, gather user input
diceResults = stdarray.create1D(12, value=0)
trials = int(sys.argv[1])

#provided script describing the probabilities of two dice
probabilities = stdarray.create1D(13, 0.0)
for i in range(1, 7):
    for j in range(1, 7):
        probabilities[i+j] += 1.0
probabilitiesPercent = [k/36 for k in probabilities]

#simulate rolling of dice and check against probabilities
for k in range(trials):
    roll = random.random()
    count = 0
    percentTracker = list()
    for j in probabilitiesPercent[2:13]:
        count += 1
        percentTracker.append(j)
        if roll < sum(percentTracker):
            diceResults[count] += 1
            break

stdio.write(diceResults)


