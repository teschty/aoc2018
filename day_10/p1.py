# lol this is also bad

import time
import re

with open("input.txt") as f:
    lines = f.readlines()

grid = {}

def points_at_pos(x, y):
    return grid.get((x, y), [])

def add_point(point):
    x, y = point[0], point[1]

    arr = points_at_pos(x, y)
    arr.append(point)
    grid[x, y] = arr

points = []
for line in lines:
    parts = re.split("<|>|,", line)
    point = [int(s) for s in [parts[1], parts[2], parts[4], parts[5]]]

    points.append(point)
    add_point(point)

min_x, max_x = float("inf"), -float("inf")
min_y, max_y = float("inf"), -float("inf")

last_area = float("inf")
while True:
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]

    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]

    area = (max_x - min_x) * (max_y - min_y)

    # message will be spelled out when area is minimal
    # so if it increases, we're done
    if area > last_area:
        break

    last_area = area

    if max_x - min_x < 100:
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                print("#" if len(points_at_pos(x, y)) > 0 else ".", end="")

            print()

        time.sleep(0.5)

    for point in points:
        x, y = point[0], point[1]
        grid[x, y].remove(point)

        point[0] += point[2]
        point[1] += point[3]

        add_point(point)

