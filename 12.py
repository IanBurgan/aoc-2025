#!/usr/bin/env python3

import utils

data = utils.read_file("12.in")
data = data.split("\n\n")

shape_sizes = [x.count("#") for x in data[:-1]]
lines = data[-1].splitlines()

part_one = 0

for line in lines:
    dims, counts = line.split(": ")
    dims = tuple(int(x) for x in dims.split("x"))
    counts = [int(x) for x in counts.split(" ")]

    have = dims[0] * dims[1]
    need = sum(x * s for x, s in zip(counts, shape_sizes))

    if need < have:
        part_one += 1

print("Part One:", part_one)
