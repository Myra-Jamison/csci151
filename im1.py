import stddraw
import pygame
import stdarray

pic = pygame.image.load('/home/myra/Documents/csci151/mandrill.jpg')

listOfIntensities = list()
frequencyIntensity = stdarray.create1D(256, 0)

for x in range(pic.get_width()):
    for y in range(pic.get_height()):
        colorPixel = pic.get_at((x,y))
        grayPixel = tuple(colorPixel.grayscale())
        print(grayPixel)
        listOfIntensities.append(grayPixel[0])

count = 0
for i in listOfIntensities:
    frequencyIntensity[i] += 1
print(frequencyIntensity)

stddraw.setYscale(0,1200)
stddraw.setXscale(0,270)
for j in frequencyIntensity:
    stddraw.filledRectangle(count,1,0.9,j)
    count += 1


stddraw.show()
