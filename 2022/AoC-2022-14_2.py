# https://adventofcode.com/2022/day/14
# --- Day 14: Regolith Reservoir ---
from datetime import datetime
start_time = datetime.now()

# Reading the file and splitting the lines into a list of lists.
with open('C:\\Users\\edo-wg\\Documents\\AoC\\2022\\input\\workfile14', encoding="utf-8") as f:
    scan = [[s for s in line.strip().split(" -> ")] for line in f]
f.closed
# print(len(scan))

iScan = []
for r in scan:
    iScan.append([])
    for e in r:
        a = e.split(",")
        iScan[len(iScan)-1].append([int(a[1]), int(a[0])])
# iScan = iScan[1:]

floor = 0

def foundBoundaries():
    global floor
    for r in iScan:
        for e in r:
            if e[0] > floor:
                floor = e[0]

foundBoundaries()
floor += 2

# cave = [['.']*600 for i in range(floor)]
# cave = [['.']*700 for i in range(floor)]
cave = [['.']*1000 for i in range(floor)]

start = [0, 500]

def drawSidePath(y, st, fin):
    global cave
    for p in range(st, fin+1):
        cave[y][p] = '#'

def drawDownPath(x, st, fin):
    global cave
    for p in range(st, fin+1):
        cave[p][x] = '#'

def rocksFall():
    for rock in iScan:
        for i in range(len(rock) - 1):
            if rock[i][0] == rock[i+1][0]:
                drawSidePath(rock[i][0], min(rock[i][1], rock[i+1][1]), max(rock[i][1],rock[i+1][1]))
            if rock[i][1] == rock[i+1][1]:
                drawDownPath(rock[i][1], min(rock[i][0],rock[i+1][0]), max(rock[i][0],rock[i+1][0]))

rocksFall()

# print(cave)

unitsOfSand = 0
theEnd = False

def checkDown(curr):
    return [curr[0]+1, curr[1]]

def checkDownLeft(curr):
    return [curr[0]+1, curr[1]-1]

def checkDownRight(curr):
    return [curr[0]+1, curr[1]+1]

def downOneStep(curr):
    global theEnd
    move = checkDown(curr)
    if move[0] == floor:
        cave[curr[0]][curr[1]] = 'o'
        return curr
    whatsNext = cave[move[0]][move[1]]
    if whatsNext == '.':
        return move
    if whatsNext in ('#', 'o'):
        move = checkDownLeft(curr)
        if move[0] == floor:
            cave[curr[0]][curr[1]] = 'o'
            return curr
        whatsNext = cave[move[0]][move[1]]
        if whatsNext == '.':
            return move
        if whatsNext in ('#', 'o'):
            move = checkDownRight(curr)
            if move[0] == floor:
                cave[curr[0]][curr[1]] = 'o'
                return curr
            whatsNext = cave[move[0]][move[1]]
            if whatsNext == '.':
                return move
    cave[curr[0]][curr[1]] = 'o'
    return curr

while not theEnd:
    sand = start
    while True:
        newPos = downOneStep(sand)
        if newPos == start:
            theEnd = True
            break
        if newPos == sand:
            break
        if theEnd:
            break
        sand = newPos
    unitsOfSand += 1

# print(cave)

print(unitsOfSand)

# 25248
# Duration: 0:00:10.072654

# Time of execution
print('Duration: {}'.format(datetime.now() - start_time))