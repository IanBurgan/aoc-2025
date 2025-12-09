#!/usr/bin/env python3

from collections import defaultdict, deque
from math import sqrt
from operator import itemgetter

import utils

lines = utils.parse_input("8.in")


def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def get_circuits(
    connections: int,
    distances: list[tuple[int, tuple[int, int, int], tuple[int, int, int]]],
) -> tuple[list[int], tuple[tuple[int, int, int], tuple[int, int, int]]]:
    _distances = deque(distances)
    graph = defaultdict(list)
    last_pair = (_distances[0][1], distances[0][2])
    for _ in range(connections):
        _, a, b = _distances.popleft()
        graph[a].append(b)
        graph[b].append(a)
        last_pair = (a, b)

    circuits = []
    while len(graph) > 0:
        circuit = set()
        node, neighbors = graph.popitem()
        q = deque()
        q.append(node)
        q.extend(neighbors)
        while q:
            curr = q.popleft()
            circuit.add(curr)
            if curr in graph:
                q.extend(graph[curr])
                del graph[curr]

        circuits.append(len(circuit))
    return sorted(circuits, reverse=True), last_pair


boxes = []
for line in lines:
    boxes.append(tuple(int(x) for x in line.split(",")))

distances = []
for i, box_a in enumerate(boxes):
    for j, box_b in enumerate(boxes[i + 1 :]):
        d = dist(box_a, box_b)
        distances.append((d, box_a, box_b))

distances.sort(key=itemgetter(0))

circuits, last_pair = get_circuits(1000, distances)
part_one = circuits[0] * circuits[1] * circuits[2]

part_two = 0
lower, upper = 1000, len(distances)
while upper > lower:
    next = (lower + upper) // 2
    circuits, last_pair = get_circuits(next, distances)

    if len(circuits) == 1:
        upper = next - 1
    else:
        lower = next + 1

    part_two = last_pair[0][0] * last_pair[1][0]

print("Part One:", part_one)
print("Part Two:", part_two)
