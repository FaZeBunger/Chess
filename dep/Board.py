#!/usr/bin/python3
import os
from game_logic import Coord
import PieceMoves

BothKings = True


class Piece:
    def __init__(self, type, color, coords: Coord):
        self.color = color
        self.type = type
        self.img = self.format_img()
        self.coords = coords
        self.isFirstMove = True

    def check_if_legal_move(self, origin, dest):
        signed_x_diff = dest.x - origin.x
        signed_y_diff = dest.y - origin.y
        x_diff = abs(signed_x_diff)
        y_diff = abs(signed_y_diff)

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
                # Checks if Piece is trying to move backwards
                if self.color == 'white':
                    if signed_y_diff < 0:
                        return False
                else:
                    if signed_y_diff > 0:
                        return False
                # Checks if pawn is moving to the column next to it or not
                if -1 <= signed_x_diff <= 1:
                    if PieceMoves.PawnMove(x_diff, y_diff, self.isFirstMove):
                        self.isFirstMove = False
                        return True
                else:
                    return False
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

    def clearScreen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def draw(self):
        self.clearScreen()
        LINE = "   +---+---+---+---+---+---+---+---+"
        for line in range(9):
            print(LINE)
            if line != 8:
                LineWP = f"{8-line}: | {self.board[line][0].img} | {self.board[line][1].img} | {self.board[line][2].img} | {self.board[line][3].img} | {self.board[line][4].img} | {self.board[line][5].img} | {self.board[line][6].img} | {self.board[line][7].img} |"
                print(LineWP)

        print("     A   B   C   D   E   F   G   H")
        print()

    def makeMove(self, Move: (Coord, Coord)):
        (start_coord, end_coord) = Move[0], Move[1]
        x_diff = abs(start_coord.x - end_coord.x)
        # y_diff = abs(start_coord.y - end_coord.y)

        start_piece = self.board[7 - start_coord.y][start_coord.x]
        end_piece = self.board[7 - end_coord.y][end_coord.x]
        blank_piece = Piece(color=None, type=' ', coords=start_coord)

        # Check if the Piece can make the Move
        if start_piece.check_if_legal_move(start_coord, end_coord) is False:
            return False

        if start_piece.type != 'N':
            if start_piece.type != 'P':
                if start_piece.type != 'K':
                    if self.CheckBetween(start_coord, end_coord) is False:
                        return False

        if start_piece.type == 'P':
            if x_diff == 1:
                if end_piece.type == ' ':
                    return False

        if end_piece == 'K':
            self.gameOver(start_piece.color)

        self.board[7 - end_coord.y][end_coord.x] = start_piece
        self.board[7 - end_coord.y][end_coord.x].coords = end_coord
        self.board[7 - start_coord.y][start_coord.x] = blank_piece

        return True

    def CheckBetween(self, start_point, end_point):
        y_diff = abs(start_point.x - end_point.x)
        x_diff = abs(start_point.y - end_point.y)

        actual_start_y = 7 - start_point.y
        actual_end_y = 7 - end_point.y

        # Check if move is diagonal
        if x_diff == y_diff:
            # Get whether x and y should go up or down
            if start_point.x > end_point.x:
                x_step = -1
            else:
                x_step = 1

            if actual_start_y > actual_end_y:
                y_step = -1
            else:
                y_step = 1

            curr_x = start_point.x
            curr_y = actual_start_y

            # Diagonal length is the same as horizontal or vertical length
            for _ in range(x_diff):
                curr_x += x_step
                curr_y += y_step

                if self.board[curr_y][curr_x].type != ' ':
                    return False

            return True

        # Check for horizontal movement
        elif y_diff and not x_diff:
            current_row = actual_start_y

            if start_point.x > end_point.x:
                step = -1
            else:
                step = 1

            for current_col in range(start_point.x + step, end_point.x, step):
                if self.board[current_row][current_col].type != ' ':
                    return False

            return True

        # Check for vertical movement
        elif x_diff and not y_diff:
            current_col = start_point.x

            if actual_start_y > actual_end_y:
                step = -1
            else:
                step = 1

            for current_row in range(actual_start_y + step, actual_end_y, step):
                if self.board[current_row][current_col].type != ' ':
                    return False

            return True

    def gameOver(self, winner):
        global BothKings
        self.draw()
        BothKings = False
        print(f"{winner.capitalize()} wins!")
