with open("input.txt") as f:
    after_amount = int(f.read().strip())

recipes = "37"
first_elf = 0
second_elf = 1

while len(recipes) < after_amount + 10:
    one = int(recipes[first_elf])
    two = int(recipes[second_elf])

    recipes += str(one + two)

    first_elf = (first_elf + 1 + one) % len(recipes)
    second_elf = (second_elf + 1 + two) % len(recipes)

print(recipes[after_amount:])
