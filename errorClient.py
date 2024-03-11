# -------------------------------------
# Assignment 9, Module
# -------------------------------------
# Myra Jamison, CSCI 151, March 10 2024

import toErrIsPythonic
import sys
import stdio

# Problem Statement:
# Myra often measures haphazardly when making her special
# popcorn seasoning. her measurements usually consist of 1 tbsp of
# salt and 3 tbsp of nutritional yeast, +/- 0.5 tbsp and 1 tbsp, respectively.
# Determine the total amount of uncertainty in her seasoning.

    # bash command:
    # $ cd (directory with both module and this test client)
    # $ python3 errorClient.py 1 0.5 3 1

popcornSeasoningUncertainty = toErrIsPythonic.additive(
    sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

stdio.writeln("Popcorn Seasoning (tbsp): "+popcornSeasoningUncertainty)

# Problem Statement:
# Last month, Myra's landlady promised to fix the hole in her wall 
# in 7 days. Instead, it took 14, indicating an error of at least 
# +/- 7 days. For every day the hole existed, cold air entering the
# house increased Myra's gas bill by $5.00 +/- $0.10, given variability
# in the temperature, gas heater draw, and meter measurement. Find how
# much money Myra would lose in gas costs if another hole had to be
# repaired and the landlady promised to fix it in 3 days time.

    # bash command:
    # $ cd (directory with both module and this test client)
    # $ python3 errorClient.py 3 7 5 0.1

myraGasCostUncertainty = toErrIsPythonic.multiplicative(
    sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

stdio.writeln("Gas Cost (dollars): "+myraGasCostUncertainty)


