#Dictionary
#A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.


#List:          is a collection which is ordered and changeable. Allows duplicate members.
#Tuple:         is a collection which is ordered and unchangeable. Allows duplicate members.
#Set:           is a collection which is unordered and unindexed. No duplicate members.
#Dictionary:    is a collection which is unordered, changeable and indexed. No duplicate members.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)


for x in thisdict:
  print(x)

for x in thisdict.values():
  print(x)


for x, y in thisdict.items():
  print(x, y)


'''
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()  	Returns a dictionary with the specified keys and values
get()	        Returns the value of the specified key
items()	        Returns a list containing the a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary

'''