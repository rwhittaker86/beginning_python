#!/usr/bin/env python 3.6
a = 10
b=20
print("A added to B is %d" % (a+b))
def in_fridge():
    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count
fridge = {'apples':10, 'oranges':3, 'milk':2}
wanted_food = 'apples'
print(in_fridge())
