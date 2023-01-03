# https://adventofcode.com/2022/day/11
# --- Day 11: Monkey in the Middle ---

import os

from datetime import datetime
start_time = datetime.now()

import math

# Reading the file and creating a list of lists.
with open(os.path.join('input', 'workfile11'), encoding="utf-8") as f:
    notes = f.read().splitlines()
f.closed
#print(len(notes))

monkeyBusiness = 0
# monkeys = []
items = []
operations = []
values = []
tests = []
throwsT = []
throwsF = []
inspections = []

for note in notes:
    if note[:6] == "Monkey":
        inspections.append(0)
        #pass
    elif note.find("items") > -1:
        #  Starting items: 79, 98
        note = note[note.index(":")+2:]
        it = [int(n) for n in note.split(", ")]
        items.append(it)
    elif note.find("new") > -1:
        #  Operation: new = old * 19
        op = note[note.index("old")+4:].split(" ")
        operations.append(op[0])
        values.append(op[1]) # could be a number or 'old'
    elif note.find("Test:") > -1:
        #  Test: divisible by 19
        tests.append(int(note[note.rindex(" ")+1:]))
    elif note.find("true") > -1:
        #    If true: throw to monkey 2
        throwsT.append(int(note[note.rindex(" ")+1:]))
    elif note.find("false") > -1:
        #    If false: throw to monkey 3
        throwsF.append(int(note[note.rindex(" ")+1:]))

monkeys = len(operations)

def inspectItem(item, operation, value):
    v = 0
    if value == 'old':
        v = item
    else:
        v = int(value)
    if operation == '+':
        v += item
    else:
        v *= item
    return v

for round in range(20):
    for monkey in range(monkeys):
        for item in items[monkey]:
            worryLevel = inspectItem(item, operations[monkey], values[monkey])
            worryLevel = math.floor(worryLevel / 3)
            if worryLevel % tests[monkey] == 0:
                items[throwsT[monkey]].append(worryLevel)
            else:
                items[throwsF[monkey]].append(worryLevel)
            items[monkey] = items[monkey][1:]
            inspections[monkey] += 1

inspections.sort(reverse=True)
monkeyBusiness = inspections[0] * inspections[1]
print(monkeyBusiness)

# 55944
# Duration: 0:00:00.003989

# Time of execution
print('Duration: {}'.format(datetime.now() - start_time))