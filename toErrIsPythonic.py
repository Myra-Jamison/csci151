# -------------------------------------
# Assignment 9, Module
# -------------------------------------
# Myra Jamison, CSCI 151, March 10 2024

"""
Welcome to toErrIsPythonic
Version 0.1
~~~~
This module delivers two functions which can be used to calculate
the total propogated error in results that are dependent on two
variables with known individual uncertainties. 
"""

import numpy as np
import stdio
import sys

# for results that rely on adding/subtracting two variables (A+B=C), we use the 
# formula sqrt(dA^2 + dB^2) = dC

def additive(A,dA,B,dB):
    """
    Use to calculate propogation of error in results that 
    rely on adding two variables A and B with known uncertainties
    dA and dB, respectively:

    toErrIsPythonic.additive(A,dA,B,dB)

    Returns C +/- dC for C = A + B
    """
    add_dC = (float(dA)**2 + float(dB)**2)**0.5
    add_C = float(A) + float(B)
    return "Total = "+str(add_C)+" +/- "+str(add_dC)

# for results that rely on multiplying/dividing two variables with exponents (A*B = C),
# we use the formula dc = |c|*sqrt([da/A]^2 + [db/B]^2)

def _ratioOfUncertainty(A,dA,B,dB): #private helper function
    ratioA = float(dA)/float(A)
    ratioB = float(dB)/float(B)
    return [ratioA,ratioB]

def multiplicative(A,dA,B,dB):
    """
    Use to calculate propogation of error in results 
    that rely on multiplying two variables A and B with known uncertainties
    dA and dB, respectively:

    toErrIsPythonic.multiplicative(A,dA,B,dB)

    Returns C +/- dC for C = A*B
    """
    squares = [i**2 for i in _ratioOfUncertainty(A,dA,B,dB)]
    mult_C = float(A)*float(B)
    mult_dC = abs(mult_C)*(sum(squares))**0.5
    return "Total = "+str(mult_C)+" +/- "+str(mult_dC)

#private test client, allow A, dA, B, and dB as command line arguments

def _main():
    a = sys.argv[1]
    dA = sys.argv[2]
    b = sys.argv[3]
    dB = sys.argv[4]
    return stdio.write("Additive: "+additive(a,dA,b,dB)+
                "\nMultiplicative: "+multiplicative(a,dA,b,dB))

if __name__ == "__main__": _main()