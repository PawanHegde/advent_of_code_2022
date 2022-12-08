from typing import List, Set, Tuple

from aocd import data, submit


# data = """30373
# 25512
# 65332
# 33549
# 35390"""


def _parse() -> List[List[int]]:
    matrix = []
    for line in data.splitlines():
        matrix.append([int(digit) for digit in line])
    return matrix


def a():
    matrix = _parse()
    visible: Set[Tuple[int, int]] = set()

    for row in range(len(matrix)):
        # Visible from the left
        cur_max = -1
        for col in range(len(matrix[0])):
            if (value := matrix[row][col]) > cur_max:
                visible.add((row, col))
                cur_max = value

        # Visible from the right
        cur_max = -1
        for col in range(len(matrix[0]) - 1, -1, -1):
            if (value := matrix[row][col]) > cur_max:
                visible.add((row, col))
                cur_max = value

    for col in range(len(matrix[0])):
        # Visible from the top
        cur_max = -1
        for row in range(len(matrix)):
            if (value := matrix[row][col]) > cur_max:
                visible.add((row, col))
                cur_max = value

        # Visible from the bottom
        cur_max = -1
        for row in range(len(matrix) - 1, -1, -1):
            if (value := matrix[row][col]) > cur_max:
                visible.add((row, col))
                cur_max = value

    answer = len(visible)
    submit(answer, part='a')


def _calculate_score(matrix: List[List[int]], row: int, col: int) -> int:
    value = matrix[row][col]

    left = 0
    col_to_compare = col - 1
    while col_to_compare >= 0:
        left += 1
        if matrix[row][col_to_compare] >= value:
            break
        col_to_compare -= 1

    right = 0
    col_to_compare = col + 1
    while col_to_compare < len(matrix[0]):
        right += 1
        if matrix[row][col_to_compare] >= value:
            break
        col_to_compare += 1

    top = 0
    row_to_compare = row - 1
    while row_to_compare >= 0:
        top += 1
        if matrix[row_to_compare][col] >= value:
            break
        row_to_compare -= 1

    bottom = 0
    row_to_compare = row + 1
    while row_to_compare < len(matrix):
        bottom += 1
        if matrix[row_to_compare][col] >= value:
            break
        row_to_compare += 1

    return left * right * top * bottom


def b():
    matrix = _parse()

    row_count = len(matrix)
    col_count = len(matrix[0])

    max_value = -1
    for row in range(row_count):
        for col in range(col_count):
            if (score := _calculate_score(matrix, row, col)) > max_value:
                max_value = score

    answer = max_value
    submit(answer, part="b")


a()
b()
