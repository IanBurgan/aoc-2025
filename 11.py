#!/usr/bin/env python3

from collections import defaultdict
from functools import cache

import utils

lines = utils.parse_input("11.in")

graph = defaultdict(list)
for line in lines:
    key, out = line.split(": ")
    graph[key] += out.split()

@cache
def routes(start: str, end: str):
    if start == end:
        return 1

    return sum(routes(neighbor, end) for neighbor in graph[start])


print("Part One:", routes("you", "out"))
print("Part Two:", routes("svr", "fft") * routes("fft", "dac") * routes("dac", "out"))
