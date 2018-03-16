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

def prime_factors(n):
    primes = get_primes(n % 10000000)
    p = []
    for i in primes:
        while n % i == 0:
            n //= i
            p.append(i)
    return  p
n = 600851475143
print(max(prime_factors(n)))
