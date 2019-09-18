#Tuple
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

#Method	Description
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found


thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#throw error as a tuple is unchangeable
#thistuple[1] = "blackcurrant"
#print(thistuple)

'''
Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, 
change the list, and convert the list back into a tuple.
'''
x = ("apple", "banana", "cherry")
y = list(x)  #covert a tuple to a list
y[1] = "kiwi" 
x = tuple(y)

print(x)

#Tuple
temps = (("Berlin",29),("Cairo",36),("Buenos Aires",19),("Los Angeles",26),("Tokyo",27),("New York",28))
print(type(temps))
print(temps[0])

for i in temps:
    print(i[1])

import timeit
list_test = timeit.timeit(stmt="[1,2,3,4,5]",number = 1000000)
tuple_test = timeit.timeit(stmt="[1,2,3,4,5]",number = 1000000)

print("list time:",list_test)
print("tuple time:",tuple_test)