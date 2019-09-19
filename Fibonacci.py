
#Recursion, the Fibonacci Sequence
'''
from functools import lru_cache

#fibonacci
@lru_cache(maxsize=1000)
def fibonacci2(n):
    if type(n) not in [int]:
        raise TypeError("n must be a positive number")
    if n<1:
        raise TypeError("n must be a positive number")

    if n==1:
        return 1
    elif n==2:
        return 1        
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)
    #fibonacci_cache[n] = value

for n in range(1,101):
    print(n,":",fibonacci2(n))

#fibonacci2(-1)
'''

fibonacci_cache={}
def fibonacci(n):
    #If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    #Compute the Nth term
    if n==1:
        value = 1
    elif n== 2:
        value = 1
    elif n>2:
        value = fibonacci(n-1)+fibonacci(n-2)
    
    #Cache the value & return it
    fibonacci_cache[n] = value
    return value
    

for n in range(1,11):
    print(n,":",fibonacci(n))

for n in range(1,20):
    print(fibonacci(n+1)/fibonacci(n))


