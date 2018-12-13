from itertools import cycle

def part_two():
    with open("input.txt") as f:
        lines = f.readlines()

    freq = 0
    previous_freqs = { 0 }
    for line in cycle(lines):
        previous_freqs.add(freq)

        val = int(line)
        freq += val

        if freq in previous_freqs:
            return freq

print(part_two())
