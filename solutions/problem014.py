def collats_sequence(n):
    count = 1
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count

m = 0
nbr = 0
for i in range(1000000):
    l = collats_sequence(i)
    if  l > m:
        m = l
        nbr = i

print(nbr, m)
