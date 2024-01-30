#----------------
# Palindrome Assignment
# ----------------
# Myra Jamison, Jan 29, CSCI151

import stdio
import sys
import string

# create a dictionary of punctuation using the string package plus a couple other important characters
# and create an empty list
punctuationDictionary = {string.punctuation, " ", "?"}
letters = list()

# allow user input
input = str(sys.argv[1])

# calculate if the word is a palindrome using a for loop
for i in range(0,len(input)):
    letters.append(input[i])
lettersBackwards = list(reversed(letters))
if lettersBackwards == letters:
    stdio.writeln(str(input) + " is a palindrome! ")
# consider that it may be an imperfect palindrome (see notes)
else:
    lettersLower = [j.lower() for j in letters]
    for k in lettersLower:
        if k in punctuationDictionary:
            lettersLower.remove(k)
    lettersLowerBackwards = list(reversed(lettersLower))
    if lettersLowerBackwards == lettersLower:
        stdio.write(str(input) + " is an imperfect palindrome. ")
# or that it is not a palindrome at all
    else: stdio.write(str(input) + " is not a palindrome. ")

# Notes ------------------------------
# testing for an imperfect palindrome involved me learning
# a little bit of list comprehension. I tried to do this with sets
# at first but i needed an ordered array to calculate the palindromes