import re
from typing import List, Tuple, Dict

from aocd import lines, submit

# lines = [
#     "    [D]",
#     "[N] [C]",
#     "[Z] [M] [P]",
#     "1   2   3",
#     "",
#     "move 1 from 2 to 1",
#     "move 3 from 1 to 3",
#     "move 2 from 2 to 1",
#     "move 1 from 1 to 2",
# ]


class Instruction:
    number: int
    of: int
    to: int

    def __init__(self, data: Dict):
        self.number = int(data.get("number"))
        self.of = int(data.get("of")) - 1
        self.to = int(data.get("to")) - 1


def _parse() -> Tuple[List[List[str]], List[Instruction]]:
    parsed_initial_config = False
    initial_configs = []
    stacks = []
    instructions: List[Instruction] = []
    for line in lines:
        if not parsed_initial_config:
            parts = [line[i + 1:i + 2] for i in range(0, len(line), 4)]
            initial_configs.append(parts)

        if line == "":  # Time to build the stacks!
            parsed_initial_config = True

            stacks = []
            num_of_stacks = len(initial_configs[-2])
            for _ in range(num_of_stacks):
                stacks.append([])

            for config in list(reversed(initial_configs))[2:]:
                for index, value in enumerate(config):
                    if value != " ":
                        stacks[index].append(value)
            continue

        if parsed_initial_config:
            print(line)
            match = re.match(r"move (?P<number>\d+) from (?P<of>\d+) to (?P<to>\d+)", line)
            instruction = Instruction(match.groupdict())
            instructions.append(instruction)

    return stacks, instructions


def a():
    stacks, instructions = _parse()

    for instruction in instructions:
        for _ in range(instruction.number):
            popped_crate = stacks[instruction.of].pop()
            stacks[instruction.to].append(popped_crate)

    answer = "".join([stack[-1] for stack in stacks])
    submit(answer, part="a")


def b():
    stacks, instructions = _parse()

    for instruction in instructions:
        crates_to_pop = stacks[instruction.of][-instruction.number:]
        stacks[instruction.of] = stacks[instruction.of][:-instruction.number]
        stacks[instruction.to] += crates_to_pop

    answer = "".join([stack[-1] for stack in stacks])
    submit(answer, part="b")


a()
b()
