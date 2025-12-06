#!/usr/bin/env python3

from collections import deque
from math import prod

import utils

lines = utils.parse_input("6.in")

part_one = 0
part_two = 0

symbols = deque(lines[-1].split())

nums = [line.split() for line in lines[:-1]]
problems = zip(*nums, symbols)

for problem in problems:
    if problem[-1] == "+":
        part_one += sum(int(x) for x in problem[:-1])
    elif problem[-1] == "*":
        part_one += prod(int(x) for x in problem[:-1])

cols = zip(*lines[:-1])
cols = ["".join(x).strip() for x in cols] + [""]  # add marker for last problem
problem = []
for x in cols:
    if x == "":
        symbol = symbols.popleft()
        if symbol == "+":
            part_two += sum(problem)
        elif symbol == "*":
            part_two += prod(problem)
        problem = []
    else:
        problem.append(int(x))

print("Part One:", part_one)
print("Part Two:", part_two)
