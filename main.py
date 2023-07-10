class ChessBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        self.board[1] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
        self.board[-1] = self.board[0]
        self.board[-2] = self.board[1]

    def draw(self):
        print( "     A   B   C   D   E   F   G   H")
        LINE = "   +---+---+---+---+---+---+---+---+"
        for line in range(9):
            print(LINE)
            if line != 8:
                LineWP = f"{8-line}: | {self.board[line][0]} | {self.board[line][1]} | {self.board[line][2]} | {self.board[line][3]} | {self.board[line][4]} | {self.board[line][5]} | {self.board[line][6]} | {self.board[line][7]} |"
                print(LineWP)


Board = ChessBoard()

Board.draw()
