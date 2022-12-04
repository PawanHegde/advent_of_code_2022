from typing import Tuple

from aocd import lines, submit


#
# lines = [
#     "2-4,6-8",
#     "2-3,4-5",
#     "5-7,7-9",
#     "2-8,3-7",
#     "6-6,4-6",
#     "2-6,4-8",
# ]


class Range:
    start: int
    end: int

    def __init__(self, representation: str):
        start, end = representation.split("-")
        self.start = int(start)
        self.end = int(end)

    def contains(self, other: 'Range') -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: 'Range') -> bool:
        return (other.start <= self.start <= other.end) or (self.start <= other.start <= self.end)


def _parse(line: str) -> Tuple[Range, Range]:
    first, second = line.split(",")
    first = Range(first)
    second = Range(second)
    return first, second


def a():
    answer = 0
    for line in lines:
        first, second = _parse(line)
        if first.contains(second) or second.contains(first):
            answer += 1
    submit(answer, part="a")


def b():
    answer = 0
    for line in lines:
        first, second = _parse(line)
        if first.overlaps(second):
            answer += 1
    submit(answer, part="b")


a()
b()
