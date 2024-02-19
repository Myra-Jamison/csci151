#----------------
# Circle assignment
# ----------------
# Myra Jamison, Feb 19th, CSCI151

import stdio
import stddraw
import stdarray
import sys
import random
import math

#description: draw n equidistant points along a line curve of a circle. connect points according to random probability, 
#making some connected and some not.

#user command line input
n = int(sys.argv[1])
p = float(sys.argv[2])

stddraw.setXscale(-1.2,1.2)
stddraw.setYscale(-1.2,1.2)

#array to store points in
pointCoords = stdarray.create2D(n, n, 0.0)

#calculations and drawingfor points
for i in range(n):
    pointCoords[i] = [
        math.cos((2*math.pi/n)*i),
        math.sin((2*math.pi/n)*i)] 
    stddraw.point(pointCoords[i][0],pointCoords[i][1])

#drawing lines
for j in range(n):
    for k in range(n):
        randomNum = random.random()
        if randomNum < p:
            stddraw.line(pointCoords[j][0], pointCoords[j][1], pointCoords[k][0], pointCoords[k][1])
            

#print plot
stddraw.show()