'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.



'''
class Box:
    def __init__(self, data):
        self.data = data

    def setNext(self,Box):
        self.next = Box
        
b1 = Box(6)
b2 = Box(3)
b1.setNext(b2)
print(b1.data)
print(b1.next.data)

class Robot:
    def __init__(self,name):
        self.name = name
        

    def introduce_self(self):
        print(self.name)

class Person:
    #def __init__(self, name, personality,isSitting,Robot):
    def __init__(self, name, personality,isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True

    def ownRobot(self,Robot):
        self.robotOwned = Robot


r1 = Robot("Tom")

p1 =  Person("Jerry","Friendly","Y")
p1.ownRobot(r1)

print(p1.robotOwned.name)
'''

a_smile = False
b_smile = True

if a_smile != b_smile: print("False")
else: print("True")

def monkey_trouble(a_smile,b_smile):
    return not (a_smile!=b_smile)

#print(monkey_trouble(a_smile,b_smile))
a = 1
b = 2

if a==b:print (2*(a+b))
else: print(a+b) 

def sum_double(a, b):
  if a==b :return 2*(a+b)
  else:return a+b

#print(sum_double(a,b))  

def diff21(n):
    if n>21: 
        return 2*abs(n-21)
    else: 
        return abs(n-21)

def parrot_trouble(talking, hour):
    return(talking and (hour<7 or hour>20))

def makes10(a, b):
    return((10 in (a,b)) or (a+b==10))

def near_hundred(n):
    return(abs(n-100)<10 or abs(n-200)<10)
'''
str = "EDDEBCABA"
first=""

for i in str:
    if str.find(i,str.index(i)+1)>0 :
        print(i)
        break

def str_finder(str):
    for s in str:
        i = str.index(s)
        if str.find(s,i+1)>0:
            print(s)
            break

def first_recurring(given_string):
    counts={}
    for char in given_string:
        if char in counts:
            return char
        counts[char]=1


#print(first_recurring("abcd"))

def not_string(str):
    if str.find("not")==0:
        return str
    else: 
        return "not "+str

#print(not_string("too bad"))

#str2 = "abcd"
#print(str2[3])

def missing_char(str, n):
    return str.replace(str[n],"")

#print(missing_char("ABCDEFG",2))    

def front_back(str):
    if len(str)==1:
        return str
    return str[len(str)-1]+str[1:len(str)-1]+str[0]

#print(front_back("bc"))
def front3(str):
    str=str[0:3]
    return str+str+str
#print(front3("A"))    

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''
#A list/array
list = ["a",1,True,"a","d"]
#print(list)

#A tuple
tuple = ("a",1,True,"a")
#print(tuple)

#A set
set = {"a",1,"b","g"}
#print(set)

dic1 = {
    "a":1,
    "b":2,
    "c":3,
    "d":4
}

#print(dic1.get("a"))
#print(dic1["a"])


def covert(str1,dic):
    result = ""
    for i in str1:
        result=result+str(dic.get(i))
    return result

#print(covert("badc",dic1))


def string_times(str, n):
    result = ""
    #i=1
    #while i<=n:    
    for i in range(n):
        result = result+str
        #i=i+1
    return result

#print(string_times("ab",1))

def front_times(str, n):
    result = ""
    for i in range(n):
        result = result+str[0:3]
    return result

#print(front_times("abcdefg",2))
def string_bits(str):
    result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result

#print(string_bits("abcdefghij"))  
def string_splosion(str):
    newstr = ""
    for i in range(len(str)):
        newstr+=str[0:i+1]
    return newstr
#print(string_splosion("Code"))


def last2(str):
    count = 0
    if len(str)<2:
        return count
    last2 = str[len(str)-2:]    
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
            count+=1    
    return count

#print(last2("axxxaaxx"))
def array_count9(nums):
    count = 0
    for i in nums:
        if i==9: count+=1
    return count

#print(array_count9([1,9,9,9,9, 2, 9]))
def array_front9(nums):  
    result = False
    for i in nums:
        if i==9 and nums.index(i)<4:
            result = True
            break
    return result

def array123(nums):
    istrue = False
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            istrue = True
            break
    return istrue

#print(array123([1,4]))

def string_match(a, b):

     # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count

  '''
    count = 0
    for i in range(len(a)-1):
        for j in range(len(b)-1):
            if a[i]==b[j] and a[i+1]==b[j+1]:
                count+=1
                break
    return count
'''
print(string_match('aabbccdd', 'abbbxxd'))
    
  
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count

    

#print(array_count9([1, 2, 3, 4, 9]))
#array_front9([1, 2, 3, 4, 9])


#newstr=""
#newstra="a"+"a"
#newstr=aa+b+ab
    

#here is new code

#print(array)