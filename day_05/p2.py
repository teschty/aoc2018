from functools import reduce
from string import ascii_lowercase

with open("input.txt") as f:
    polymer = f.read()

def will_react(c1, c2):
    return c1.lower() == c2.lower() and c1 != c2

def react(poly):
    return reduce(lambda s, c: s[1:] if s and will_react(s[0], c) else c+s, reversed(poly))

def length_with_removal(poly, c):
    poly = poly.replace(c, "").replace(c.upper(), "")

    return len(react(poly))

print(min([length_with_removal(polymer, c) for c in ascii_lowercase]))
