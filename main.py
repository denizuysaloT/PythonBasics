"""
# This is a sample Python script.
#https://www.learnpython.org/
#https://app.datacamp.com/learn/career-tracks/data-scientist-with-python
#https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=3
#https://pythonexamples.org/

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#Python basics
#Burası tamamen bir deneme alanıdır. Pythonun temeli burada atılmaktadır.

#1
#print("This line will be printed.")
#2
#x = 1
#if x == 1:
    # indented four spaces
#    print("x is 1.")

#3
#myint = 7
#print(myint)

#4
#myfloat = 7.0
#print(myfloat)
#myfloat = float(7)
#print(myfloat)

#5
#mystring = 'hello'
#print(mystring)
#mystring = "hello"
#print(mystring)



print(type(x))
print(type(y))
print(type(z))

mystring='hello'
print(mystring)
mystring="hello"
print(mystring)
"""
"""
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
"""

"""
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)
"""
"""
myfamily = []
myfamily.append("umut")
myfamily.append("sema")
myfamily.append("cengiz")
myfamily.append("deniz")
print(myfamily[0])
print(myfamily[1])
print(myfamily[2])
for x in myfamily:
    print(x)
"""
"""
numbers = []
strings = []
names = ["Sema", "Deniz", "Umut", "Cengiz"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
"""
"""
# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100*1.1**7)
"""
"""
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7
# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string

pi_string = "3.1415926"

pi_float = float(pi_string)
"""

"""
#
 List of lists
As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

Instead of creating a flat list containing strings and floats, representing the names and areas of the rooms in your 
house, 
you can create a list of lists. The script in the editor can already give you an idea.

Don't get confused here: "hallway" is a string, while hall is a variable that represents the float 11.25 you specified 
earlier.
 
Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
Print out house; does this way of structuring your data make more sense?
Print out the type of house. Are you still dealing with a list?
  
 area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
"""
"""
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs=["hallway",11.25,"kitchen",18.0,"living room",20.0]
downstairs[1:5]

# Use slicing to create upstairs
upstairs=["bedroom",10.75,"bathroom",9.50]
upstairs[0:4]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
"""
"""
Inner workings of lists
At the end of the video, Hugo explained how Python lists work behind the scenes. In this exercise you'll get some 
hands-on experience with this.

The Python code in the script already creates a list with the name areas and a copy named areas_copy. Next, the first 
element in the areas_copy list is changed and the areas list is printed out. If you hit Run Code you'll see that, 
although you've changed areas_copy, the change also takes effect in the areas list. That's because areas and areas_copy 
point to the same list.

If you want to prevent changes in areas_copy from also taking effect in areas, you'll have to do a more explicit copy of 
the areas list. You can do this with list() or by using [:].

Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas. 
After your edit, changes made to areas_copy shouldn't affect areas. Submit the answer to check this.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
list(areas)
# Create areas_copy
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
"""
"""
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))
# Print out length of var1

print(len(var1))

# Convert var2 to an integer: out2
out2=int(var2)
"""
