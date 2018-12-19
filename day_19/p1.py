with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

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

ip = 0
ip_reg = int(lines[0][4:])
registers = [0] * 6

lines = lines[1:]
while ip < len(lines):
    registers[ip_reg] = ip
    line = lines[ip]

    if line.startswith("#ip"):
        ip_reg = int(line[4:])
    else:
        parts = line.split()
        ins = parts[0]
        a, b, c = [int(p) for p in parts[1:]]
        registers[c] = instructions[ins](registers, a, b)

    ip = registers[ip_reg] + 1

print(registers[0])