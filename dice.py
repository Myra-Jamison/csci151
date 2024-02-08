#----------------
# Dice assignment
# ----------------
# Myra Jamison, Feb 8th, CSCI151

import stdio
import sys
import stdarray
import random

#description: simulate the rolling of two 6-sided dice and the sum produced for n trials

#create empty array for the results, gather user input
diceResults = stdarray.create1D(12, value=0)
trials = int(sys.argv[1])
probabilitiesPercent = stdarray.create1D(11, value=0.0)


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
    for l in probabilitiesPercent[2:13]:
        count += 1
        percentTracker.append(l)
        if roll < sum(percentTracker):
            diceResults[count] += 1
            break

stdio.write(diceResults)

#confused about how lists are mutable vs immutable arrays produced by the booksite module... can
# we iterate over the booksite arrays?

#also, its a lot; to get our theoretical and experimental to match to 3 decimal places,
# approximately 10^6 trials are required
