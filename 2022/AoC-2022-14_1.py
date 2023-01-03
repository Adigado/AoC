# https://adventofcode.com/2022/day/14
# --- Day 14: Regolith Reservoir ---

import os

from datetime import datetime
start_time = datetime.now()

# Reading the file and splitting the lines into a list of lists.
with open(os.path.join('input', 'workfile14'), encoding="utf-8") as f:
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

minX = 10000
maxX = 0
minY = 0 # 10000
maxY = 0

def foundBoundaries():
    global minX, minY, maxX, maxY
    for r in iScan:
        for e in r:
            if e[1] < minX:
                minX = e[1]
            if e[1] > maxX:
                maxX = e[1]
            # if e[0] < minY:
            #     minY = e[0]
            if e[0] > maxY:
                maxY = e[0]

foundBoundaries()
cave = [['.']*(maxX - minX + 2) for i in range((maxY + 1))]
#a = a + [0]*(maxLen - len(a))
#t = [ [0]*3 for i in range(3)]

start = [0, (500-minX)]

# print(cave)

def drawSidePath(y, start, fin):
    global cave
    for p in range(start-minX, fin-minX+1):
        cave[y][p] = '#'

def drawDownPath(x, start, fin):
    global cave
    for p in range(start, fin+1):
        cave[p][x - minX] = '#'

def rocksFall():
    for rock in iScan:
        for i in range(len(rock) - 1):
            if rock[i][0] == rock[i+1][0]:
                drawSidePath(rock[i][0], min(rock[i][1], rock[i+1][1]), max(rock[i][1],rock[i+1][1]))
            if rock[i][1] == rock[i+1][1]:
                drawDownPath(rock[i][1], min(rock[i][0],rock[i+1][0]), max(rock[i][0],rock[i+1][0]))

rocksFall()

# print(cave)

endlessVoid = False

def checkDown(curr):
    return [curr[0]+1, curr[1]]

def checkDownLeft(curr):
    return [curr[0]+1, curr[1]-1]

def checkDownRight(curr):
    return [curr[0]+1, curr[1]+1]

def downOneStep(curr):
    global endlessVoid
    move = checkDown(curr)
    if move[0] > maxY or move[1] >= len(cave[0]) or move[1] < 0:
        endlessVoid = True
        return move
    whatsNext = cave[move[0]][move[1]]
    if whatsNext == '.':
        return move
    if whatsNext in ('#', 'o'):
        move = checkDownLeft(curr)
        if move[0] > maxY or move[1] >= len(cave[0]) or move[1] < 0:
            endlessVoid = True
            return move
        whatsNext = cave[move[0]][move[1]]
        if whatsNext == '.':
            return move
        if whatsNext in ('#', 'o'):
            move = checkDownRight(curr)
            if move[0] > maxY or move[1] >= len(cave[0]) or move[1] < 0:
                endlessVoid = True
                return move
            whatsNext = cave[move[0]][move[1]]
            if whatsNext == '.':
                return move
    cave[curr[0]][curr[1]] = 'o'
    return curr

unitsOfSand = 0

while not endlessVoid:
    sand = start
    while True:
        newPos = downOneStep(sand)
        if newPos == sand:
            break
        if endlessVoid:
            break
        if newPos[0] > maxY and (newPos[1] >= len(cave[0]) or newPos[1] < 0):
            endlessVoid = True
            break
        sand = newPos
    unitsOfSand += 1

# print(cave)

print(unitsOfSand-1)

# 715
# Duration: 0:00:00.282270

# Time of execution
print('Duration: {}'.format(datetime.now() - start_time))