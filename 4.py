#!/usr/bin/env python3

from collections import defaultdict

import utils

lines = utils.parse_input("4.in")

grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[(x, y)] = lines[y][x]

part_one = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if grid[(x,y)] != '@':
            continue

        adjacent_rolls = 0
        for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if grid[(x + d[0], y + d[1])] == '@':
                adjacent_rolls += 1

        if adjacent_rolls < 4:
            part_one += 1

part_two = 0
did_modify = True
while did_modify:
    did_modify = False
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if grid[(x,y)] != '@':
                continue

            adjacent_rolls = 0
            for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if grid[(x + d[0], y + d[1])] == '@':
                    adjacent_rolls += 1

            if adjacent_rolls < 4:
                grid[(x,y)] = '.'
                part_two += 1
                did_modify = True

print("Part One:", part_one)
print("Part Two:", part_two)
