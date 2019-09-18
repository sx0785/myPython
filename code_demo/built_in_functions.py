'''
print(abs(-5))


i1 = 1
i2 = 1
i=0
while i<100:
    i = i1+i2
    print(i)
    i1=i2
    i2=i
'''    

from functools import lru_cache

#fibonacci
@lru_cache(maxsize=1000)
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1        
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)
    #fibonacci_cache[n] = value
    

#fibonacci_cache = {}
'''
def fibonacci(n):
    if n==1:
        value = 1
    elif n==2:
        value = 1        
    elif n>2:
        value = fibonacci(n-1)+fibonacci(n-2)    
    #fibonacci_cache[n] = value
    return value
'''

fibonacci(2.1)

#for n in range(1,501):
#    print(n,":",fibonacci(n))

