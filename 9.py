#!/usr/bin/env python3

from itertools import combinations

import utils

lines = utils.parse_input("9.in")

red_tiles = []
for line in lines:
    x, y = line.split(",")
    red_tiles.append((int(x), int(y)))

part_one = 0
part_two = 0

edges = []
for i in range(len(red_tiles) - 1):
    a, b = red_tiles[i], red_tiles[i + 1]
    # sort pair to have leftmost / topmost point first
    if (a[0] == b[0] and a[1] > b[1]) or (a[0] == b[0] and a[1] > b[1]):
        a, b = b, a
    edges.append((a, b))

for a, b in combinations(red_tiles, 2):
    area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

    if area > part_one:
        part_one = area
    if area < part_two:
        continue

    x_bounds = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])
    y_bounds = (a[1], b[1]) if a[1] < b[1] else (b[1], a[1])

    # eliminate rectangle if another edge crosses
    invalid = False
    for start, end in edges:
        if (
            start[0] < x_bounds[1]
            and start[1] < y_bounds[1]
            and end[0] > x_bounds[0]
            and end[1] > y_bounds[0]
        ):
            invalid = True
            break

    if not invalid:
        part_two = area

print("Part One:", part_one)
print("Part Two:", part_two)
