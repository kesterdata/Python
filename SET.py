
"""SET

A set is a collection which is unordered, unchangeable*, and unindexed.


* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.
"""

#Example
#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)


#ADD ITEMS IN SET


my_set ={"python","java","R"}

my_set.add("JS")

print(my_set)

"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Duplicates Not Allowed
Sets cannot have two items with the same value.
"""

#Example
#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


#CLASS WORK

#sets

#create a set"unique_numbers" that contains the integers 1,2,3,4,5
unique_numbers = {1,2,3,4,5}

#add number 6 to the unique_numbers
unique_numbers.add(6)
print(unique_numbers)

#print the length of the unique_numbers
print(len(unique_numbers))

#try to add a duplicare number and see what happens
unique_numbers.add(5)
print(unique_numbers)