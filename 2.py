#!/usr/bin/env python3

import re

import utils

lines = utils.parse_input("2.in", sep=",")

part_one = 0
part_two = 0

repeats_once = re.compile(r"^(.+)\1$")
repeats_once_or_more = re.compile(r"^(.+)\1+$")
for line in lines:
    ids = [int(x) for x in line.split("-")]

    for id in range(ids[0], ids[1] + 1):
        if repeats_once.match(str(id)):
            part_one += id
        if repeats_once_or_more.match(str(id)):
            part_two += id

print("Part One:", part_one)
print("Part Two:", part_two)
