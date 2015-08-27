def power(base,exponent):  # Add your parameters here!
    result = base**exponent
    print("%d to the power of %d is %d." % (base, exponent, result))

power(2,3)  # Add your arguments here!

# function in function
def cube(number) :
    return number**3
def by_three(number) :
    if number % 3 == 0 :
        return cube(number)
    else :
        return False

tree_cube=by_three(3)
print(tree_cube)
"""
universal import
from math import *
"""
# generic import
from math import sqrt
print(sqrt(25))

# lists things from a module
import sys
everything = dir(sys)
print(everything)