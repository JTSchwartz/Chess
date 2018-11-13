from tkinter import *
from pieces import *

pieceMap = {}
board = [[0 for x in range(8)] for y in range(8)]


def init_pawns(row=True):
	row_num = 1 if row else 6

	for x in range(8):
		pieceMap[board[row_num][x]] = Pawn(board[row_num][x], row)

	if row:
		init_pawns(False)


def init_dups(piece, row=True):
	row_num = 0 if row else 7
	col = piece.origin_col

	pieceMap[board[row_num][col]] = piece(board[row_num][col], row)
	pieceMap[board[row_num][7 - col]] = piece(board[row_num][7 - col], row)

	if row:
		init_dups(piece, False)


def init_essential(row=True):
	row_num = 0 if row else 7

	pieceMap[board[row_num][3]] = King(board[row_num][3], row)
	pieceMap[board[row_num][4]] = Queen(board[row_num][4], row)

	if row:
		init_essential(False)


if __name__ == '__main__':

	for i in range(8):
		for j in range(8):
			board[i][j] = (i * 10) + j

	init_pawns()
	init_dups(Rook)
	init_dups(Knight)
	init_dups(Bishop)
	init_essential()

	print(board)

