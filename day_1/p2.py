def part_two():
    with open("input.txt") as f:
        lines = f.readlines()

    freq = 0
    previous_freqs = dict()
    while True:
        for line in lines:
            previous_freqs[freq] = 1

            val = int(line)
            freq += val

            if freq in previous_freqs:
                print(freq)
                return

part_two()
