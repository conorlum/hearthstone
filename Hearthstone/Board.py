import queue
import random
from Card import Card

class Board:

	def __init__(self):
		self.board = [None] * 7

	def import_board(self, board):
		self.board = [None] * 7
		for card in board:
			if card is not None:	
				self.board.append(Card(
					card.attack, 
					card.health, 
					divine_shield = card.divine_shield,
					poisonous = card.poisonous,
					reborn = card.reborn,
					windfury = card.windfury,
					taunt = card.taunt
				))
			else:
				self.board.append(card)

	def copy_board(self):
		ret = []
		for card in self.board:
			if card is not None:
				ret.append(Card(
					card.attack, 
					card.health, 
					divine_shield = card.divine_shield,
					poisonous = card.poisonous,
					reborn = card.reborn,
					windfury = card.windfury,
					taunt = card.taunt
				))
			else:
				ret.append(None)
		return ret

	def add_card(self, card, pos):
		if(self.slot_is_empty(pos)):
			self.board[pos] = card

	def amount_of_cards(self):
		return len(self.get_queue())

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

	def __str__(self):
		ret = ""
		for card in self.board:
			if card is not None:
				ret += str(card)
		return ret



