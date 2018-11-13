from tkinter import *
from pieces import *

pieceMap = {}
board = [[0 for x in range(8)] for y in range(8)]


def init_pawns(row):
	row_num = 1 if row else 6

	for x in range(8):
		pieceMap[board[row_num][x]] = Pawn(board[row_num][x], row)

	if row:
		init_pawns(False)


if __name__ == '__main__':

	for i in range(8):
		for j in range(8):
			board[i][j] = (i * 10) + j

	init_pawns(True)

	print(board)

