def get_digits(nbr, power):
    return str(pow(nbr, power))

print(sum([int(i) for i in get_digits(2, 1000)]))
