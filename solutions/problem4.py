def is_palindrome(n):
    return str(n) == str(n)[::-1]

prod, m = 0, 0
for x in range(100, 999):
    for y in range(100, 999):
        prod = x * y
        if is_palindrome(prod):
            m = max(m, prod)
print(m)
