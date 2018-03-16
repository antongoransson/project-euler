from math import log
# Optimized Sieve of Eratosthenes
def get_primes(n):
    primes = [2] + [i for i in range(3, n, 2)]
    p = 1
    for x in primes:
        p += 2
        while primes[p // 2] == 0 : p += 2
        if  p ** 2 > n: break
        for i in range(p ** 2, n, 2 * p): primes[i // 2] = 0
    return list(filter(lambda x: x != 0, primes))

n = 10001
primes_n = n * log(n) + n * log(log(n)) #  prime number theorem approximation
print(get_primes(int(primes_n))[10000])
