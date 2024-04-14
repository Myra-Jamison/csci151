#------------------------------------------
# Assignment 11a, part 3
# -------------------------------------
# Myra Jamison, April 5

#this script produces 3 rgb filtered images from a full color image

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

#import three copies of picture again, this time with a booksite module for printing
#with stddraw
pictR = picture.Picture(sys.argv[1])
pictG = picture.Picture(sys.argv[1])
pictB = picture.Picture(sys.argv[1])

#iterate through every row in the array. unpack color tuples and re-encode them in the color.Color class and as x and y
#coordinates. modify each picture to only be in red green or blue.
for i in range(len(array[:,0])):
    (r,g,b,a) = array[i,1]
    (x,y) = array[i,0]
    pictR.set(x,y,color.Color(r,0,0))
    pictG.set(x,y,color.Color(0,g,0))
    pictB.set(x,y,color.Color(0,0,b))

#draw the three pictures next to each other
stddraw.setCanvasSize(w=width*3,h=height)
stddraw.setYscale(0,height)
stddraw.setXscale(0,width*3)
stddraw.picture(pictR, width*0.5, height/2)
stddraw.picture(pictG, width*1.5, height/2)
stddraw.picture(pictB, width*2.5, height/2)
stddraw.show()