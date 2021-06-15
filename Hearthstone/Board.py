import queue

class Board:

	def __init__(self):
		self.board = [7]
		for i in range(0,7):
			self.board[i] = None
		self.attacking = 0

	def add_card(self, Card c, int pos):
		if(slot_is_empty(pos)):
			self.board[pos] = c

	def is_empty(self):
		return len(self.board) == 0

	def slot_is_empty(self, int pos):
		return self.board[pos] is None

	def attacked(self):
		self.attacking += 1

	def attackable_spaces(self):
		space = []
		for i in range(0,7):
			if self.board[i] is not None:
				space.append(self.board[i])
		return space[random.randint(0,len(space))]

	def get_queue(self):
		q = queue.SimpleQueue()
		for card in self.board:
			q.put(card)
		return q


