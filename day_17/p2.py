from collections import Counter, defaultdict
from itertools import product, count
import re

with open("input.txt") as f:
    lines = f.readlines()

def parse_line(line):
    parts = [int(x) for x in re.findall("[0-9]+", line)]
    return list(range(parts[0], parts[-1] + 1))

tiles = defaultdict(lambda: ".")

for line in lines:
    x, y = sorted(line.split(", "))
    x_range, y_range = map(parse_line, [x, y])

    for x, y in product(y_range, x_range):
        tiles[y, x] = "#"

min_x = min([x for _, x in tiles.keys()])
max_x = max([x for _, x in tiles.keys()])
max_y = max([y for y, _ in tiles.keys()])

stack = [(500, min_x - 1)]
while stack:
    current = stack[-1]
    if tiles[current] == "~":
        stack.pop()
        continue

    y, x = current

    if x == max_x:
        stack.pop()
        continue
    
    for p in [(y, x + 1), (y + 1, x), (y - 1, x)]:
        if tiles[p] == "|" and p == (y, x + 1):
            stack.pop()
            break
        
        if tiles[p] == ".":
            tiles[p] = "|"
            stack.append(p)
            break
    else:
        stack.pop()
        if re.match("#\|+#", "".join(tiles[(j, x)] for j in range(y - 1, max_y + 1))):
            for j in count(y):
                if tiles[j, x] == "#": break
                tiles[j, x] = "~"

c = Counter(tiles.values())
print(c["~"])
