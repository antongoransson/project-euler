import sys

def fibonacci_sequence(length = sys.maxsize, max_val = sys.maxsize):
    prev, curr = 1, 1
    for i in range(length):
        if curr > max_val: break
        yield curr
        prev, curr = curr, curr + prev

print(sum([i for i in fibonacci_sequence(max_val = 4000000) if i % 2 == 0]))
