#----------------
# Boys and Girls Assignment
# ----------------
# Myra Jamison, Jan 31, CSCI151

import stdio
import sys
import stdarray
import statistics
import random

#create initial lists, grab user input for amount of trials
storedChildren = list()
frequencyArray = stdarray.create1D(50,0)
trials = int(sys.argv[1])

#simulate n amount of trials of how many children must be born to have at least 2 of each gender
for i in range(trials):   
    while len(storedChildren) == 0 or type(statistics.mean(storedChildren)) == int:
        storedChildren.append(random.randint(0,1))
        childNumber = len(storedChildren)
    frequencyArray[childNumber] +=1
    storedChildren = list()

#output data
stdio.write('Trials with 2 children: ' + str(frequencyArray[3]) + '\n' +
            'Trials with 3 children: ' + str(frequencyArray[4]) + '\n' +
            'Trials with 4 children: ' + str(frequencyArray[5]) + '\n' +
            'Trial with 5 children: ' + str(frequencyArray[6]) +'\n')