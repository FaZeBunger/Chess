#!/usr/bin/python3
import os
from game_logic import Coord
import PieceMoves


class Piece:
    def __init__(self, type, color):
        self.color = color
        self.type = type
        self.img = self.format_img()

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

    def swap(self):
        if self.color == 'black':
            return Piece(color="white", type=self.type)
        else:
            return Piece(color="black", type=self.type)

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
        self.board = [[Piece(color=None, type=' ')
                       for _ in range(8)] for _ in range(8)]
        self._initBoard()

    def _initBoard(self):
        self.board[0] = [
            Piece(color='black', type='R'), Piece(color='black', type='N'),
            Piece(color='black', type='B'), Piece(color='black', type='Q'),
            Piece(color='black', type='K'), Piece(color='black', type='B'),
            Piece(color='black', type='N'), Piece(color='black', type='R')
        ]
        self.board[-1] = [
            Piece(color='white', type='R'), Piece(color='white', type='N'),
            Piece(color='white', type='B'), Piece(color='white', type='Q'),
            Piece(color='white', type='K'), Piece(color='white', type='B'),
            Piece(color='white', type='N'), Piece(color='white', type='R')
        ]

        self.board[1] = [Piece(color='black', type='P') for _ in range(8)]
        self.board[-2] = [Piece(color='white', type='P') for _ in range(8)]

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
        start_coord, end_coord = Move[0], Move[1]

        # Check if the Piece can make the Move
        if not self.board[7-start_coord.y][start_coord.x].check_if_legal_move(start_coord, end_coord):
            return False

        self.board[7-end_coord.y][end_coord.x] = self.board[7 -
                                                            start_coord.y][start_coord.x]
        self.board[7 -
                   start_coord.y][start_coord.x] = Piece(color=None, type=' ')

        return True
