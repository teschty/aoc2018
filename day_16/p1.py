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

with open("input.txt") as f:
    text = f.read()
    # remove second section for now
    text = text[:text.find("\n\n\n")]
    # remove empty lines
    lines = [line for line in text.splitlines() if line]

def chunks(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

num_multiple_matches = 0
for before, ins, after in chunks(lines, 3):
    before = ast.literal_eval(before[8:])
    ins = [int(s) for s in ins.split()]
    after = ast.literal_eval(after[8:])

    num_matches = 0
    for (name, op_fn) in instructions.items():
        # clone 'before' by slicing
        registers = before[:]
        registers_after = after[:]

        a, b, c = ins[1:]
        registers[c] = op_fn(registers, a, b)

        # if these are now equal, this instruction matches
        if registers == registers_after:
            num_matches += 1
    
    if num_matches >= 3:
        num_multiple_matches += 1

print(num_multiple_matches)
