# https://adventofcode.com/2022/day/9
# --- Day 9: Rope Bridge ---
from datetime import datetime
start_time = datetime.now()

# Opening the file and reading it into a list.
with open('workfile09', encoding="utf-8") as f:
    seriesOfMotions = f.read().splitlines()
f.closed
#print(len(read_data))

#                N         NW        W        SW      S       SE      E       NE       Start
#                12        11        9        7       6       5       3       1        0
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, 0)] # (x, y)

visitedPositions = [] #[{'y': 0, 'x': 0}]
# visitedPositions = []
head = [0, 0]
tail = [0, 0]
#visitedPositions.append([0, 0])
visitedPositions.append({'y': tail[0], 'x': tail[1]})

# Is this new visited position for tail or what?
def updateVisitedPositions(pos):
    v = {'y': pos[0], 'x': pos[1]}
    if v not in visitedPositions:
    # if pos not in visitedPositions:
        # visitedPositions.append(pos)
        visitedPositions.append(v)
    return

def makeMotion(direction, steps):
    # global head
    for step in range(steps):
        match direction:
            case "R":
                head[1] += 1
            case "U":
                head[0] += 1
            case "L":
                head[1] -= 1
            case "D":
                head[0] -= 1
        updateTailPosition(direction)
    return

def updateTailPosition(direction):
    # global head
    # global tail
    # If head and tail remain close enough.
    for add_x, add_y in directions:
        n_x = tail[1] + add_x   # neighbour_x
        n_y = tail[0] + add_y   # neighbour_y
        neighbour = [n_y, n_x]
        if neighbour == head:
            # Head and tail are touching.
            return
    if (head[0] == tail[0] or head[1] == tail[1]):
        # Tail must move one step in the same direction as head.
        match direction:
            case "R":
                tail[1] += 1
            case "U":
                tail[0] += 1
            case "L":
                tail[1] -= 1
            case "D":
                tail[0] -= 1
        updateVisitedPositions(tail)
    else:
        # Head and tail aren't touching and aren't in the same row or column.
        # Diagonal move.
        match direction:
            case "R":
                tail[0] += (head[0] - tail[0])
                tail[1] += 1
            case "U":
                tail[0] += 1 #(head[0] - tail[0] - 1)
                tail[1] += (head[1] - tail[1])
            case "L":
                tail[0] += (head[0] - tail[0])
                tail[1] -= 1
            case "D":
                tail[0] -= 1
                tail[1] += (head[1] - tail[1])
        updateVisitedPositions(tail)
        return

for m in seriesOfMotions:
    move = m.split()
    makeMotion(move[0], int(move[1])) # Debug
    # == U 4 == v
    # == L 3 == v
    # == D 1 == v
    # == R 4 == v
    # == D 1 == 
    # == L 5 == 
    # == R 2 == 

print(len(visitedPositions))

# Time of execution
print('Duration: {}'.format(datetime.now() - start_time))

# 6642
# Duration: 0:00:00.914970 / 0:00:00.835121
