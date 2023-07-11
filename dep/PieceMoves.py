def KingMove(x_diff, y_diff):
    if x_diff <= 1 and y_diff:
        return True
    return False


def BishopMove(x_diff, y_diff):
    if x_diff == y_diff:
        return True
    return False


def KnightMove(x_diff, y_diff):
    if [x_diff, y_diff].sort() == [1, 2]:
        return True
    return False


def RookMove(x_diff, y_diff):
    if y_diff == 0 or x_diff == 0:
        return True
    return False


def PawnMove(x_diff, y_diff, is_first_move):
    # Note this does not take into consideration En Pessant, or capturing

    if is_first_move:
        if 1 <= y_diff <= 2:
            return True
    elif y_diff == 1:
        return True

    return False


def QueenMove(x_diff, y_diff):
    return RookMove(x_diff, y_diff) or BishopMove(x_diff, y_diff)
