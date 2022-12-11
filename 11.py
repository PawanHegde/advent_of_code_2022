import re
from math import prod
from typing import Callable, List, Tuple, Dict

from aocd import data, submit


# data = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3
#
# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0
#
# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3
#
# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""


class Monkey:
    id: int
    items: List[int]
    inspect_count: int

    # For the operation
    operator: str  # + or *
    operand: str

    test_divisor: int
    throw_test: Callable[[int], int]

    def __init__(self, lines: List[str]):
        self.id = int(re.match(r'Monkey (\d+)', lines[0])[1])
        self.items = [int(item) for item in re.findall(r'\d+', lines[1])]
        self.inspect_count = 0

        expression = (re.findall(r'Operation: new = old (.*)', lines[2])[0]).split()
        self.operator = expression[0]
        self.operand = expression[1]

        self.test_divisor = int(re.findall(r'Test: divisible by (\d+)', lines[3])[0])
        monkey_if_true = int(re.findall(r'(\d+)', lines[4])[0])
        monkey_if_false = int(re.findall(r'(\d+)', lines[5])[0])
        self.throw_test = lambda value: monkey_if_true if value % self.test_divisor == 0 else monkey_if_false

    def add_item(self, item: int):
        self.items.append(item)

    def get_inspect_count(self):
        return self.inspect_count

    def operate(self, worry_reducer: Callable[[int], int] = lambda worry: worry / 3) -> List[Tuple[int, int]]:
        results = []
        for item in self.items:
            self.inspect_count += 1

            # Apply the operation
            argument = item if self.operand == 'old' else int(self.operand)
            if self.operator == '*':
                item *= argument
            elif self.operator == '+':
                item += argument
            else:
                raise NotImplementedError()

            item = worry_reducer(item)

            recipient = self.throw_test(item)
            results.append((recipient, item))

        # All items will be empty once this monkey's turn is over
        self.items = []

        return results

    def __repr__(self):
        return f'Items={self.items}; Inspected={self.inspect_count}'


def _parse() -> Dict[int, Monkey]:
    lines = data.splitlines()
    monkeys = []
    for i in range(0, len(lines), 7):
        monkeys.append(Monkey(lines[i:i + 6]))
    return {monkey.id: monkey for monkey in monkeys}


def a():
    monkeys: Dict[int, Monkey] = _parse()

    for _ in range(20):
        for monkey in monkeys.values():
            results = monkey.operate()
            for recipient, item in results:
                monkeys[recipient].add_item(item)

    naughtiest = sorted(monkeys.values(), key=lambda mk: mk.get_inspect_count())[-2:]
    answer = prod((mk.get_inspect_count() for mk in naughtiest))
    submit(answer, part="a")


def b():
    monkeys: Dict[int, Monkey] = _parse()

    # The optimal solution would be to find the least-common-multiple, but bah.
    common_divisor: int = prod(mk.test_divisor for mk in monkeys.values())

    for i in range(10000):
        for monkey in monkeys.values():
            results = monkey.operate(worry_reducer=lambda worry: worry % common_divisor)
            for recipient, item in results:
                monkeys[recipient].add_item(item % common_divisor)

    naughtiest = sorted(monkeys.values(), key=lambda mk: mk.get_inspect_count())[-2:]
    answer = prod((mk.get_inspect_count() for mk in naughtiest))
    submit(answer, part="b")


a()
b()
