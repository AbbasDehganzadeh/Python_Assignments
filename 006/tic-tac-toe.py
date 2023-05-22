# a joyful game

players = tuple(("X", "O"))
boards = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # initial board game
######################################
# first, _ , last = boards
# print(first, last)
# for x in first:
# 	print(first, x)gg


def check_pos(col, row):
    """It checks whether the given position is empty or not"""
    if boards[col][row] == " ":
        return False
    return True


def check_win():
    """It checks whether the players won or not"""

    if (boards[0][0] == boards[0][1] == boards[0][2]) and boards[0][0] != " ":
        print("The player {} won!".format(boards[0][0]))
        return True
    if (boards[1][0] == boards[1][1] == boards[1][2]) and boards[1][0] != " ":
        print("The player {} won!".format(boards[1][0]))
        return True
    if (boards[2][0] == boards[2][1] == boards[2][2]) and boards[2][0] != " ":
        print("The player {} won!".format(boards[2][0]))
        return True
    if (boards[0][0] == boards[1][0] == boards[2][0]) and boards[0][0] != " ":
        print("The player {} won!".format(boards[0][0]))
        return True
    if (boards[0][1] == boards[1][1] == boards[2][1]) and boards[0][1] != " ":
        print("The player {} won!".format(boards[0][1]))
        return True
    if (boards[0][2] == boards[1][2] == boards[2][2]) and boards[0][2] != " ":
        print("The player {} won!".format(boards[0][2]))
        return True
    if (boards[0][0] == boards[1][1] == boards[2][2]) and boards[0][0] != " ":
        print("The player {} won!".format(boards[0][0]))
        return True
    if (boards[0][2] == boards[1][1] == boards[2][0]) and boards[1][1] != " ":
        print("The player {} won!".format(boards[0][2]))
        return True
    for board in boards:
        if " " in board:
            break
    else:
        print("\tThe game was drawn!")
        return True

    return False


def display():
    """It displays the screen for the players"""

    player = players[0] if role else players[1]
    for sq in boards:
        print("----" * 3)
        for i, k in enumerate(sq):
            print(f"| {k} ", end="")

        print("|")

    print("____" * 3)
    print("The current player {}".format(player)) if not done else " "


role = bool(0)  # first the opponent one
done = False  # for quitting the loop
while not done:
    message = "please enter two digits\tfirst for col and sec_ for row"
    C, R = input(message)
    c, r = int(C) - 1, int(R) - 1
    #    print(c, "\t", r)
    if not 0 <= c < 3 or r not in range(0, 3):
        print(
            "InvalidInput:\t The column {} and the row {} is \
            not correct".format(
                C, R
            )
        )
        continue
    mistake = check_pos(c, r)
    if not mistake:
        if role is True:
            boards[c][r] = players[1]
        else:
            boards[c][r] = players[0]

    role = not role
    done = check_win()
    display()  # It should be called last.
