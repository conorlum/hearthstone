import Board
import random

class BoardCollector:

	def __init__(self, Board1, Board2):
		self.Board1 = Board1
		self.Board2 = Board2

	def __init__(self):
		self.Board1 = Board()
		self.Board2 = Board()

	def simulate(self):
		turn = first_turn()
		board1_queue = Board1.get_queue()
		board2_queue = Board2.get_queue()
		while(is_winner() is None):
			attacking_card = board1_queue.get()
			attacked_card = Board2.attackable_spaces()


	def attack(self):
		#define how a card attacks another



	def first_turn(self):
		if len(self.Board1) > len(self.Board2):
			return Board1
		if len(self.Board2) > len(self.Board1):
			return Board2
		return [Board1, Board2][random.randint(0,1)]

	def is_winner(self):
		if (self.Board1.is_empty() and not self.Board2.is_empty()):
			return Board1
		if (self.Board2.is_empty() and not self.Board1.is_empty()):
			return Board2
		return None