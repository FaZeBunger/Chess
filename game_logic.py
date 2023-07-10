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

    print((start_coords.x, start_coords.y), (end_coords.x, end_coords.y))
    input("waiting for input")

    return (start_coords, end_coords)
