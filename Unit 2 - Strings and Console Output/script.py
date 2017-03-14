Strings & Console Output
1. Strings

# Set the variable brian on line 3!
brian = "Hello life!"

2. Practice

# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"

# Put your variables above this line

print caesar
print praline
print viking

3. Escaping characters

# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'

4. Access by Index

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print fifth_letter

STRING METHODS
5. String methods

parrot = "Norwegian Blue"
len(parrot)
print len(parrot)

6. lower()

parrot = "Norwegian Blue"
parrot = "Norwegian Blue".lower()
print parrot

7. upper()

parrot = "norwegian blue"
parrot = "norwegian blue".upper()
print parrot

8. str()

"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)

9. Dot Notation

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

PRINT
10. Printing Strings

"""Tell Python to print "Monty Python"
to the console on line 4!"""

print "Monty Python"

11. Printing Variables

"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print the_machine_goes

ADVANCED PRINTING
12. String Concatenation

# Print the concatenation of "Spam and eggs" on line 3!

print "Spam " + "and " + "eggs"

13. Explicit String Conversion

# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)

14. String Formatting with %, Part 1

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

15. String Formatting with %, Part 2

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

REVIEW
16. And Now, For Something Completely Familiar

# Write your code below, starting on line 3!
my_string = "Monty Python"
print len(my_string)
print my_string.upper()










