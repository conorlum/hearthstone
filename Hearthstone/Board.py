import queue
import random

class Board:

	def __init__(self):
		self.board = [None] * 7

	def add_card(self, c, pos):
		if(self.slot_is_empty(pos)):
			self.board[pos] = c

	def amount_of_cards(self):
		return len(self.board)

	def is_empty(self):
		for card in self.board:
			if card is not None and card.is_alive():
				return False
		return True

	def slot_is_empty(self, pos):
		return self.board[pos] is None

	def attackable_space(self):
		space = []
		for i in range(0,len(self.board)-1):
			if self.board[i] is not None:
				space.append(self.board[i])
		return space[random.randint(0,len(space)-1)]

	def clean_board(self):
		for i in range(0,len(self.board)-1):
			if self.board[i] is not None and not self.board[i].is_alive():
				self.board.remove(self.board[i])

	def get_queue(self):
		ret = []
		for card in self.board:
			if card is not None:
				ret.append(card)
		return ret

	def print_board(self):
		for card in self.board:
			if card is not None:
				print(str(card.attack) + "," + str(card.health))



