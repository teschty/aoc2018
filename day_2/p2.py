# lazy, dumb solution

with open("input.txt") as f:
    lines = f.readlines()

def difference(one, two):
    num_differing = 0
    common = ""

    for c1, c2 in zip(one, two):
        if c1 != c2:
            num_differing += 1
        else:
            common += c1

    return num_differing, common

# input is small enough that we can brute-force
one_off = [(l1, l2) for l1 in lines for l2 in lines if difference(l1, l2)[0] == 1]

first = one_off[0][0]
second = one_off[0][1]

print(difference(first, second)[1])
