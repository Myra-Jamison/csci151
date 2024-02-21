#----------------
# Longest Run
# ----------------
# Myra Jamison, February 19, CSCI151

#read a sequence of integers from standard input, then calculate the longest
#consecutive run of the same integer

import stdio
import stdarray

#read stdin
input = list(stdio.readAllInts())

#make an array to store results in, then calculate consecutive runs
storedResults = stdarray.create1D((max(input)+1),1)
count = 0
currentLength = 1
for i in input:
    if input[count] == input[count-1] and count != 0:
        currentLength += 1
        if currentLength >= storedResults[i]:
            storedResults[i] = currentLength
    else: currentLength = 1
    count += 1

#find value and length of longest consecutive run
length = max(storedResults)
value = storedResults.index(length)

#write results to stdout
stdio.write('Longest Run: ' + str(length) + ' consecutive ' + str(value) +'s')
