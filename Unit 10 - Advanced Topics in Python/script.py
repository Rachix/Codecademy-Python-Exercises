ITERATION NATION
1. Iterators for Dictionaries

my_dict = {
    "Name": "Rachith",
    "Age": 23,
    "RDBMS": True
}

print my_dict.items()

2. keys() and values()

my_dict = {
    "Name": "Rachith",
    "Age": 23,
    "RDBMS": True
}

print my_dict.keys()
print my_dict.values()

3. The 'in' Operator

my_dict = {
    "Name": "Rachith",
    "Age": 23,
    "RDBMS": True
}

print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print str(key),str(my_dict[key])

LIST COMPREHENSIONS
4. Building Lists

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

5. List Comprehension Syntax

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [4, 16, 36, 64, 100]

print even_squares

6. Now You Try!

cubes_by_four = [ x ** 3 for x in range(1,11) if x ** 3 % 4 == 0 ]
print cubes_by_four

LIST SLICING
7. 

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

8. Omitting Indices

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]

9. Reversing a List

my_list = range(1, 11)

# Add your code below!
backwards =  my_list[::-1]
print backwards

10. Stride Length

to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[100::-10]
print backwards_by_tens

11. Practice Makes Perfect

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

print to_21
print odds
print middle_third

LAMBDAS
12. Anonymous Functions

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

13. Lambda Syntax

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

14. Try It!

squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >= 30 and x <= 70, squares)

REVIEW
15. Iterating Over Dictionaries

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print movies.items()

16. Comprehending Comprehensions

threes_and_fives = [x for x in range(1,16) if ((x % 3 == 0) or (x % 5 == 0))]
print threes_and_fives

17. List Slicing

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = filter(lambda x: x != "X", garbled[::-1]) 
print message

18. Lambda Expressions

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message
