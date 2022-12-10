from bisect import bisect
from typing import List, Dict

from aocd import data, submit


# data = """addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop"""


def _parse() -> List[List[str]]:
    return [line.split() for line in data.splitlines()]


class Communicator:
    initial_register_value: int
    states: Dict[int, int]

    def __init__(self, instructions: List[List[str]], initial_register_value: int = 1):
        self.initial_register_value = initial_register_value

        register = initial_register_value
        step = 1
        self.states = {}  # Dictionaries are ordered in Python!!
        for instruction in instructions:
            match instruction:
                case ["noop"]:
                    step += 1
                case ["addx", value]:
                    step += 2
                    register += int(value)
                case unknown:
                    raise NotImplementedError("No support for " + str(unknown))
            self.states[step] = register

    def value_at(self, step: int):
        if step in self.states:
            return self.states[step]
        elif step <= 1:
            return self.initial_register_value

        keys = list(self.states.keys())
        previous_key = keys[bisect(keys, step) - 1]

        return self.states[previous_key]


def a():
    communicator = Communicator(_parse())

    answer = 0
    for step in range(20, 221, 40):
        answer += step * communicator.value_at(step)

    submit(answer, part="a")


def b():
    instructions = _parse()
    communicator = Communicator(instructions)

    for cycle in range(1, 241):
        pixel = (cycle - 1) % 40
        if pixel == 0:
            # New line
            print()

        x = communicator.value_at(cycle)
        if x - 1 <= pixel <= x + 1:
            print('#', end='')
        else:
            print(' ', end='')


a()
b()
