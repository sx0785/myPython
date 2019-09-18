#Python Lambda

#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#https://realpython.com/python-lambda/

#https://realpython.com/lessons/what-is-lambda-function/

'''
Syntax
As you saw in the previous sections, a lambda form presents syntactic distinctions from a normal function. In particular, a lambda function has the following characteristics:

It can only contain expressions and can’t include statements in its body.
It is written as a single line of execution.
It does not support type annotations.
It can be immediately invoked (IIFE).

Arguments
Like a normal function object defined with def, Python lambda expressions support all the different ways of passing arguments. This includes:

Positional arguments
Named arguments (sometimes called keyword arguments)
Variable list of arguments (often referred to as varargs)
Variable list of keyword arguments
Keyword-only arguments

'''


add_one = lambda x: x + 1
add_one(2)


def add_one(x):
    return x + 1


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))


'''
Taken literally, an anonymous function is a function without a name. 
In Python, an anonymous function is created with the lambda keyword. 
More loosely, it may or not be assigned a name. 
Consider a two-argument anonymous function defined with lambda but not bound to a variable. 
The lambda is not given a name:
'''

print((lambda x, y: x + y)(2,3))

#print(_(2,3))


#high-order function
high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x)) #6
print(high_ord_func(2, lambda x: x + 3)) #7


import dis
add = lambda x, y: x + y
type(add)
dis.dis(add)
add

import dis
def add(x, y): return x + y
type(add)
dis.dis(add)
add
'''
Arguments
Like a normal function object defined with def, Python lambda expressions support all the different ways of passing arguments. This includes:

Positional arguments
Named arguments (sometimes called keyword arguments)
Variable list of arguments (often referred to as varargs)
Variable list of keyword arguments
Keyword-only arguments

'''
(lambda x, y, z: x + y + z)(1, 2, 3)
(lambda x, y, z=3: x + y + z)(1, 2)
(lambda x, y, z=3: x + y + z)(1, y=2)
(lambda *args: sum(args))(1,2,3)
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)



def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")


'''
Appropriate Uses of Lambda Expressions
Lambdas in Python tend to be the subject of controversies. Some of the arguments against lambdas in Python are:

Issues with readability
The imposition of a functional way of thinking
Heavy syntax with the lambda keyword
'''


import functools
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)) #6


pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
sum(x[0] for x in pairs) #6

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
sum(x for x, _ in pairs)



def second(x):
    return x[1]

a = [(1,2),(2,5),(3,1),(4,15)]
a.sort(key=second)
print(a)

a.sort(key=lambda x: x[1])
print(a)

import math
def area(r):
    return math.pi * (r**2)

radii = [2,5,7.1,0.3,10]
areas = []

for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

#Map
print(list(map(area,radii)))
#print(list(map(lambda r:math.pi*(r**2),[2,5,7.1,0.3,10])))
#print(list(map(lambda r:math.pi*(r**2)))[2,5,7.1,0.3,10])

#https://www.youtube.com/watch?v=hUes6y2b--0
temps = [("Berlin",29),("Cairo",36),("Buenos Aires",19),("Los Angeles",26),("Tokyo",27),("New York",28)]
c_to_f = lambda data:(data[0],(9/5)*data[1]+32)
print(list(map(c_to_f,temps)))


#Filter
import statistics
data = [1.3,2.7,0.8,4.1,4.3,-0.1]
avg = statistics.mean(data)
print(avg)

print(list(filter(lambda x:x>avg,data)))

countries = ["","Argentina","Brazil","Chile","","Colombia","","Venezuela"]
print(list(filter(None,countries)))


#reduce
from functools import reduce
data = [2,3,5,8,9,11]
multiplier = lambda x,y:x*y
print(reduce(multiplier,data))
