# lazy, dumb solution

with open("input.txt") as f:
    lines = f.readlines()

# returns the number of differing characters and common characters joined to a string
# works under the assumption that both strings are the same length
def difference(one, two):
    common_chars = [c1 for (c1, c2) in zip(one, two) if c1 == c2]

    return len(one) - len(common_chars), "".join(common_chars)

# input is small enough that we can brute-force
one_off = [(l1, l2) for l1 in lines for l2 in lines if difference(l1, l2)[0] == 1]

first = one_off[0][0]
second = one_off[0][1]

print(difference(first, second)[1])
