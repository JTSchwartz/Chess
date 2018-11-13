class Piece:
	_black = True
	_white = False

	name = str
	id = int
	color = bool
	moves = list()
	moved_yet = False
	origin_col = int

	def __init__(self, id, color):
		self.id = id
		self.color = color


class Bishop(Piece):
	None


class King(Piece):
	None


class Knight(Piece):
	None


class Pawn(Piece):
	None


class Rook(Piece):
	None


class Queen(Piece):
	None
