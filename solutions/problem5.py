from functools import reduce
from math import gcd

def lcm(a, b):
    return abs(a) // gcd(a, b) * abs(b)

def smallest_multiple(arr):
    return reduce(lambda x, y: lcm(x, y) , arr)

n =  20
print(smallest_multiple([x for x in range(1, n + 1)]))
