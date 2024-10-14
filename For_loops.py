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
#
for n in range(3,51):
    print(n)