import re

with open("input.txt") as f:
    lines = f.readlines()

grid = [[0] * 1000 for _ in range(1000)]
count = 0

for line in lines:
    parts = [int(p) for p in re.split("#| |,|:|x", line.strip()) if p.isdigit()]

    (sx, sy) = (parts[1], parts[2])
    (w, h) = (parts[3], parts[4])

    for y in range(sy, sy + h):
        for x in range(sx, sx + w):
            grid[x][y] += 1

            # only add to count if we're incrementing to two
            # this prevents double counting
            if grid[x][y] == 2:
                count += 1

print(count)
