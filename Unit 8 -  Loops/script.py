WHILE LOOPS
1. While you're here

count = 0

if count < 10:
    print "Hello, I am an if statement and count is", count
    
while count < 10:
    print "Hello, I am a while and count is", count
    count += 1

2. Condition

loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False

3. While you're at it

num = 1

while num <= 10:  # Fill in the condition
    print num ** 2 # Print num squared
    num = num + 1 # Increment num (make sure to do this!)

4. Simple errors

choice = raw_input('Enjoying the course? (y/n)')
y="y"
n="n"
while choice != y and choice!=n:  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

5. Infinite loops

count = 0

while count < 10: # Add a colon
    print count
    count += 1# Increment count

6. Break

count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break

7. While / else

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

8. Your own while / else 

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
while guesses_left>0:
    guess=int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left -= 1
else:
    print "You lose"

FOR LOOPS
9. For your health

print "Counting..."

for i in range(20):
    print i
    
10. For your hobbies

hobbies = []

# Add your code below!
for x in range(3):
    hobby = raw_input("Whats your hobby?")
    hobbies[x] = hobbies.append(hobby)

11. For your strings

thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!

for i in word:
  print i

12. For your A

phrase = "A bird in the hand..."
# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
      
       print 'X',
    else:
       
       print char, 
#Don't delete this print statement!
print

13. For your lists

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!
for num in numbers:
    print num**2

STEP UP YOUR 'FOR'S
14. Looping over a dictionary

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key, d[key]

15. Counting as you go

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item

16. Multiple lists

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here![TAB] If b > a:
    if b > a:
        print b
    elif a > b:
        print a

17. For / else

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

18. Change it up

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        
    print 'A', f
else:
    print 'A fine selection of fruits!'

19. Create your own

for num in numbers:
    if num == 1:
        print num
    else:
        print num**2





