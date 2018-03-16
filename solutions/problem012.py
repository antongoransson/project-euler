from functools import reduce

def get_nbr_divisors(arr):
    arr = [1] + arr
    return reduce(lambda x, y: x * (y + 1) , arr)

def get_primes(n):
    primes = [2] + [i for i in range(3, n, 2)]
    p = 1
    for x in primes:
        p += 2
        while primes[p // 2] == 0 : p += 2
        if  p ** 2 > n: break
        for i in range(p ** 2, n, 2 * p): primes[i // 2] = 0
    return list(filter(lambda x: x != 0, primes))

def tri_seq_generator(n = 1):
    while True:
        T = n * ( n + 1) // 2
        n += 1
        yield T

primes = get_primes(1000)
for y in tri_seq_generator(1000):
    x = y
    divisors = []
    for p in primes:
        if p // 2 > x: break
        while x % p == 0:
            x //= p
            divisors.append(p)
    div_cnt = set(map(lambda x  : (x, list(divisors).count(x)), divisors))
    count = get_nbr_divisors([t for _, t in div_cnt])
    if count > 500:
        print(y, count, divisors)
        break
