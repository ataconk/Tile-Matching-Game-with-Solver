import numpy as np


def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


def getColorandSize():
    size_of_board = get_non_negative_int("Please enter the size of board NxN, N:")  # noqa
    num_of_colors = get_non_negative_int("Please enter number of colors:")
    board = np.random.randint(low=1,
                              high=num_of_colors+1,
                              size=(size_of_board,
                                    size_of_board))
    return board
