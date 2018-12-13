from itertools import takewhile
from functools import reduce
from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()

points = [[int(i) for i in line.split(", ")] for line in lines]

min_x = min(points, key=lambda p: p[0])[0]
max_x = max(points, key=lambda p: p[0])[0]

min_y = min(points, key=lambda p: p[1])[1]
max_y = max(points, key=lambda p: p[1])[1]

def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

grid = {}
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        point = (x, y)

        distances = sorted((dist(x, y, px, py), n) for (n, (px, py)) in enumerate(points))
        closest = [*takewhile(lambda t: t[0] == distances[0][0], distances)]

        if len(closest) == 1:
            grid[x, y] = closest[0][1]

edges = [n for ((x, y), n) in grid.items() if x in {min_x, max_x} or y in {min_y, max_y}]
counts = Counter(n for n in grid.values() if n not in edges)

print(counts.most_common(1)[0][1])
