############
#  STRING  #
############
'''
name = "Shawn"
age = 42

i = "this is my first string"

print(i[1])
print(name + " is "+ str(age) +" yrs old")
#print(i.upper())
'''
#String
i = "this is my first string"
print(i.split(" ")[1])
i.join("abc")
print(i)

#"\n".join(wrap(i, ...))

print('{0}, {1}, {2}'.format('a', 'b', 'c'))

#List
friends = ["Kevin","Karen","Jim"]

friends.append("Shawn")

print(friends)
print(friends[1:3])#Kevin
print(friends[-1])#Shawn

print(all(friends))

#Exception
try:
    file = open("test.csv")
except FileNotFoundError as identifier:
    print ("file not found")
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()


#Tuple
coordinates = (4,5)    
print(coordinates[1])

#Function
def say_hello():
    print("hi")

def say_hello(name):
    print("hi "+name)


def max(x,y):    
    if x>y:
        return x
    else:
        return y

print(max(10,5))

say_hello("Shawn")

#Dictionaries
dict_month={
    1:"Jan",
    2:"Feb",
    3:"Mar",
    4:"Apr"
}
#print(dict_month[3])
print(dict_month.get(4,"not a valid key"))

#while loop
cnt = 1
while cnt<5:
    print(cnt)
    cnt+=1

#For loop
#     
for friend in friends:
    print(friend)
    

for num in range(10):
    print(num)
    