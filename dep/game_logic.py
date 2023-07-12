class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getMove():
    move = input("Enter a Move: ")
    return parseMove(move)


def parseMove(Move: str):
    if len(Move) != 4:
        getMove()

    start, dest = Move[:2], Move[2:]

    start_coords = Coord(ord(start[0].upper()) - 65, int(start[1]) - 1)
    end_coords = Coord(ord(dest[0].upper()) - 65, int(dest[1]) - 1)

    if start_coords.x <= 0 or start_coords.y >= 8:
        return False
    if end_coords.x <= 0 or end_coords.y >= 8:
        return False

    input("Press Enter to Confirm")

    return (start_coords, end_coords)
