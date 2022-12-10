from typing import List, Tuple, Set

from aocd import data, submit


# data = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""


def _parse() -> List[Tuple[str, int]]:
    instructions = []
    for line in data.splitlines():
        direction = line[0]
        steps = int(line[2:])
        instructions.append((direction, steps))

    return instructions


direction_vectors = {
    "R": 1,
    "L": -1,
    "U": 1j,
    "D": -1j
}


def _react(leader: complex, follower: complex) -> complex:
    distance = leader - follower
    if abs(distance.real) <= 1 and abs(distance.imag) <= 1:
        return follower

    horizontal = distance.real / abs(distance.real) if distance.real != 0 else 0
    vertical = distance.imag / abs(distance.imag) if distance.imag != 0 else 0
    return follower + horizontal + (vertical * 1j)


def a():
    instructions = _parse()
    unique_positions: Set[complex] = {0}

    h = 0
    t = 0

    for direction, steps in instructions:
        step = direction_vectors[direction]
        for _ in range(steps):
            h += step
            t = _react(h, t)
            unique_positions.add(t)

    answer = len(unique_positions)
    submit(answer, part="a")


def b():
    instructions = _parse()
    unique_positions: Set[complex] = {0}

    knots: List[complex] = [0] * 10

    for direction, steps in instructions:
        step = direction_vectors[direction]
        for _ in range(steps):
            knots[0] += step
            for knot_id in range(1, 10):
                knots[knot_id] = _react(knots[knot_id - 1], knots[knot_id])
            unique_positions.add(knots[9])
    answer = len(unique_positions)
    submit(answer, part="b")


a()
b()
