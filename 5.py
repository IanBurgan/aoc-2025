#!/usr/bin/env python3

from operator import itemgetter

import utils

lines = utils.parse_input("5.in", groups=True)

ranges = lines[0]
ranges = [x.split("-") for x in ranges]
ranges = [(int(x[0]), int(x[1])) for x in ranges]
ranges = sorted(ranges, key=itemgetter(0))
ingredients = [int(x) for x in lines[1]]

part_one = 0
for ingredient in ingredients:
    for r in ranges:
        low, high = r
        if low <= ingredient <= high:
            part_one += 1
            break

part_two = 0
seen = set()
for r in ranges:
    low, high = r
    for x in seen:
        seen_low, seen_high = x
        if seen_low <= low <= seen_high:
            low = seen_high + 1
        if seen_low <= high <= seen_high:
            high = seen_low - 1

    if low <= high:
        part_two += (high - low) + 1

    seen.add(r)

print("Part One:", part_one)
print("Part Two:", part_two)
