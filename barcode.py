#----------------
# Postal Barcode (assignment 8a)
# ----------------
# Myra Jamison, February 23, CSCI151

#draw to stdout a barcode using the USPS barcode system for
#a given 5 or 9 digit zipcode

#imports
import sys
import stddraw
import stdarray

#define functions to draw bars of two lengths
def short(x):
    stddraw.filledRectangle(x,0,0.2,0.5)
def tall(x):
    stddraw.filledRectangle(x,0,0.2,1)

#defining function to draw barcode
def drawbarcode(stri):
    tall(0)
    x = 0.3
    for i in stri:
        if i == 's':
            short(x)
        if i == 't':
            tall(x)
        x += 0.3
    tall(x)

#creating a function to encode zip codes as strings of two values
def codeGen(num):
    zipEncoded = ''
    for i in str(num):
        zipEncoded += codes[int(i)]
    return zipEncoded

#creating checksum and returning its encoded string
def checksum(num):
    sumOfDigits = 0
    for i in str(num):
        sumOfDigits += int(i)
    return codes[sumOfDigits%10]

#encoding system
codes = stdarray.create1D(10,'')
codes = ['ttsss','ssstt','sstst','sstts','stsst','ststs','sttss',
         'tssst','tssts','tstss']

#stdin
input = sys.argv[1].replace('-','')

#stdout parameters
if len(input) == 5:
    stddraw.setXscale(0,9.6)
else: stddraw.setXscale(0,15.6)
stddraw.setYscale(0,1.1)

#calling functions to create stdout drawing
drawbarcode(codeGen(input) + checksum(input))
stddraw.show()