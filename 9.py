#!/usr/bin/env python3

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
    edges.append((a, b))
edges.append((red_tiles[-1], red_tiles[0]))

for i, a in enumerate(red_tiles):
    for b in red_tiles[i + 1 :]:
        if a[0] == b[0] or a[1] == b[1]:
            continue

        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        part_one = max(part_one, area)

        if area < part_two:
            continue

        x_bounds = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])
        y_bounds = (a[1], b[1]) if a[1] < b[1] else (b[1], a[1])

        # eliminate rectangle if another edge crosses
        invalid = False
        for edge in edges:
            start, end = edge
            if a in (start, end) or b in (start, end):
                continue

            left = max(start[0], end[0]) <= x_bounds[0]
            right = min(start[0], end[0]) >= x_bounds[1]
            above = max(start[1], end[1]) <= y_bounds[0]
            below = min(start[1], end[1]) >= y_bounds[1]

            if not (left or right or above or below):
                invalid = True
                break
        if invalid:
            continue

        part_two = area

print("Part One:", part_one)
print("Part Two:", part_two)
