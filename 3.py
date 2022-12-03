from typing import Set, Tuple, List

from aocd import lines, submit


# lines = [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw"
# ]


def _get_rucksacks() -> List[Tuple[Set[str], Set[str]]]:
    rucksacks = []
    for line in lines:
        length = len(line)
        first_compartment: Set[str] = set(line[:int(length / 2)])
        second_compartment: Set[str] = set(line[int(length / 2):])
        rucksacks.append((first_compartment, second_compartment))
    return rucksacks


def _spill(rucksack: Tuple[Set[str], Set[str]]) -> Set[str]:
    return rucksack[0].union(rucksack[1])


def score(character: str) -> int:
    if ord(character) > ord('a'):
        return ord(character) - ord('a') + 1
    return ord(character) - ord('A') + 27


def a():
    rucksacks = _get_rucksacks()
    answer = 0
    for left_compartment, right_compartment in rucksacks:
        common, = left_compartment.intersection(right_compartment)
        answer += score(common)
    submit(answer=answer, part="a")


def b():
    rucksacks = _get_rucksacks()
    answer = 0

    for index in range(0, len(rucksacks), 3):
        rucksack1 = _spill(rucksacks[index])
        rucksack2 = _spill(rucksacks[index + 1])
        rucksack3 = _spill(rucksacks[index + 2])

        common, = rucksack1.intersection(rucksack2).intersection(rucksack3)
        answer += score(common)

    submit(answer=answer, part="b")


a()
b()
