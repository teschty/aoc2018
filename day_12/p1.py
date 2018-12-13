with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

transformations = { before: after for before, _, after in map(str.split, lines[2:]) if after == "#" }
plant_indexes = { idx for idx, p in enumerate(lines[0][15:]) if p == "#" }

generations = 20

for _ in range(generations):
    left_plant = min(plant_indexes)
    right_plant = max(plant_indexes)

    pots = "".join("#" if i in plant_indexes else "." for i in range(left_plant - 4, right_plant + 4))
    plant_indexes = { i -4 + left_plant for i in range(2, right_plant + 7) if pots[i-2:i+3] in transformations }

print(sum(plant_indexes))
