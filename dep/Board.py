#!/usr/bin/python3
import os
from game_logic import Coord
import PieceMoves


class Piece:
    def __init__(self, type, color, coords: Coord):
        self.color = color
        self.type = type
        self.img = self.format_img()
        self.coords = coords

    def check_if_legal_move(self, origin, dest):
        x_diff = abs(dest.x - origin.x)
        y_diff = abs(dest.y - origin.y)
        match self.type:

            case 'K':
                return PieceMoves.KingMove(x_diff, y_diff)
            case 'Q':
                return PieceMoves.QueenMove(x_diff, y_diff)
            case 'B':
                return PieceMoves.BishopMove(x_diff, y_diff)
            case 'N':
                return PieceMoves.KnightMove(x_diff, y_diff)
            case 'R':
                return PieceMoves.RookMove(x_diff, y_diff)
            case 'P':
                return PieceMoves.PawnMove(x_diff, y_diff)
            case _:
                print("There is no piece on this square")

    def coords_as_tuple(self):
        return (self.coords.x, self.coords.y)

    def swap(self):
        if self.color == 'black':
            return Piece(color="white", type=self.type, coords=self.coords)
        else:
            return Piece(color="black", type=self.type, coords=self.coords)

    def format_img(self):
        if self.color == 'black':
            return self.paint_black()
        else:
            return self.type

    def paint_black(self):
        out = f"\033[31m{self.type}\033[37m"
        return out


class ChessBoard:
    def __init__(self):
        self.board = [[Piece(color=None, type=' ', coords=Coord(x, y))
                       for x in range(8)] for y in range(8)]
        self._initBoard()

    def _initBoard(self):
        self.board[0] = [
            Piece(color='black', type='R', coords=Coord(0, 0)),
            Piece(color='black', type='N', coords=Coord(0, 1)),
            Piece(color='black', type='B', coords=Coord(0, 2)),
            Piece(color='black', type='Q', coords=Coord(0, 3)),
            Piece(color='black', type='K', coords=Coord(0, 4)),
            Piece(color='black', type='B', coords=Coord(0, 5)),
            Piece(color='black', type='N', coords=Coord(0, 6)),
            Piece(color='black', type='R', coords=Coord(0, 7))
        ]
        self.board[-1] = [
            Piece(color='white', type='R', coords=Coord(-1, 0)),
            Piece(color='white', type='N', coords=Coord(-1, 1)),
            Piece(color='white', type='B', coords=Coord(-1, 2)),
            Piece(color='white', type='Q', coords=Coord(-1, 3)),
            Piece(color='white', type='K', coords=Coord(-1, 4)),
            Piece(color='white', type='B', coords=Coord(-1, 5)),
            Piece(color='white', type='N', coords=Coord(-1, 6)),
            Piece(color='white', type='R', coords=Coord(-1, 7))
        ]

        self.board[1] = [Piece(color='black', type='P',
                               coords=Coord(x, 1)) for x in range(8)]
        self.board[6] = [Piece(color='white', type='P',
                               coords=Coord(x, 6)) for x in range(8)]

    def draw(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("     A   B   C   D   E   F   G   H")
        LINE = "   +---+---+---+---+---+---+---+---+"
        for line in range(9):
            print(LINE)
            if line != 8:
                LineWP = f"{8-line}: | {self.board[line][0].img} | {self.board[line][1].img} | {self.board[line][2].img} | {self.board[line][3].img} | {self.board[line][4].img} | {self.board[line][5].img} | {self.board[line][6].img} | {self.board[line][7].img} |"

                print(LineWP)

    def makeMove(self, Move: (Coord, Coord)):
        (start_coord, end_coord) = Move[0], Move[1]

        start_piece = self.board[7 - start_coord.y][start_coord.x]
        end_piece = self.board[7 - end_coord.y][end_coord.x]
        blank_piece = Piece(color=None, type=' ', coords=start_coord)

        # Check if the Piece can make the Move
        if not start_piece.check_if_legal_move(start_coord, end_coord):
            return False

        print(f"Old coords: {start_piece.coords_as_tuple()}")

        self.board[7 - end_coord.y][end_coord.x] = start_piece
        end_piece.coords = Coord(end_coord.x, end_coord.y)
        self.board[7 - start_coord.y][start_coord.x] = blank_piece

        print(f"New Coords: {end_piece.coords_as_tuple()}")
        input()

        return True
