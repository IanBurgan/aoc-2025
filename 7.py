#!/usr/bin/env python3

from collections import defaultdict

import utils

lines = utils.parse_input("7.in")

origin = (0, 0)
grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "S":
            origin = (x, y)
        grid[(x, y)] = lines[y][x]

part_one = 0
part_two = 0

routes = defaultdict(int)
grid[(origin[0], origin[1] + 1)] = "|"
routes[(origin[0], origin[1] + 1)] += 1

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if grid[(x, y)] == "|":
            if grid[(x, y + 1)] == "^":
                grid[(x - 1, y + 1)] = "|"
                routes[(x - 1, y + 1)] += routes[(x, y)]
                grid[(x + 1, y + 1)] = "|"
                routes[(x + 1, y + 1)] += routes[(x, y)]

                part_one += 1
            elif grid[(x, y + 1)] == ".":
                grid[(x, y + 1)] = "|"
                routes[(x, y + 1)] += routes[(x, y)]
            elif grid[(x, y + 1)] == "|":
                routes[(x, y + 1)] += routes[(x, y)]

for x in range(len(lines[-1])):
    if grid[(x, len(lines[-1]) - 1)] == "|":
        part_two += routes[(x, len(lines[-1]) - 1)]

print("Part One:", part_one)
print("Part Two:", part_two)
