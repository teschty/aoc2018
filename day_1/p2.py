def part_two():
    with open("input.txt") as f:
        lines = f.readlines()

    freq = 0
    previous_freqs = { 0 }
    while True:
        for line in lines:
            previous_freqs.add(freq)

            val = int(line)
            freq += val

            if freq in previous_freqs:
                print(freq)
                return

part_two()
