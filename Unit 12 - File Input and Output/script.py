INTRODUCTION TO FILE I/O
1. See It to Believe It

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

2. The open() Function

my_file = open("output.txt", "r+")

3. Writing

my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

# Add your code below!
for item in my_list:
    my_file.write("%s\n" % (item))

my_file.close()

4. Reading

my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

THE DEVIL'S IN THE DETAILS
5. Reading Between the Lines

f = open("text.txt", "w+")
f.write("Hello World!" + "\n")
f.write("Hello World!!" + "\n")
f.write("Hello World!!!" + "\n")
f.close()

my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

6. PSA: Buffering Data

# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")



# Try to read from the file
print read_file.read()

7. The 'with' and 'as' Keywords

with open("text.txt", "w") as textfile:
	textfile.write("Success!")

8. Try It Yourself

with open("text.txt","w") as my_file:
    my_file.write("Road To ~Sucess~")
print my_file

9. Case Closed?

with open("text.txt","w") as my_file:
    my_file.write("Road To ~Sucess~")
print my_file

if not my_file.closed:
    my_file.close()
print my_file.closed
