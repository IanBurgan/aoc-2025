#!/usr/bin/env python3

from collections import defaultdict
from itertools import chain, combinations
from math import inf

import utils

lines = utils.parse_input("10.in")


def powerset(items: list[tuple[int, ...]]):
    return chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))


part_one = 0
part_two = 0

for i, line in enumerate(lines):
    parts = line.split()
    diagram = parts[0]
    buttons = parts[1:-1]
    joltage = parts[-1]

    diagram = frozenset(i for i, x in enumerate(diagram[1:-1]) if x == "#")

    buttons = [x[1:-1].split(",") for x in buttons]
    buttons = [tuple(map(int, x)) for x in buttons]

    joltage = tuple(int(x) for x in joltage[1:-1].split(","))

    solutions = defaultdict(list)
    for button_group in powerset(buttons):
        press_count = len(button_group)
        deltas = [0] * len(joltage)
        for button in button_group:
            for i in button:
                deltas[i] += 1

        odd_positions = frozenset(i for i, x in enumerate(deltas) if x % 2 != 0)
        solutions[odd_positions].append((press_count, deltas))
    part_one += min(x[0] for x in solutions[diagram])

    def solve(remaining: tuple[int, ...]) -> float:
        if sum(remaining) == 0:
            return 0

        result = inf
        odd_positions = frozenset(i for i, x in enumerate(remaining) if x % 2 != 0)
        for press_count, deltas in solutions[odd_positions]:
            next = tuple((x - y) // 2 for x, y in zip(remaining, deltas))
            if any(x < 0 for x in next):
                continue
            result = min(result, press_count + (2 * solve(next)))

        return result

    part_two += solve(joltage)

print("Part One:", part_one)
print("Part Two:", part_two)
