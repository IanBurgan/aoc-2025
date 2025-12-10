#!/usr/bin/env python3

from collections import deque

import utils

lines = utils.parse_input("10.in")

part_one = 0
part_two = 0

for line in lines:
    parts = line.split()
    diagram = parts[0]
    buttons = parts[1:-1]
    joltage = parts[-1]

    diagram = diagram[1:-1]
    diagram = set(i for i, x in enumerate(diagram) if x == "#")

    buttons = [x[1:-1].split(",") for x in buttons]
    buttons = [tuple(map(int, x)) for x in buttons]

    q = deque([[x] for x in buttons])
    while q:
        curr = q.popleft()

        on_lights = set()
        for button in curr:
            for light in button:
                if light in on_lights:
                    on_lights.discard(light)
                else:
                    on_lights.add(light)

        if on_lights == diagram:
            part_one += len(curr)
            break

        for button in buttons:
            if button not in curr:
                q.append(curr + [button])

print(part_one)
# print("Part One:", part_one)
# print("Part Two:", part_two)
