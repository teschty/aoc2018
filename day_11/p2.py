with open("input.txt") as f:
    serial = int(f.read().strip())

def get_power_level(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_level = int(power_level / 100) % 10
    power_level -= 5

    return power_level

grid = [[0 for _ in range(300)] for _ in range(300)]

# convenince function as the loop below will attempt to access negative indicies
def get_grid(x, y):
    return grid[y][x] if x > 0 and y > 0 else 0

max_power, max_x, max_y, max_size = 0, 0, 0, 0

for x in range(0, 300):
    for y in range(0, 300):
        grid[y][x] = get_power_level(x, y) + get_grid(x, y - 1) + get_grid(x - 1, y) - get_grid(x - 1, y - 1)

for size in range(2, 300):
    for y in range(size, 300):
        for x in range(size, 300):
            total_power = get_grid(x, y) - get_grid(x, y - size) - get_grid(x - size, y) + get_grid(x - size, y - size)

            if total_power > max_power:
                max_power = total_power
                max_x, max_y = x, y
                max_size = size

print(f"{max_x - max_size + 1},{max_y - max_size + 1},{max_size}")
