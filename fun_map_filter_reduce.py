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