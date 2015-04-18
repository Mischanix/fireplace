from ..utils import *


# The Black Knight
class EX1_002:
	action = destroyTarget


# Bloodmage Thalnos
class EX1_012:
	deathrattle = drawCard


# King Mukla
class EX1_014:
	def action(self):
		self.controller.opponent.give("EX1_014t")
		self.controller.opponent.give("EX1_014t")

# Bananas
class EX1_014t:
	action = buffTarget("EX1_014te")


# Sylvanas Windrunner
class EX1_016:
	def deathrattle(self):
		if self.controller.opponent.field:
			self.controller.takeControl(random.choice(self.controller.opponent.field))


# Old Murk-Eye
class EX1_062:
	def atk(self, value):
		murlocs = self.game.board.filter(race=Race.MURLOC).exclude(self)
		return value + len(murlocs)


# Tinkmaster Overspark
class EX1_083:
	def action(self):
		targets = self.game.board
		if targets:
			random.choice(targets).morph(random.choice(("EX1_tk28", "EX1_tk29")))


# Lorewalker Cho
class EX1_100:
	def CARD_PLAYED(self, player, card):
		if card.type == CardType.SPELL:
			player.opponent.give(card.id)


# Cairne Bloodhoof
class EX1_110:
	deathrattle = summonMinion("EX1_110t")


# Gelbin Mekkatorque
class EX1_112:
	def action(self):
		self.controller.summon(random.choice(self.data.entourage))

# Homing Chicken
class Mekka1:
	def OWN_TURN_BEGIN(self):
		self.destroy()
		self.controller.draw(3)

# Repair Bot
class Mekka2:
	def OWN_TURN_END(self):
		targets = [target for target in self.game.characters if target.damage]
		if targets:
			self.heal(random.choice(targets), 6)

# Emboldener 3000
class Mekka3:
	def OWN_TURN_END(self):
		self.buff(random.choice(self.game.board), "Mekka3e")

# Poultryizer
class Mekka4:
	def OWN_TURN_BEGIN(self):
		random.choice(self.game.board).morph("Mekka4t")


# Leeroy Jenkins
class EX1_116:
	def action(self):
		self.controller.opponent.summon("EX1_116t")
		self.controller.opponent.summon("EX1_116t")


# Baron Geddon
class EX1_249:
	def action(self):
		for target in self.game.characters:
			if target is not self:
				self.hit(target, 2)


# Ragnaros the Firelord
class EX1_298:
	def OWN_TURN_END(self):
		self.hit(random.choice(self.controller.opponent.characters), 8)


# Nat Pagle
class EX1_557:
	def OWN_TURN_BEGIN(self):
		if random.choice((0, 1)):
			self.controller.draw()


# Harrison Jones
class EX1_558:
	def action(self):
		weapon = self.controller.opponent.weapon
		if weapon:
			self.controller.draw(weapon.durability)
			weapon.destroy()


# Ysera
class EX1_572:
	def OWN_TURN_END(self):
		self.controller.give(random.choice(self.data.entourage))

# Ysera Awakens
class DREAM_02:
	def action(self):
		for target in self.game.characters:
			if target.id != "EX1_572":
				self.hit(target, 5)

# Dream
class DREAM_04:
	action = bounceTarget

# Nightmare
class DREAM_05:
	action = buffTarget("DREAM_05e")

class DREAM_05e:
	def OWN_TURN_BEGIN(self):
		self.owner.destroy()


# The Beast
class EX1_577:
	def deathrattle(self):
		self.controller.opponent.summon("EX1_finkle")


# Illidan Stormrage
class EX1_614:
	def OWN_CARD_PLAYED(self, card):
		self.controller.summon("EX1_614t")


# Captain Greenskin
class NEW1_024:
	def action(self):
		if self.controller.weapon:
			self.buff(self.controller.weapon, "NEW1_024o")


# Millhouse Manastorm
class NEW1_029:
	def action(self):
		self.buff(self.controller.opponent.hero, "NEW1_029t")

class NEW1_029t:
	cost = lambda self, i: 0

	def TURN_END(self, player):
		# Remove the buff at the end of the other player's turn
		if player is not self.owner.controller:
			self.destroy()

class NEW1_029ta:
	cost = lambda self, i: 0


# Deathwing
class NEW1_030:
	def action(self):
		for target in self.game.board.exclude(self):
			target.destroy()
		self.controller.discardHand()


# Gruul
class NEW1_038:
	def TURN_END(self, player):
		self.buff(self, "NEW1_038o")


# Hogger
class NEW1_040:
	OWN_TURN_END = summonMinion("NEW1_040t")


# Elite Tauren Chieftain
class PRO_001:
	def action(self):
		self.controller.give(random.choice(self.data.entourage))
		self.controller.opponent.give(random.choice(self.data.entourage))

# I Am Murloc
class PRO_001a:
	def action(self):
		for i in range(random.choice((3, 4, 5))):
			self.controller.summon("PRO_001at")

# Rogues Do It...
class PRO_001b:
	def action(self, target):
		self.hit(target, 4)
		self.controller.draw()


# Power of the Horde
class PRO_001c:
	def action(self):
		self.controller.summon(random.choice(self.data.entourage))
