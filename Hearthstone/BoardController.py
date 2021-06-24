from Board import Board
import random
import sys
import os
import time

class BoardController:

	def __init__(self, Board1, Board2):
		self.Board1 = Board1
		self.Board2 = Board2
		self.BOARD1 = Board1.copy_board()
		self.BOARD2 = Board2.copy_board()
		self.turn = self.first_turn()
	
	def blockPrint(self):
		sys.stdout = open(os.devnull, 'w')

	def enablePrint(self):
		sys.stdout = sys.__stdout__

	def big_simulate(self):
		board1win = 0
		board2win = 0
		tie = 0
		simulate_amount = 10000
		print("Simulating " + str(simulate_amount) + " times:")
		print("BOARD1:")
		print(self.Board1)
		print("BOARD2:")
		print(self.Board2)
		self.blockPrint()
		start_time = time.time()
		for i in range(0,simulate_amount):
			winner, board = self.simulate()
			self.reset()
			if winner == 2:
				tie += 1
			elif winner == 0:
				board1win += 1
			else:
				board2win += 1

		self.enablePrint()
		end_time = time.time()
		print("\nSimulation time: " + str(end_time - start_time) + " seconds")
		print(board1win/simulate_amount)
		print(board2win/simulate_amount)
		print(tie/simulate_amount)

	def reset(self):
		self.Board1.import_board(self.BOARD1)
		self.Board2.import_board(self.BOARD2)
		self.turn = self.first_turn()

	def simulate(self):
		attack_queue = self.get_board(self.turn).get_queue()
		defend_queue = self.get_board(self.other_turn()).get_queue()
		while(self.is_winner() == (-1, None)):
			self.board_states()
			attacker = attack_queue.pop(0)
			defender = self.get_board(self.other_turn()).attackable_space()
			attacker_alive, defender_alive = self.attack(attacker, defender)
			if attacker_alive:
				if attacker.was_reborn:
					attack_queue.insert(0,attacker)
				else:
					attack_queue.append(attacker)
			else:
				while attacker in attack_queue:
					attack_queue.remove(attacker)
				self.get_board(self.turn).clean_board()

			if not defender_alive:
				print("removing defender" + str(defender))
				defend_queue.remove(defender)
				self.get_board(self.other_turn()).clean_board()

			attack_queue, defend_queue = self.switch_queues(attack_queue, defend_queue)
		return self.is_winner()

	def board_states(self):
		print("BOARD 1:")
		print(self.Board1)
		print("BOARD 2:")
		print(self.Board2)

	def switch_queues(self, attack, defend):
		temp = attack
		attack = defend
		defend = temp
		self.turn = self.other_turn()
		return (attack,defend)

	def other_turn(self):
		return (self.turn+1)%2

	def get_board(self, b):
		return [self.Board1, self.Board2][b]

	def attack(self, attacking, defending):
		print("attacker of:" + str(attacking))
		print("defending:" + str(defending))
		defending.take_damage(attacking)
		attacking.take_damage(defending)
		return (attacking.is_alive(), defending.is_alive())

	def first_turn(self):
		if self.Board1.amount_of_cards() > self.Board2.amount_of_cards():
			return 0
		if self.Board2.amount_of_cards() > self.Board1.amount_of_cards():
			return 1
		return random.randint(0,1)

	def is_winner(self):
		if (self.Board2.is_empty() and not self.Board1.is_empty()):
			return (0, self.Board1)
		if (self.Board1.is_empty() and not self.Board2.is_empty()):
			return (1, self.Board2)
		if (self.Board1.is_empty() and self.Board2.is_empty()):
			return (2, None)
		return (-1, None)