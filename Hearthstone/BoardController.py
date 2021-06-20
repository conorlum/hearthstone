import Board
import random

class BoardController:

	def __init__(self, Board1, Board2):
		self.Board1 = Board1
		self.Board2 = Board2
		self.turn = self.first_turn()
		
	def simulate(self):
		attack_queue = self.get_board(self.turn).get_queue()
		defend_queue = self.get_board(self.other_turn()).get_queue()
		while(self.is_winner() is None):
			self.board_states()
			attacker = attack_queue.pop(0)
			defender = self.get_board(self.other_turn()).attackable_space()
			attacker_alive, defender_alive = self.attack(attacker, defender)
			if attacker_alive: 
				attack_queue.append(attacker)
			else:
				self.get_board(self.turn).clean_board()

			if not defender_alive:
				defend_queue.remove(defender)
				self.get_board(self.other_turn()).clean_board()

			attack_queue, defend_queue = self.switch_queues(attack_queue, defend_queue)
		return self.is_winner()

	def board_states(self):
		print("BOARD 1:")
		self.Board1.print_board()
		print("BOARD 2:")
		self.Board2.print_board()

	def switch_queues(self, attack, defend):
		temp = attack
		attack = defend
		defend = temp
		return (attack,defend)

	def other_turn(self):
		return (self.turn+1)%2

	def get_board(self, b):
		return [self.Board1, self.Board2][b]

	def attack(self, attacking, defending):
		defending.take_damage(attacking.attack)
		attacking.take_damage(defending.attack)
		return (attacking.is_alive(), defending.is_alive())


	def first_turn(self):
		if self.Board1.amount_of_cards() > self.Board2.amount_of_cards():
			return 0
		if self.Board2.amount_of_cards() > self.Board1.amount_of_cards():
			return 1
		return random.randint(0,1)

	def is_winner(self):
		if (self.Board2.is_empty() and not self.Board1.is_empty()):
			print("BOARD 1 WON!")
			self.board_states()
			return self.Board1
		if (self.Board1.is_empty() and not self.Board2.is_empty()):
			print("BOARD 2 WON!")
			self.board_states()
			return self.Board2
		return None