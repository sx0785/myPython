#Set
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

#List:          is a collection which is ordered and changeable. Allows duplicate members.
#Tuple:         is a collection which is ordered and unchangeable. Allows duplicate members.
#Set:           is a collection which is unordered and unindexed. No duplicate members.
#Dictionary:    is a collection which is unordered, changeable and indexed. No duplicate members.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Throw error as no unordered
#thisset[0]


'''
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	                        Description
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others

'''

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)