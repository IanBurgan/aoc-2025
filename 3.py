#!/usr/bin/env python3

import utils

lines = utils.parse_input("3.in")

part_one = 0
part_two = 0

for line in lines:
    batteries = list(int(x) for x in line)

    first = max(batteries[:-1])
    start = batteries.index(first) + 1
    second = max(batteries[start:])
    part_one += (first * 10) + second

    joltage = 0
    start = 0
    for end in range(len(batteries) - 11, len(batteries) + 1):
        amount = max(batteries[start:end])
        joltage = (joltage * 10) + amount
        start = batteries.index(amount, start) + 1
    part_two += joltage

print("Part One:", part_one)
print("Part Two:", part_two)
