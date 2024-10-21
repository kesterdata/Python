"""
For loops are used to iterate (loop over ) all elements in 
a container(A container can be a list of values, a string of characters, rand of numbers)
one at a time. They are also used for counting.


"""
"""
name = [12,12,10,29,47,]

for c in name:
    print(c)
    """
"""
fruits = ["apple","banana","mango"]
for f in fruits:
    print(f.capitalize())
"""
#multiplication
"""u = 3
numbers = [1,2,3,4,5,6,7,8]
for n in numbers:
    print(f"{u} * {n}= {n*3}")

"""
"""
numbers = [1,2,3,4,5,6,7,8]

for n in numbers:
    if n%2 == 1:
        print(f"{n}this is an odd number")
    else:
        print(f"{n} this is an even number")
"""
"""
students = {"name" : "Samuel","age":20, "class" : "ss3"}

for s in students.keys():
    print(s)
"""
"""
students = {"name" : "Samuel","age":20, "class" : "ss3"}

for s,r in students.items():
    print(s,r)

    """

"""
The range() Function
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
 and ends at a specified number.

Example
Using the range() function:

for x in range(6):
  print(x)


"""
"""
for n in range(20):
    print("kester")
    """
"""
li=["kester","AY","kaybee","Samuel","Mac"]
for i in range(len(li)):
    print(li[i])
    """

"""
1. Use a for loop to print the individual element in each list 
2. usse a for loop and print the name 'Samual' 15 times
3. use a for loop and print statement 20 times


"""

students = ["kester","AY","kaybee","Samuel","Mac"]
scores = [98,92,90,89,50]
statment = "I am running"


for n in range(len(students)):
    print(students[n])
for i in range(len(scores)):
    print(scores[n])

for y in range(15):
    print(students[3])

for y in range(20):
    print(statment)
