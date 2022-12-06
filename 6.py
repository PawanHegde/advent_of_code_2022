from collections import deque

from aocd import data, submit

# data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"


def a():
    window = deque()
    answer = None
    for index, character in enumerate(data):
        if len(window) == 4:
            window.popleft()
        window.append(character)
        if len(set(window)) == 4:
            answer = index + 1
            break
    submit(answer, part="a")


def b():
    window = deque()
    answer = None
    for index, character in enumerate(data):
        if len(window) == 14:
            window.popleft()
        window.append(character)
        if len(set(window)) == 14:
            answer = index + 1
            break

    submit(answer, part="b")


a()
b()
