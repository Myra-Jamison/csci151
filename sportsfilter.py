#--------------------------------
# Caitlin Clark Data Reader: Assignment 11
# -------------------------------------
# Myra Jamison (Late)
# CSCI 151

import sys
import stdarray
from instream import InStream
from outstream import OutStream

#this program reads data from a .csv file and then
#writes it and formats it into tabular form in a .txt file

#-----------------------------------------------------------

#pull data from a .csv file in pwd given as
#command line argument
dataIn = InStream(sys.argv[1])

#create an array for data permutation
array = stdarray.create2D(6, 26, '')

#read through standard input and write the data to 
#our array. because this is a csv and comma delineated,
#we simply switch to the next element when a comma is
#read in and don't record it to the array.
rowcount = 0
colcount = 0
for j in range(6):
    for i in dataIn.readLine():
        if i != ',':
            array[rowcount][colcount] += i
        if i == ',':
            colcount += 1
    colcount = 0
    rowcount += 1

#here, the output data file is created
dataOut = OutStream('clarkout.txt')

#format the data: here, we iterate through our array
#and write it to the file. line breaks are accounted for
#by using a 2d array. also, there's a little bit of janky
#code using f strings to make sure the spacing is as Trish wanted.
#the buffer is the spacing for each column essentially
for i in range(6):
    for j in range(26):
        if j < 5:
            buffer = '>20s'
        else: buffer = '>8s'
        dataOut.write(f'{str(array[i][j]):{buffer}}')
    dataOut.write('\n')

#an output file clarkout.txt will be created in the present
#working directory

#-----------------------------------------------------------
#to run this script in bash shell:

# $ cd present/working/directory
# $ python3 sportsfilter.py NAMEOFCSV.csv
# $ cat clarkout.txt