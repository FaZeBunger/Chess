class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def debug(self):
        return (self.x, self.y)


def getMove():
    move = input("Enter a Move: ")
    return parseMove(move)


def parseMove(Move: str):
    if len(Move) != 4:
        getMove()
        return

    start, dest = Move[:2], Move[2:]

    input(f"Start: {start}  End: {dest}")
    start_coords = Coord(ord(start[0].upper()) - 65, int(start[1]) - 1)
    end_coords = Coord(ord(dest[0].upper()) - 65, int(dest[1]) - 1)

    if start_coords.x < 0 or start_coords.x >= 8:
        return False

    if start_coords.y < 0 or start_coords.y >= 8:
        return False

    if end_coords.x < 0 or end_coords.x >= 8:
        return False

    if end_coords.y < 0 or end_coords.y >= 8:
        return False

    print(f"Start: {start_coords.debug()}   End: {end_coords.debug()}")
    input("Press Enter to Confirm")

    return (start_coords, end_coords)
