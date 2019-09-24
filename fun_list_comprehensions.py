list = [1,2,"a",3.14,True]


#List comprehensions
#[expr for val in collection]
#[expr for val in collection if <test>]
#[expr for val in collection if <test1> and <test2>]
#[expr for val1 in collection1 and val2 in collection2]

squares = []

for i in range(1,11):
    squares.append(i**2)
print(squares)

squares2 = [i**2 for i in range(10)]
print(squares2)

remainders5 = [x**2 % 5 for x in range(1,30)]
print(remainders5)

movies = ["Star Wars","Ghostbusters"]
gmovies = [m for m in movies if m.startswith("G")]
print(gmovies)


movies = [("Star Wars",2010),("Ghostbusters",1999)]
gmovies = [m[0] for m in movies if m[1]>2000]
print(gmovies)

A=[1,3,5,7]
B=[2,4,6,8]

C=[(a,b) for a in A for b in B]
print(C)