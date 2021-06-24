


class Card:
	
	def __init__(self, attack, health, divine_shield = False, poisonous = False, reborn = False, windfury = False, mega_windfury = False, taunt = False):
		self.attack = attack
		self.health = health
		self.divine_shield = divine_shield
		self.poisonous = poisonous
		self.reborn = reborn
		self.windfury = windfury
		self.mega_windfury = mega_windfury
		self.taunt = taunt
		self.was_reborn = False

	def take_damage(self, attacking_card):
		damage = attacking_card.attack

		if self.divine_shield:
			self.divine_shield = False
			return True

		if attacking_card.poisonous:
			self.health = 0
			return self.death()

		self.health -= damage
		if self.health < 0:
			 return self.death()

		return True

	def death(self):
		if self.reborn:
			self.health = 1
			self.reborn = False
			self.was_reborn = True
			self.trigger_deathrattle()
			return True
		self.trigger_deathrattle()
		return False

	def trigger_deathrattle(self):
		pass

	def is_alive(self):
		return self.health > 0

	def __str__(self):
		ret = "|" + str(self.attack) + "," + str(self.health) + "|"
		if self.taunt:
			ret = "!" + ret + "!"
		if self.divine_shield:
			ret = "(" + ret + ")"
		if self.poisonous:
			split = ret.split(",")
			ret = split[0] + "P," + split[1]
		if self.reborn:
			split = ret.split("|")
			ret = split[0] + "|" + split[1] + "R" + "|" +split[2]
		if self.windfury:
			split = ret.split(",")
			ret = split[0] + "W," + split[1]
		return ret + "  "
