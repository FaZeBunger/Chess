#!/usr/bin/python3
class Piece:
    def __init__(self, type, color):
        self.color = color
        self.type = type
        self.img = self.format_img()

    def swap(self):
        if self.color == 'black':
            return Piece(color="white", type=self.type)
        else:
            return Piece(color="black", type=self.type)

    def format_img(self):
        if self.color == 'black':
            return f"\033[31m{self.type}\033[37m"
        else:
            return self.type


class ChessBoard:
    def __init__(self):
        self.board = [[Piece(color=None, type=' ') for _ in range(8)] for _ in range(8)]
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
        print("     A   B   C   D   E   F   G   H")
        LINE = "   +---+---+---+---+---+---+---+---+"
        for line in range(9):
            print(LINE)
            if line != 8:

                LineWP = f"{8-line}: | {self.board[line][0].img} | {self.board[line][1].img} | {self.board[line][2].img} | {self.board[line][3].img} | {self.board[line][4].img} | {self.board[line][5].img} | {self.board[line][6].img} | {self.board[line][7].img} |"
                print(LineWP)


Board = ChessBoard()

Board.draw()
