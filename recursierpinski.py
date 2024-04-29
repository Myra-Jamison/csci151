#-------------------------------------------
# Assignment 10: Recursive Triangle Generator
#------------------------------------------
# Myra Jamison (Late)
# CSCI 151

import stddraw
import math
import sys
import stdio

#this script generates sierpinski fractals of a degree given by command
#line input, and writes them to standard output

#--------------------------------------------------------------------

#given two lists containing the coordinates of the points of
#a triangle in form [x1,x2,x3] and [y1,y2,y3], calculate the
#'daughter triangles' that would be created in step n+1
#(note: there are more optimized ways for python to do this, 
#this is just how I calculated it myself)

def daughterTriangles(x,y):
    (x1,x2,x3) = x
    (y1,y2,y3) = y
    length = x3-(x3+x1)/2
    #
    t1x1 = x1-(0.5*length)
    t1x2 = x1
    t1x3 = (x1+x2)/2
    t1y1 = y2 + math.sin(math.pi/3)*length
    t1y2 = y2
    t1y3 = y2 + math.sin(math.pi/3)*length
    results1 = [t1x1,t1x2,t1x3], [t1y1,t1y2,t1y3]
    #
    t2x1 = x1+(0.5*length)
    t2x2 = x2
    t2x3 = (x2 + x3)/2
    t2y1 = y1+math.sin(math.pi/3)*(length)
    t2y2 = y1
    t2y3 = y1+math.sin(math.pi/3)*(length)
    results2 = [t2x1,t2x2,t2x3], [t2y1,t2y2,t2y3]
    #
    t3x1 = (x2 + x3)/2
    t3x2 = x3
    t3x3 = x3+(0.5*length)
    t3y1 = y2 + math.sin(math.pi/3)*length
    t3y2 = y2
    t3y3 = y2 + math.sin(math.pi/3)*length
    results3 = [t3x1,t3x2,t3x3], [t3y1,t3y2,t3y3]
    #
    results = [results1, results2, results3]
    return results

#now use the above function to recursively generate and draw
#the triangles of each step for k amount of steps. check edge cases
#where the user has requested no recursion or a negative amount of steps

def createDaughters(x,y,k):
    if k == 0:
        stddraw.polygon(x,y)
        return
    if k < 0:
        return stdio.write('The designer of this script neither had ' +
                    'the time nor willpower to consider complex ' +
                    'numbers. Please choose a positive integer.\n')
    for i in daughterTriangles(x,y):
        for (a,b) in [i]:
            stddraw.polygon(a,b)
            if k > 1:
               createDaughters(a,b,k-1)
    return

#---------------------------------------------------------------------

#create a seed for x,y (these can be anything, this just fits the default
#canvas well) and k from command line input. then execute.
#~~~~~seeds~~~
x = [0.25,0.5,0.75]
y = [math.tan(math.pi/3)*0.25,0,math.tan(math.pi/3)*0.25]
k = int(sys.argv[1])
#~~~~~~~~~~~~~
stddraw.polygon(x,y)
createDaughters(x,y,k)
stddraw.show()