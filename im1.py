#------------------------------------------
# Assignment 11a, part 1
# -------------------------------------
# Myra Jamison, April 5

#this script creates a histogram of the intensities of a color image

#import packages
import stddraw
import pygame
import stdarray

#import picture from local directory
pic = pygame.image.load('/home/myra/Documents/csci151/mandrill.jpg')

#create some empty lists/arrays for future use
listOfIntensities = list()
frequencyIntensity = stdarray.create1D(256, 0)

#iterate over each pixel of the image, calculate the color > grayscale value > intensity and adds final intensity to list
for x in range(pic.get_width()):
    for y in range(pic.get_height()):
        colorPixel = pic.get_at((x,y))
        grayPixel = tuple(colorPixel.grayscale())
        listOfIntensities.append(grayPixel[0])

#take list of values and iterate through them, counting to create a frequency array
for i in listOfIntensities:
    frequencyIntensity[i] += 1
print(frequencyIntensity)

#set parameters for drawing, then draw a histogram using filled rectangles of height equal to frequency of intensity
stddraw.setYscale(0,1200)
stddraw.setXscale(0,270)
count = 0
for j in frequencyIntensity:
    stddraw.filledRectangle(count,1,0.9,j)
    count += 1
stddraw.show()
