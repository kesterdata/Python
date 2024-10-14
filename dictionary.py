"""
Dictionary

Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values: { }
"""

#EXAMPLE:  Create and print a dictionary:

student_info = {"Student_name": "David Amadi", "age":20, "class":"ss1"}
print(student_info["Student_name"])

student_two = {"Student_name" : "Kester Eke", "age":25, "class": "ss3"}
print(student_two["Student_name"])
print(student_two["age"])
print(student_two["class"])


# keys() in DICTIONARY 

#Returns a list containing the dictionary's keys

print(student_one.keys())


#Python Dictionary values() Method

""" The values() method returns a view object. The view object contains the values of the dictionary, as a list.
The view object will reflect any changes done to the dictionary, see example below.


Syntax
dictionary.values()
"""


""" Removing Items
There are several methods to remove items from a dictionary:

Example
The pop() method removes the item with the specified key name:
"""

thisdict = {"brand": "Ford", "model": "Mustang","year": 1964
}

thisdict.pop("model")
print(thisdict)


"""
UPDATE 

Update is used to add, update , or merge and existing dictionary from another dictionary 
"""

my_dictionary ={"knowledge": "Data science","tool":"python","year":2020}
second_dict ={"Database": "POSTGRESQL", "tool":"Java"}

my_dictionary.update(second_dict)

print(my_dictionary)