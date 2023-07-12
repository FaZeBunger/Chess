# Takes current Piece coordinates and computes whether the move is a possible
# move based on the type of Piece
#
# *Note:
#   This does not consider whether there are pieces in between the origin coordinate
#   and the destination coordinate for pieces like the queen, bishop, rook, or
#   in the case of the king, whether or not the piece is guarded or not and can
#   be taken

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


def PawnMove(x_diff, y_diff):
    # Note this does not take into consideration En Pessant, or capturing

    if 1 <= y_diff <= 2:
        return True
    return False


def QueenMove(x_diff, y_diff):
    return RookMove(x_diff, y_diff) or BishopMove(x_diff, y_diff)
