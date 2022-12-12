import sys
from collections import deque
from typing import List, Tuple, Deque

from aocd import data, submit

# data = '''Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi'''


def _parse() -> Tuple[List[List[int]], complex, complex]:
    grid: List[List[int]] = []
    start: complex = 0
    end: complex = 0

    for row_num, line in enumerate(data.splitlines()):
        row: List[int] = []
        for col_num, character in enumerate(line):
            if character == 'S':
                value = 0
                start = row_num + 1j * col_num
            elif character == 'E':
                value = 25
                end = row_num + 1j * col_num
            else:
                value = ord(character) - ord('a')

            row.append(value)
        grid.append(row)
    return grid, start, end


def _calculate_steps_grid(grid: List[List[int]], origin: complex) -> List[List[int]]:
    steps_grid: List[List[int]] = []
    for _ in range(len(grid)):
        steps_grid.append([-1] * len(grid[0]))

    # Stores the coordinate and steps from origin
    # We traverse the grid in BFS one further step at a time while populating steps_grid
    queue: Deque[Tuple[complex, int]] = deque()
    queue.append((origin, 0))
    while len(queue) > 0:
        current, steps_to_current = queue.popleft()

        x = int(current.real)
        y = int(current.imag)

        if steps_grid[x][y] != -1:
            continue  # We have already visited this node. We can't do better now.

        steps_grid[x][y] = steps_to_current

        neighbors = [current + diff for diff in [-1, 1, -1j, 1j]]
        for neighbor in neighbors:
            nx, ny = int(neighbor.real), int(neighbor.imag)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) \
                    and grid[nx][ny] >= grid[x][y] - 1 \
                    and steps_grid[nx][ny] == -1:
                steps_to_neighbor = steps_to_current + 1
                queue.append((neighbor, steps_to_neighbor))

    return steps_grid


def a():
    grid, start, end = _parse()
    steps_grid = _calculate_steps_grid(grid, end)

    answer = steps_grid[int(start.real)][int(start.imag)]
    submit(answer, part='a')


def b():
    grid, start, end = _parse()
    steps_grid = _calculate_steps_grid(grid, end)

    closest = sys.maxsize
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 0 and steps_grid[i][j] > -1:
                closest = min(steps_grid[i][j], closest)

    submit(closest, part='b')


a()
b()
