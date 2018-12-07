with open("input.txt") as f:
    lines = f.readlines()

points = [[int(i) for i in line.split(", ")] for line in lines]

min_x = min(points, key=lambda p: p[0])[0]
max_x = max(points, key=lambda p: p[0])[0]

min_y = min(points, key=lambda p: p[1])[1]
max_y = max(points, key=lambda p: p[1])[1]

def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

total = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distance = sum(dist(x, y, px, py) for (px, py) in points)

        if distance < 10000:
            total += 1

print(total)

