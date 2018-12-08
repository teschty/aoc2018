with open("input.txt") as f:
    lines = f.readlines()

print(sum(map(int, lines)))
