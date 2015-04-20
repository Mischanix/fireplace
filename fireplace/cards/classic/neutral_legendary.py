from ..utils import *


# The Black Knight
class EX1_002:
	action = [Destroy(TARGET)]


# Bloodmage Thalnos
class EX1_012:
	deathrattle = [Draw(CONTROLLER, 1)]


# King Mukla
class EX1_014:
	action = [Give(OPPONENT, "EX1_014t"), Give(OPPONENT, "EX1_014t")]

# Bananas
class EX1_014t:
	action = [Buff("EX1_014te")]


# Sylvanas Windrunner
class EX1_016:
	deathrattle = [TakeControl(RANDOM_ENEMY_MINION)]


# Old Murk-Eye
class EX1_062:
	def atk(self, value):
		murlocs = self.game.board.filter(race=Race.MURLOC).exclude(self)
		return value + len(murlocs)


# Tinkmaster Overspark
class EX1_083:
	def action(self):
		choice = random.choice(("EX1_tk28", "EX1_tk29"))
		return [Morph(RANDOM_MINION, choice)]


# Lorewalker Cho
class EX1_100:
	def CARD_PLAYED(self, player, card):
		if card.type == CardType.SPELL:
			return [Give(player.opponent, card.id)]


# Cairne Bloodhoof
class EX1_110:
	deathrattle = [Summon(CONTROLLER, "EX1_110t")]


# Gelbin Mekkatorque
class EX1_112:
	def action(self):
		choice = random.choice(self.data.entourage)
		return [Summon(CONTROLLER, choice)]

# Homing Chicken
class Mekka1:
	OWN_TURN_BEGIN = [Destroy(SELF), Draw(CONTROLLER, 3)]

# Repair Bot
class Mekka2:
	OWN_TURN_END = [Heal(RANDOM(DAMAGED_CHARACTERS), 6)]

# Emboldener 3000
class Mekka3:
	OWN_TURN_END = [Buff(RANDOM_MINION, "Mekka3e")]

# Poultryizer
class Mekka4:
	OWN_TURN_BEGIN = [Morph(RANDOM_MINION, "Mekka4t")]


# Leeroy Jenkins
class EX1_116:
	action = [Summon(OPPONENT, "EX1_116t"), Summon(OPPONENT, "EX1_116t")]


# Baron Geddon
class EX1_249:
	OWN_TURN_END = [Hit(ALL_CHARACTERS - SELF, 2)]


# Ragnaros the Firelord
class EX1_298:
	OWN_TURN_END = [Hit(RANDOM_ENEMY_CHARACTER, 8)]


# Nat Pagle
class EX1_557:
	def OWN_TURN_BEGIN(self):
		if random.choice((0, 1)):
			return [Draw(CONTROLLER, 1)]


# Harrison Jones
class EX1_558:
	def action(self):
		weapon = self.controller.opponent.weapon
		if weapon:
			return [Draw(CONTROLLER, weapon.durability), Destroy(ENEMY_WEAPON)]


# Ysera
class EX1_572:
	def OWN_TURN_END(self):
		choice = random.choice(self.data.entourage)
		return [Give(CONTROLLER, choice)]

# Ysera Awakens
class DREAM_02:
	action = [Hit(ALL_CHARACTERS - FILTER(id="EX1_572"), 5)]

# Dream
class DREAM_04:
	action = [Bounce(TARGET)]

# Nightmare
class DREAM_05:
	action = [Buff(TARGET, "DREAM_05e")]

class DREAM_05e:
	# TODO
	def OWN_TURN_BEGIN(self):
		self.owner.destroy()


# The Beast
class EX1_577:
	deathratte = [Summon(OPPONENT, "EX1_finkle")]


# Illidan Stormrage
class EX1_614:
	OWN_CARD_PLAYED = [Summon(CONTROLLER, "EX1_614t")]


# Captain Greenskin
class NEW1_024:
	action = [Buff(FRIENDLY_WEAPON, "NEW1_024o")]


# Millhouse Manastorm
class NEW1_029:
	action = [Buff(ENEMY_HERO, "NEW1_029t")]

class NEW1_029t:
	cost = lambda self, i: 0

	def TURN_END(self, player):
		# TODO
		# Remove the buff at the end of the other player's turn
		if player is not self.owner.controller:
			self.destroy()

class NEW1_029ta:
	cost = lambda self, i: 0


# Deathwing
class NEW1_030:
	action = [Destroy(ALL_MINIONS - SELF), Discard(CONTROLLER_HAND)]


# Gruul
class NEW1_038:
	TURN_END = [Buff(SELF, "NEW1_038o")]


# Hogger
class NEW1_040:
	OWN_TURN_END = [Summon(CONTROLLER, "NEW1_040t")]


# Elite Tauren Chieftain
class PRO_001:
	def action(self):
		choice1 = random.choice(self.data.entourage)
		choice2 = random.choice(self.data.entourage)
		return [Give(CONTROLLER, choice1), Give(OPPONENT, choice2)]

# I Am Murloc
class PRO_001a:
	def action(self):
		return [Summon(CONTROLLER) * random.choice((3, 4, 5))]

# Rogues Do It...
class PRO_001b:
	action = [Hit(TARGET, 4), Draw(CONTROLLER, 1)]


# Power of the Horde
class PRO_001c:
	def action(self):
		choice = random.choice(self.data.entourage)
		return [Summon(CONTROLLER, choice)]
