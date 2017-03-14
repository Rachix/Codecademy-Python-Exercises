LIST RECAP
1. List accessing

n = [1, 3, 5]

# Add your code below
print n[1]

2. List element modification

n = [1, 3, 5]
# Do your multiplication here
n[1] = 3*5
print n

3. Appending to a list

n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print n

4. Removing elements from lists

n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
print n

FUNCTION RECAP
5. Changing the functionality of a function

number = 5

def my_function(x):
    return x * 3

print my_function(number)

6. More than one argument

m = 5
n = 13
# Add add_function here!
def add_function(m,n):
    return m + n
   
print add_function(m, n)

7. Strings in functions

n = "Waynes"
# Your function here!
def string_function(s):
    return s + "world"

print string_function(n)

INTRODUCTION TO USING FUNCTIONS WITH LISTS
8. Passing a list to a function

def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)

9. Using an element from a list in a function

def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)

10. Modifying an element of a list in a function

def list_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print list_function(n)

11. List manipulation in functions

n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst

print list_extender(n)

USING ENTIRE LIST IN THE FUNCTION
12. Printing out a list item by item in a function

x = [3, 5, 7]

for i in range(0, len(x)):
    print x[i]

def print_list(x):
    for number in x:
      print number

print_list(n)

13. Modifying each element in a list in a function

n = [3, 5, 7]

for i in range(0, len(n)):
    n[i] = n[i] * 2
# Don't forget to return your new list!
def double_list(x):
    for i in x:
            x[i] = x[i] * 2
            print i
    return x  
    print double_list(n)

14. Passing a range into a function

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) # Add your range between the parentheses!

15. Iterating over a list in a function

n = [3, 5, 7]


def total(x):
    result = 0
    
    for i in range(0, len(x)):
        result = result + x[i]
    return result
    
print total(n) 

16. Using strings in lists in functions

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for i in range(len(words)):
        result += words[i]
    return result

print join_strings(n)

USING LIST OF LISTS IN FUNCTION
17. Using two lists as two arguments in a function

m = [1, 2, 3]
n = [4, 5, 6]


# Add your code here!
def join_lists(x, y):
    return x + y
    
print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

18. Using a list of lists in a function

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    results = results + numbers
  return results

print flatten(n)

print flatten(n)















    
    
















































