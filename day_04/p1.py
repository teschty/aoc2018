# lol, this isn't good

import re

with open("input.txt") as f:
    lines = f.readlines()

# Sorting YYYY-MM-DD timestamps lexicographically 
# also sorts them chronologically
lines = sorted(lines)

# dict from guard id to dict of frequency that guard sleeps for each minute
sleep_times = {}
# dict from guard id to total number of minutes slept
total_sleep_time = {}

guard_on_duty = None
guard_sleep_start = None

for line in lines:
    parts = list(filter(None, re.split(" |#|:|]", line)))

    if parts[3] == "Guard":
        guard_on_duty = int(parts[4])

        sleep_times[guard_on_duty] = sleep_times.get(guard_on_duty, {})
        total_sleep_time[guard_on_duty] = total_sleep_time.get(guard_on_duty, 0)
    elif parts[3] == "falls":
        guard_sleep_start = int(parts[2])
    elif parts[3] == "wakes":
        sleep_end = int(parts[2])
        total_sleep_time[guard_on_duty] += (sleep_end - guard_sleep_start)

        for time in range(guard_sleep_start, sleep_end):
            sleep_times[guard_on_duty][time] = sleep_times[guard_on_duty].get(time, 0) + 1
        
max_guard = max(total_sleep_time.keys(), key = lambda key: total_sleep_time[key])
max_minute = max(sleep_times[max_guard].keys(), key = lambda key: sleep_times[max_guard][key])

print(max_guard * max_minute)
