
#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:

#Example
#You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

#Or three single quotes:
#Example
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])  #e
print(a[:3]) #Hel
print(a[0:3]) #Hel
print(a[-3:]) #ld!

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#String Methods
#https://www.w3schools.com/python/python_strings.asp