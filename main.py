import sys

sys.path.append("dep")

import game_logic
import Board

def mainLoop():
    global WhiteTurn
    global board

    board.draw()
    print("Syntax Example: e2e4")
    move = game_logic.getMove()

    if not move:
        mainLoop()

    start_pos = move[0]
    end_pos = move[1]

    curr_piece = board.board[7 - start_pos.y][start_pos.x]
    end_piece = board.board[7 - end_pos.y][end_pos.x]

    if not move:
        mainLoop()
        return

    # Check if it is correct turn for the piece
    if WhiteTurn:
        if curr_piece.color != "white":
            mainLoop()
            return

    else:
        if curr_piece.color != "black":
            mainLoop()
            return

    # Check if trying to take other piece
    if curr_piece.color == end_piece.color:
        mainLoop()
        return

    # If could not make move due to Illegal move, try again
    if not board.makeMove(move):
        mainLoop()
        return


if __name__ == "__main__":
    board = Board.ChessBoard()
    WhiteTurn = True
    for i in range(20):
        mainLoop()
        WhiteTurn = not WhiteTurn
    board.draw()
