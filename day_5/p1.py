from functools import reduce

with open("input.txt") as f:
    polymer = f.read()

def will_react(c1, c2):
    return c1.lower() == c2.lower() and c1 != c2

polymer = reduce(lambda s, c: s[1:] if will_react(s[0], c) else c+s, reversed(polymer))

print(len(polymer))
