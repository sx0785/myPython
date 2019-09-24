def build_quadratic_function(a,b,c):
    '''return the function f(x)=ax^2+bx+c'''    
    return lambda x:a*x**2+b*x+c

f=build_quadratic_function(2,3,-5)

print(f(3))

print(build_quadratic_function(3,0,1)(2))

