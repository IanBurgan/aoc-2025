#!/usr/bin/env python3

from collections import defaultdict, deque

import utils

lines = utils.parse_input("11.in")

part_one = 0
part_two = 0

graph = defaultdict(list)
for line in lines:
    key, out = line.split(': ')
    graph[key] += out.split(' ')

q = deque()
q.append(['you'])
while q:
    curr = q.popleft()
    for neighbor in graph[curr[-1]]:
        if neighbor == 'out':
            part_one += 1
        if neighbor not in curr:
            q.appendleft(curr + [neighbor])


print(graph)
print("Part One:", part_one)
print("Part Two:", part_two)
