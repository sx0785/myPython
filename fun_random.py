#https://docs.python.org/3/library/random.html?highlight=random#module-random

import random

def my_random():
    return 4*random.random()+3

for i in range(10):
    print(my_random())
    print(random.randint(4,10))


outcomes = ["rock","paper","scissors"]
for i in range(10):
    print(random.choice(outcomes))
