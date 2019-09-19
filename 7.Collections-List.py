
'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

#List:          is a collection which is ordered and changeable. Allows duplicate members.
#Tuple:         is a collection which is ordered and unchangeable. Allows duplicate members.
#Set:           is a collection which is unordered and unindexed. No duplicate members.
#Dictionary:    is a collection which is unordered, changeable and indexed. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, a
nd, it could mean an increase in efficiency or security.

Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

'''
##########     List   ##########
thislist = ["watermelon","apple", "banana", "cherry"]
print(thislist)

thislist[1] = "blackcurrant"
print(thislist)

if "banana" in thislist:
    print("Yes, 'banana' is in the fruits list")

thislist.sort()
print(thislist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


temps = [("Berlin",29),("Cairo",36),("Buenos Aires",19),("Los Angeles",26),("Tokyo",27),("New York",28)]


print(dir(temps))