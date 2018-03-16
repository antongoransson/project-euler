from math import sqrt
from functools import reduce

def mul_arr(arr):
    return int(reduce(lambda x, y: x * y , arr))

def get_triplet(n):
    max_a = n // 2 - 2
    max_b = max_a + 2
    for a in range(1, max_a):
        for b in range(a, max_b):
            c = sqrt(a ** 2 + b ** 2)
            if a + b + c == n:
                return a, b, c
n = 1000
triplet = get_triplet(n)
print(triplet, mul_arr(triplet))
