INTRODUCTION TO CONTROL FLOW
1. Go With the Flow

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

COMPARATORS
2. Compare Closely!

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three =  True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

3. Compare... Closelier!

# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

4. How the Tables Have Turned

# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 4 < 2

# Make me true!
bool_three = 5 > 1

# Make me false!
bool_four = 10 <= 1

# Make me true!
bool_five = 7 >= 5

BOOLEAN OPERATORS
5. To Be and/or Not to Be

"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""
6. And

bool_one = False

bool_two = False 

bool_three = False 

bool_four = True

bool_five = True

7. Or

bool_one = True

bool_two = True

bool_three = False

bool_four = True

bool_five = False

8. Not 

bool_one = not True

bool_two = not False

bool_three = not False

bool_four = not False

bool_five = not not False

9. This and That (or This, But Not That!)

bool_one = False

bool_two = True

bool_three = True

bool_four = True

bool_five = False

10. Mix 'n' Match

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = (4 <= 4) and "Police" == "Police"

# Make me false!
bool_three =  (3 < 1) or "If" == "of"

# Make me true!
bool_four = ( 10 <= 10 ) and ( 2<=2 )

# Make me true!
bool_five = (16 < 17) and ( 45 >= 45 ) 

IF, ELSE AND ELIF
11. Conditional Statement Syntax

response = 'Y'

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

12. If You're Having...

def using_control_once():
    if 2 == 2:
        return "Success #1"

def using_control_again():
    if 4 > 2:
        return "Success #2"

print using_control_once()
print using_control_again()

13. Else Problems, I Feel Bad for You, Son...

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False     # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False

14. I Got 99 Problems, But a Switch Ain't One

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

REVIEW
15. The Big if

# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if "elephant" == "elephant":    # Start coding here!
            # Don't forget to indent
            return True# the code inside this block!
    elif "elephant" != "flying":
            # Keep going here.
            return False # You'll want to add the else statemen, too!
    else:
            return False          















