import Board
import random

class BoardController:

	def __init__(Board1, Board2):
		self.Board1 = Board1
		self.Board2 = Board2
		self.turn = first_turn()

	def __init__(self):
		self.Board1 = Board()
		self.Board2 = Board()

	def simulate(self):
		attack_queue = get_board(turn)
		defend_queue = get_board(other_turn())
		while(is_winner() is None):
			attacker = attack_queue.pop(0)
			defender = get_board(other_turn).attackable_spaces()
			attacker_alive, defender_alive = attack(attacker, defender)
			if attacker_alive: 
				attack_queue.append(attacker)
			if not defender_alive:
				defend_queue.remove(defender)

			attack_queue, defend_queue = switch_queues(attack_queue, defend_queue)
		return is_winner()

	def switch_queues(self, attack, defend):
		temp = attack
		attack = defend
		defend = temp
		return (attack,defend)

	def other_turn(self):
		return (self.turn+1)%2

	def get_board(b):
		return [Board1, Board2][b]

	def attack(self, attacking, defending):
		defending.take_damage(attacking.attack)
		attacking.take_damage(defending.attack)
		return (attacking.is_alive(), defending.is_alive())


	def first_turn(self):
		if len(self.Board1) > len(self.Board2):
			return 0
		if len(self.Board2) > len(self.Board1):
			return 1
		return [random.randint(0,1)]

	def is_winner(self):
		if (self.Board1.is_empty() and not self.Board2.is_empty()):
			print("BOARD 1 WON!")
			return Board1
		if (self.Board2.is_empty() and not self.Board1.is_empty()):
			print("BOARD 2 WON!")
			return Board2
		return None