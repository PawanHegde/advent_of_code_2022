from typing import List

from aocd import lines, submit


def _get_elf_totals() -> List[int]:
    elf_totals = []
    total_of_current_elf = 0
    for line in lines:
        if line == '':
            # We're done calculating for the current elf
            elf_totals.append(total_of_current_elf)
            total_of_current_elf = 0
            continue
        value = int(line)
        total_of_current_elf += value
    return elf_totals


def a():
    answer = max(_get_elf_totals())
    submit(answer, part="a")


def b():
    top_three_elves = sorted(_get_elf_totals())[-3:]
    answer = sum(top_three_elves)
    submit(answer, part="b")


a()
b()
