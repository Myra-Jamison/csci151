import sys
import stddraw
import stdarray

#define functions
def short(x):
    stddraw.filledRectangle(x,0,0.2,0.5)

def tall(x):
    stddraw.filledRectangle(x,0,0.2,1)
    
def drawbar(totalCode):
    tall(0)
    x = 0.3
    for i in totalCode:
        if i == 's':
            short(x)
        if i == 't':
            tall(x)
        x += 0.3
    tall(x)

def codeGen(num):
    totalCode = ''
    for i in str(num):
        totalCode += codes[int(i)]
    return totalCode

#create variables
codes = stdarray.create1D(10,'')
codes = ['ttsss','ssstt','sstst','sstts','stsst','ststs','sttss',
         'tssst','tssts','tstss']

input = str(sys.argv[1])
input = input.replace('-','')

#plotting
if len(input) == 5:
    stddraw.setXscale(0,8.1)
elif len(input) == 9:
    stddraw.setXscale(0,14.1)
else: stddraw.setXscale(0,20)
stddraw.setYscale(0,1.5)


drawbar(codeGen(input))
stddraw.show()