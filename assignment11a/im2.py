#------------------------------------------
# Assignment 11a, part 2
# -------------------------------------
# Myra Jamison, April 5

#this script flips an image 90 degrees

#import packages
import stddraw
import pygame
import numpy
import picture
import color
import sys

#import picture from command line input, find dimensions. we import as a pygame object
#because the data types provided by that package play friendlier with arrays
pic = pygame.image.load(sys.argv[1])
width = pic.get_width()
height = pic.get_height()

#create an empty array to store pixel color/location data
array = numpy.empty((height*width, 2), dtype=tuple)

#iterate over each pixel of the image, calculate the color and location, add to array
count = 0
for x in range(width):
    for y in range(height):
        colorPixel = pic.get_at((x,y))
        array[count, 0] = (x,y)
        array[count, 1] = tuple(colorPixel)
        count += 1      

#import the picture again, this time with a booksite module for printing
#with stddraw
pict = picture.Picture(sys.argv[1])
stddraw.setYscale(0,height)
stddraw.setXscale(0, width)

#iterate through every row in the array. unpack color tuples and re-encode them in the color.Color class and as x and y
#coordinates. apply an orthoganal transformation to x and y to rotate the image 90 degrees.
for i in range(len(array[:,0])):
    (r,g,b,a) = array[i,1]
    (x,y) = array[i,0]
    pict.set(y,x,color.Color(r,g,b))

#draw
stddraw.picture(pict)
stddraw.show()