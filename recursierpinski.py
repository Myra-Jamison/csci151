import sys
import stdio
import stddraw
import math

def createDaughters(x,y,k):
    ([x1],[y1]) = daugterTriangle1(x,y)
    ([x2],[y2]) = daugterTriangle2(x,y)
    ([x3],[y3]) = daugterTriangle3(x,y)
    stddraw.polygon([x1],[y1])
    stddraw.polygon([x2],[y2])
    stddraw.polygon([x3],[y3])
    while k > 0:
        k = k-1
        createDaughters([x1],[y1],k)
        createDaughters([x2],[y2],k)
        createDaughters([x3],[y3],k)
    return 
    
def daugterTriangle1(x,y):
    (x1,x2,x3) = x
    (y1,y2,y3) = y
    length = (x3-x1)/2
    t1x1 = x1*0.5
    t1x2 = x1
    t1x3 = x1 + x1*0.5
    t1y1 = math.sin(math.pi/3)*length
    t1y2 = y2
    t1y3 = math.sin(math.pi/3)*length
    return ([t1x1,t1x2,t1x3], [t1y1,t1y2,t1y3]) #stddraw.polygon([t1x1,t1x2,t1x3], [t1y1,t1y2,t1y3])

def daugterTriangle2(x,y):
    (x1,x2,x3) = x
    (y1,y2,y3) = y
    length = (x3-x1)/2
    t2x1 = x2 + x1*0.5
    t2x2 = x2 + x1
    t2x3 = x2 + x1*1.5
    t2y1 = math.sin(math.pi/3)*length
    t2y2 = y2
    t2y3 = math.sin(math.pi/3)*length
    return ([t2x1,t2x2,t2x3], [t2y1,t2y2,t2y3]) #stddraw.polygon([t2x1,t2x2,t2x3], [t2y1,t2y2,t2y3])

def daugterTriangle3(x,y):
    (x1,x2,x3) = x
    (y1,y2,y3) = y
    length = (x3-x1)/2
    t3x1 = x1 + x1*0.5
    t3x2 = x2
    t3x3 = x2 + 0.5*x1
    t3y1 = math.sin(math.pi/3)*length*3
    t3y2 = y1
    t3y3 = math.sin(math.pi/3)*length*3
    return ([t3x1,t3x2,t3x3], [t3y1,t3y2,t3y3]) #stddraw.polygon([t3x1,t3x2,t3x3], [t3y1,t3y2,t3y3])

#create a big canvas
stddraw.setXscale(0,1)
stddraw.setYscale(0,1)
stddraw.setCanvasSize(w=1000,h=1000)

#draw first two triangles; one as seed, and one as the boundary of the fractal
#stddraw.polygon([0,1,0],[0,(0.75)**0.5,0]) #boundary

#seed
x = [0.25,0.5,0.75]
y = [math.tan(math.pi/3)*0.25,0,math.tan(math.pi/3)*0.25]

stddraw.polygon(x,y)
createDaughters(x,y,4)
stddraw.show()


