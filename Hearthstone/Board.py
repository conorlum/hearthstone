import queue

class Board:

	def __init__(self):
		self.board = [7]
		for i in range(0,7):
			self.board[i] = None

	def add_card(self, c, pos):
		if(slot_is_empty(pos)):
			self.board[pos] = c

	def is_empty(self):
		return len(self.board) == 0

	def slot_is_empty(self, pos):
		return self.board[pos] is None

	def attackable_spaces(self):
		space = []
		for i in range(0,7):
			if self.board[i] is not None:
				space.append(self.board[i])
		return space[random.randint(0,len(space))]


