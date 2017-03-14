INTRODUCTION TO FUNCTIONS
1. What Good are Functions?

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

FUNCTION SYNTAX
2. Function Junction

# Define your spam function starting on line 5. You
# can leave the code on line 11 alone for now--we'll
# explain it soon!

def spam():
    """Prints 'Eggs!' to the console. """ 
    print "Eggs!"

# Define the spam function above this line.
spam()

3. Call and Response

def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)

4. Parameters and Arguments

def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!

5. Functions Calling Functions

def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2

6. Practice Makes Perfect

def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
        
7. I Know Kung Fu

# Ask Python to print sqrt(25) on line 3.

print sqrt(25)

8. Generic Imports

# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)

9. Function Imports
# Import *just* the sqrt function from math on line 3!

from math import sqrt

10. Universal Imports

# Import *everything* from the math module on line 3!

from math import *

11. Here Be Dragons

import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

BUILT-IN FUNCTIONS
12. On Beyond Strings

def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

13. max()

# Set maximum to the max value of any set of numbers on line 3!

maximum = max(45, 56)

print maximum

14. min()

# Set minimum to the min value of any set of numbers on line 3!

minimum = min(34,56)

print minimum

15. abs()

absolute = abs( -42 ) 
print absolute

16. type()

# Print out the types of an integer, a float,
# and a string on separate lines below.

print type(42)
print type('rach')
print type(4.5)

REVIEW
17. Review: Functions

def shut_down(s):
 
 if s == "yes":
    return "Shutting down"
 elif s == "no":
    return "Shutdown aborted"
 else:
    return "Sorry"

18. Review: Modules

from math import sqrt 
squared = sqrt(13689)
print squared

19. Review: Built-In Functions

def distance_from_zero(number):
    if type(number) == int or type(number) == float:
        return abs(number)
    else:
        return "Nope"
        
        














































