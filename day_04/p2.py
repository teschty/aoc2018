# lol, this isn't good

import re

with open("input.txt") as f:
    lines = f.readlines()

# Sorting YYYY-MM-DD timestamps lexicographically 
# also sorts them chronologically
lines = sorted(lines)

# dict from guard id to dict of frequency that guard sleeps for each minute
sleep_times = {}

guard_on_duty = None
guard_sleep_start = None

for line in lines:
    parts = list(filter(None, re.split(" |#|:|]", line)))

    if parts[3] == "Guard":
        guard_on_duty = int(parts[4])

        sleep_times[guard_on_duty] = sleep_times.get(guard_on_duty, {})
    elif parts[3] == "falls":
        guard_sleep_start = int(parts[2])
    elif parts[3] == "wakes":
        sleep_end = int(parts[2])

        for time in range(guard_sleep_start, sleep_end):
            sleep_times[guard_on_duty][time] = sleep_times[guard_on_duty].get(time, 0) + 1
        
most_freq_minute = (0, 0)
most_freq_guard = None

for guard in sleep_times.keys():
    if len(sleep_times[guard].keys()) == 0:
        continue

    max_minute = max(sleep_times[guard].keys(), key = lambda key: sleep_times[guard][key])

    freq = sleep_times[guard][max_minute]
    if freq > most_freq_minute[1]:
        most_freq_minute = (max_minute, freq)
        most_freq_guard = guard

print(most_freq_guard * most_freq_minute[0])
