with open("input.txt") as f:
    recipe = f.read().strip()

recipes = "37"
first_elf = 0
second_elf = 1

len_recipe_slice = len(recipe) + 1
while not recipe in recipes[-len_recipe_slice:]:
    cur_elf_one = int(recipes[first_elf])
    cur_elf_two = int(recipes[second_elf])

    recipes += str(cur_elf_one + cur_elf_two)

    first_elf = (first_elf + 1 + cur_elf_one) % len(recipes)
    second_elf = (second_elf + 1 + cur_elf_two) % len(recipes)

# lol off by one
print(len(recipes) - len(recipe) - 1)
