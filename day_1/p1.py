with open("input.txt") as f:
    lines = f.readlines()

freq = sum(map(int, lines))
print(freq)
