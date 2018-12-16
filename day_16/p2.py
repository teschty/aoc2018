import ast

# all instructions store into register C, so no need to pass it to lambda
instructions = {
    "addr": lambda r, a, b: r[a] + r[b],
    "addi": lambda r, a, b: r[a] + b,

    "mulr": lambda r, a, b: r[a] * r[b],
    "muli": lambda r, a, b: r[a] * b,

    "banr": lambda r, a, b: r[a] & r[b],
    "bani": lambda r, a, b: r[a] & b,

    "borr": lambda r, a, b: r[a] | r[b],
    "bori": lambda r, a, b: r[a] | b,

    "setr": lambda r, a, _: r[a],
    "seti": lambda r, a, _: a,

    "gtir": lambda r, a, b: 1 if a > r[b] else 0,
    "gtri": lambda r, a, b: 1 if r[a] > b else 0,
    "gtrr": lambda r, a, b: 1 if r[a] > r[b] else 0,

    "eqir": lambda r, a, b: 1 if a == r[b] else 0,
    "eqri": lambda r, a, b: 1 if r[a] == b else 0,
    "eqrr": lambda r, a, b: 1 if r[a] == r[b] else 0,
}

possible_mappings = {
    i: set(instructions.keys()) for i in range(0, 16)
}

with open("input.txt") as f:
    text = f.read()
    # remove second section for now
    first_section = text.find("\n\n\n")
    # remove empty lines
    first_second = [line for line in text[:first_section].splitlines() if line]
    second_section = [line for line in text[first_section:].splitlines() if line]

def chunks(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

for before, ins, after in chunks(first_second, 3):
    before = ast.literal_eval(before[8:])
    ins = [int(s) for s in ins.split()]
    after = ast.literal_eval(after[8:])

    matches = []
    for (name, op_fn) in instructions.items():
        # clone 'before' by slicing
        registers = before[:]
        registers_after = after[:]

        a, b, c = ins[1:]
        registers[c] = op_fn(registers, a, b)

        # if these are now equal, this instruction matches
        if registers == registers_after:
            matches.append(name)
    
    possible_mappings[ins[0]] = possible_mappings[ins[0]].intersection(matches)
    
# now we have to loop through and remove 1-1 mappings from 1-many mappings
# this will cause a cascade of more 1-1 mappings, which we then have to remove as well
# so we'll loop an indefinite amount of times
found = True
while found:
    # create set of all definite mappings
    one_to_one = set(next(iter(mappings)) for mappings in possible_mappings.values() if len(mappings) == 1)

    found = False
    for ins_num, mappings in possible_mappings.items():
        # if it's not a definite mapping and it contains a definite one-to-one mapping
        if len(mappings) > 1 and len(mappings.intersection(one_to_one)) > 0:
            # we need to remove it from that set
            possible_mappings[ins_num] = mappings.difference(one_to_one)
            found = True

# create a dict of actual mappings to lambdas
mappings = { i: instructions[next(iter(mappings))] for i, mappings in possible_mappings.items() }
registers = [0] * 4

for line in second_section:
    ins, a, b, c = [int(s) for s in line.split()]
    registers[c] = mappings[ins](registers, a, b)

print(registers[0])
