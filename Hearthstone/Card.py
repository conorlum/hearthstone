


class Card:
	
	def __init__(self, attack, health):
		self.attack = attack
		self.health = health

	def take_damage(self, damage):
		self.health -= damage
		if self.health < 0:
			 return False
		return True

	def is_alive(self):
		return self.health > 0

	def __str__(self):
		return "(" + str(self.attack) + "," + str(self.health) + ")  "

