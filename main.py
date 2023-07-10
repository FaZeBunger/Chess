import Board
import game_logic

if __name__ == "__main__":
    board = Board.ChessBoard()

    for i in range(2):
        board.draw()
        move = game_logic.getMove()
        board.makeMove(move)

    board.draw()
