from aocd import lines, submit


def a():
    total = 0
    for line in lines:
        opponent_move, my_move = line.split(" ")

        opponent_index = 'ABC'.index(opponent_move)
        my_index = 'XYZ'.index(my_move)
        if my_index == (opponent_index + 1) % 3:  # Victory
            outcome_points = 6
        elif my_index == (opponent_index - 1) % 3:  # Loss
            outcome_points = 0
        else:
            outcome_points = 3

        choice_points = my_index + 1
        total += outcome_points + choice_points

    submit(total, part="a")


def b():
    total = 0
    for line in lines:
        opponent_move, my_move = line.split(" ")

        opponent_index = 'ABC'.index(opponent_move)
        my_index = 'XYZ'.index(my_move)

        outcome_points = 3 * my_index

        relative_choice = my_index - 1
        choice_points = (opponent_index + relative_choice) % 3 + 1

        total += outcome_points + choice_points
    submit(total, part="b")


a()
b()
