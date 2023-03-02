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

pi_float=float(pi_string)                   str 
                                            string<------>float dönüsümü
                                            print
                                            

#print("i fixed this") :==)
"""
