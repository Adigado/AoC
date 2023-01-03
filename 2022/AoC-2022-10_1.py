# https://adventofcode.com/2022/day/10
# --- Day 10: Cathode-Ray Tube ---

import os

from datetime import datetime
start_time = datetime.now()

# Opening the file and reading it into a list.
with open(os.path.join('input', 'workfile10'), encoding="utf-8") as f:
    instructions = f.read().splitlines()
f.closed
#print(len(read_data))

spec = [20, 60, 100, 140, 180, 220]

signalStrengths = 0
xValue = 1
line = 1
cycles = 0

for instr in instructions:
    if instr[:4] == "noop":
        cycles += 1
        if cycles in spec:
            signalStrengths += (xValue * cycles)
    elif instr[:4] == "addx":
        cycles += 1
        if cycles in spec:
            signalStrengths += (xValue * cycles)
        cycles += 1
        if cycles in spec:
            signalStrengths += (xValue * cycles)
        xValue += int(instr.split()[1])
    line += 1

print(signalStrengths)

# Time of execution
print('Duration: {}'.format(datetime.now() - start_time))

# 12980 is too low. match wasn't working.
# 13440
# Duration: 0:00:00.000998
