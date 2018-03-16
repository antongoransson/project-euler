def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def binomial_coeff(n ,k):
    return factorial(n) // ( factorial(k) * factorial(n - k))

def lattice_paths(row_size, col_size):
    return binomial_coeff(row_size + col_size, col_size)

print(lattice_paths(20 , 20))
