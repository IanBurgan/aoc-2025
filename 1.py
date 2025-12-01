#!/usr/bin/env python3

from math import ceil

import utils

lines = utils.parse_input("1.in")

part_one, part_two = 0, 0
position = 50
for rotation in lines:
    dir = rotation[0]
    amount = int(rotation[1:])
    if dir == "L":
        position -= amount
    elif dir == "R":
        position += amount

    if position >= 100:
        part_two += position // 100
    elif position < 0:
        part_two += ceil((-1 * position) / 100)

    position %= 100
    if position == 0:
        part_one += 1

print("Part One:", part_one)
print("Part Two:", part_two)
