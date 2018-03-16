with open('problem13in.txt', 'r') as f:
    ints = [int(line) for line in iter(f.readline, '')]
print(str(sum(ints))[:10])
