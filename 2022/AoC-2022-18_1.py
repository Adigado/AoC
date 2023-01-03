# https://adventofcode.com/2022/day/18
# --- Day 18: Boiling Boulders ---
# Finally, 3-D.

from datetime import datetime
start_time = datetime.now()

# # Reading the file and splitting the lines into a list of lists.
with open('C:\\Users\\edo-wg\\Documents\\AoC\\2022\\input\\workfile18', encoding="utf-8") as f:
    scan = [[int(s) for s in line.strip().split(",")] for line in f]
f.closed
# print(len(scan))

# Test 0
# scan = [[1,1,1], [2,1,1]]
# Test 1
# scan = [[2,2,2],
#     [1,2,2],
#     [3,2,2],
#     [2,1,2],
#     [2,3,2],
#     [2,2,1],
#     [2,2,3],
#     [2,2,4],
#     [2,2,6],
#     [1,2,5],
#     [3,2,5],
#     [2,1,5],
#     [2,3,5]]

totalSurfaceArea = len(scan) * 6

def checkExposition(c1, c2):
    if (abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])) == 1:
        return 2
    else:
        return 0

for cube in scan:
    ind = scan.index(cube)
    for i in range(ind+1, len(scan)):
        totalSurfaceArea -= checkExposition(cube, scan[i])

print(totalSurfaceArea)

# 3650
# Duration: 0:00:03.166816

# Time of execution
print('Duration: {}'.format(datetime.now() - start_time))