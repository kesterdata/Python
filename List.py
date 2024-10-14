""" LIST: A list a collection of ordered and changeable items.

SYNTAX =  [ ] OR use list 

"""
#PRACTICES: 


students = ["Samuel","Mac", "Kaybee", "AY","Kester"]
print(students)

students = ["Samuel","Mac", "Kaybee", "AY","Kester"]
print(students[4])

A list can store all data types

items = ["Samuel","Mac", "Kaybee", "AY","Kester",1,2,5.5,]
print(students[4])

A list can be stored inside a list 

items = ["Samuel","Mac", "Kaybee", "AY","Kester",1,2,5.5, [1,3,5]]
print(items[4])



items = ["Chicken Republic","Kilimanjaro", "KFC", "Tastia",4,65,80,["Victor",30,[20,30,[100,200,300]]]]
print(items[3], items[7][2][2][2])


OR 

items = ["Chicken Republic","Kilimanjaro", "KFC", "Tastia",4,65,80,["Victor",30,[20,30,[100,200,300]]]]
print(items[3])
print(items[7][2][2][2])

"""
LIST SLICING 


List slicing in Python is a technique used to access a specified portion or subset of a list. You can use both positive and negative indexes to create slices. 

The basic syntax is list[start:end], where start is the index to begin slicing (inclusive) and end is the index to stop slicing (exclusive). This allows you to retrieve a portion of the list without modifying the original list.

"""

#EXAMPLE 

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[2:7])

my_lis= [1,2,3,4,5,6,7,8,9,10]
print(my_list[7:])

"""
Steps in list 

Step determines the interval of elements to include. For example, my_list[::2] will return every second element from the list.

"""

my_list= [1,2,3,4,5,6,7,8,9,10]
print(my_list[2:9:2])

my_list= [1,2,3,4,5,6,7,8,9,10]
print(my_list[2:9:2])


"""Indexing from backward(Descending)"""

my_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(my_list[13:8:-2])



#Append Items
#To add an item to the end of the list

my_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
my_list.append(16)
print(my_list)


#Remove Specified Item
##The remove() method removes the specified item.

my_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
my_list.remove(8)
print(my_list)


#pop()  - Removes the element at the specified position

my_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
my_list.pop()
print(my_list)

#count() - Returns the number of elements with the specified value

my_list= [1,2,2,2,2,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(my_list.count(2))

#sort()- Sorts the list


my_list= [1,2,2,2,2,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

my_list.sort()
print(my_list)




#EXERCISE

my_list= [1,4,3,20,6,7,9,10,14,2,1,2]

print(my_list.count(2))

print(my_list.index(14))

my_list.pop()
print(my_list)

my_list.remove(9)
print(my_list)

my_list.sort()
print(my_list)

size = len(my_list)
print(size)