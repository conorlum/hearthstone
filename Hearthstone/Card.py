


class Card:
	
	def __init__(self, attack, health):
		self.attack = attack
		self.health = health

	def __init__(self, Card c):
		self.attack = c.attack
		self.health = c.health

	def take_damage(self, int damage):
		self.health -= damage
		if self.health < 0:
			 return False
		return True

	def alive(self):
		return self.health > 0

