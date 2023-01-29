# https://adventofcode.com/2022/day/22
# --- Day 22: Monkey Map ---

# Ctrl+Shift+P; Convert Indentation to Spaces

import os

from datetime import datetime
start_time = datetime.now()

# Reading the file and splitting the lines into a list of lists.
with open(os.path.join('input', 'workfile22'), encoding="utf-8") as f:
    # scan = [[char for char in line.strip()] for line in f]
    scan = f.read().splitlines()
f.closed
# print(len(scan))

# Creating a list of lists from the input.
width = 0
monkeyMap = []
for line in scan[:-2]:
    row = []
    for symbol in line:
        row.append(symbol)
    monkeyMap.append(row)
    if len(row) > width:
        width = len(row)

# print(len(monkeyMap), ' / ', len(monkeyMap[0]), ' | ', monkeyMap[0])

# Adding spaces to the end of each line.
for line in monkeyMap:
    if len(line) < width:
        for j in range(len(line), width):
            monkeyMap[monkeyMap.index(line)].append(" ")

path = scan[-1]

path += "."
steps = []
next = ""
# Converting the string into a list of numbers and letters.
for symbol in path:
    if symbol == ".":
        steps.append(int(next))
        break
    if symbol.isdigit():
        next += symbol
    else:
        steps.append(int(next))
        steps.append(symbol)
        next = ""
# print(len(steps))
# print(steps)

# Getting the width and height of the map.
lastX = len(monkeyMap[0])
lastY = len(monkeyMap)

start = [0, monkeyMap[0].index(".")]
facing = "R"
direction = "R"
tile = start

def searchForMatter(where, y, x):
    """
    If the monkey is facing right, search for matter (. or #) to the right,
    if the monkey is facing left, search for matter to the left,
    if the monkey is facing down, search for matter down,
    if the monkey is facing up, search for matter up.
    
    :param where: -1 or 1, depending on which direction the monkey is facing
    :param y: the y coordinate of the monkey
    :param x: the current x position of the monkey
    :return: the x or y coordinate of the first non-space character (. or #) it finds.
    """
    match facing:
        case "R":
            while monkeyMap[y][x] == " ":
                if x >= lastX-1:
                    x = 0
                else:
                    x += where
            return x
        case "L":
            while monkeyMap[y][x] == " ":
                if x < 0:
                    x = lastX-1
                else:
                    x += where
            return x
        case "D":
            while monkeyMap[y][x] == " ":
                if y >= lastY-1:
                    y = 0
                else:
                    y += where
            return y
        case "U":
            while monkeyMap[y][x] == " ":
                if y < 0:
                    y = lastY-1
                else:
                    y += where
            return y
    return [-1, -1]

# Moving the monkey.
# Iterating through the list of steps.
for step in steps:
    # Check if the step is a number.
    if str(step).isnumeric():
        # Moving the monkey one step at a time.
        for c in range(step):
            match facing:
                # It's checking if the next tile is out of bounds.
                # If it is, it sets the next tile to the first tile of the same row / column.
                case "R":
                    if tile[1]+1 > lastX-1:
                        next = monkeyMap[tile[0]][0]
                        nextX = 0
                    else:
                        next = monkeyMap[tile[0]][tile[1]+1]
                        nextX = tile[1]+1  # 
                    # Search for the next tile with non-space character (. or #).
                    if next == " ":
                        nextX = searchForMatter(1, tile[0], nextX)
                        next = monkeyMap[tile[0]][nextX]
                        tile = [tile[0], nextX]
                    # Checking go / no-go further.
                    match next:
                        case ".":
                            if tile[1]+1 > lastX-1:
                                tile = [tile[0], 0]
                            else:
                                tile = [tile[0], nextX]
                        case "#":
                            break
                case "L":
                    if tile[1]-1 < 0:
                        nextX = lastX - 1
                        next = monkeyMap[tile[0]][nextX]
                    else:
                        nextX = tile[1] - 1
                        next = monkeyMap[tile[0]][nextX]
                    if next == " ":
                        nextX = searchForMatter(-1, tile[0], nextX)
                        next = monkeyMap[tile[0]][nextX]
                        tile = [tile[0], nextX]
                    match next:
                        case ".":
                            if tile[1]-1 < 0:
                                tile = [tile[0], lastX-1]
                            else:
                                tile = [tile[0], nextX]
                        case "#":
                            break
                case "D":
                    if tile[0]+1 > lastY-1:
                        nextY = 0
                        next = monkeyMap[nextY][tile[1]]
                    else:
                        nextY = tile[0]+1
                        next = monkeyMap[nextY][tile[1]]
                    if next == " ":
                        nextY = searchForMatter(1, nextY, tile[1])
                        next = monkeyMap[nextY][tile[1]]
                        tile = [nextY, tile[1]]
                    match next:
                        case ".":
                            tile = [nextY, tile[1]]
                        case "#":
                            break
                case "U":
                    if tile[0]-1 < 0:
                        nextY = lastY - 1
                        next = monkeyMap[nextY][tile[1]]
                    else:
                        nextY = tile[0]-1
                        next = monkeyMap[nextY][tile[1]]
                    if next == " ":
                        nextY = searchForMatter(-1, nextY, tile[1])
                        next = monkeyMap[nextY][tile[1]]
                        tile = [nextY, tile[1]]
                    match next:
                        case ".":
                            tile = [nextY, tile[1]]
                        case "#":
                            break
    else:
        # Changing the direction of the monkey.
        match step:
            case "R":
                match facing:
                    case "R":
                        facing = "D"
                    case "L":
                        facing = "U"
                    case "D":
                        facing = "L"
                    case "U":
                        facing = "R"
            case "L":
                match facing:
                   case "R":
                        facing = "U"
                   case "L":
                        facing = "D"
                   case "D":
                        facing = "R"
                   case "U":
                        facing = "L"

# Converting the direction the monkey is facing into a number.
match facing:
    case "R":
        finalPassword = 0
    case "D":
        finalPassword = 1
    case "L":
        finalPassword = 2
    case "U":
        finalPassword = 3

# Converting the coordinates of the monkey into a number.
finalPassword += 1000 * (tile[0] + 1) + 4 * (tile[1] + 1)

print(finalPassword)

# 27602 is too low. tile = [26, 149]
# 16282. tile = [15, 69]
# Duration: 0:00:00.046895

# tile = [185, 32] move Down L29
# tile = [nextY, tile[1]] / tile = [tile[0], nextX] for all 4 directions.
# 5446. tile = [4, 100]

# tile = [nextY, tile[1]] only for D direction.
# 34450 is too low. tile = [26, 149]

# 165094
# Duration: 0:00:00.052859

# Time of execution
print('Duration: {}'.format(datetime.now() - start_time))