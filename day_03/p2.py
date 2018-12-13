import re

with open("input.txt") as f:
    lines = f.readlines()

grid = [[0] * 1000 for _ in range(1000)]
untouched = set()

for line in lines:
    parts = [int(p) for p in re.split("#| |,|:|x", line.strip()) if p.isdigit()]

    claim_id = parts[0]
    (sx, sy) = (parts[1], parts[2])
    (w, h) = (parts[3], parts[4])

    untouched.add(claim_id)

    for y in range(sy, sy + h):
        for x in range(sx, sx + w):
            # if someone has been here before
            if grid[x][y] != 0:
                # remove them
                untouched.discard(grid[x][y])
                # and us (as we also overlap)
                untouched.discard(claim_id)
            
            grid[x][y] = claim_id

print(untouched)
