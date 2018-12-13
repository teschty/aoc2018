with open("input.txt") as f:
    lines = f.readlines()

two_times = 0
three_times = 0

for line in lines:
    char_freqs = dict()

    for c in line:
        char_freqs[c] = char_freqs.get(c, 0) + 1

    get_freq = lambda n: [k for k in char_freqs if char_freqs[k] == n]
    two_times += 1 if get_freq(2) else 0 
    three_times += 1 if get_freq(3) else 0 

print(two_times * three_times)
