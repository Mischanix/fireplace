from ..utils import *


##
# Minions

# Fire Elemental
class CS2_042:
	action = [Hit(TARGET, 3)]


# Unbound Elemental
class EX1_258:
	def OWN_CARD_PLAYED(self, card):
		if card.overload:
			return [Buff(SELF, "EX1_258e")]


# Mana Tide Totem
class EX1_575:
	OWN_TURN_END = [Draw(CONTROLLER, 1)]


# Windspeaker
class EX1_587:
	action = [GiveWindfury(TARGET)]


##
# Spells

# Frost Shock
class CS2_037:
	action = [Hit(TARGET, 1)]


# Ancestral Spirit
class CS2_038:
	action = [Buff(TARGET, "CS2_038e")]

class CS2_038e:
	def deathrattle(self):
		# TODO tests
		return [Summon(CONTROLLER, self.id)]


# Windfury
class CS2_039:
	action = [GiveWindfury(TARGET)]


# Ancestral Healing
class CS2_041:
	def action(self, target):
		return [Heal(TARGET, target.maxHealth), Buff(TARGET, "CS2_041e")]


# Rockbiter Weapon
class CS2_045:
	action = [Buff(TARGET, "CS2_045e")]


# Bloodlust
class CS2_046:
	action = [Buff(FRIENDLY_MINIONS, "CS2_046e")]


# Far Sight
class CS2_053:
	# TODO
	def action(self):
		card = self.controller.draw()
		self.buff(card, "CS2_053e")


# Lightning Bolt
class EX1_238:
	action = [Hit(TARGET, 3)]


# Lava Burst
class EX1_241:
	action = [Hit(TARGET, 5)]


# Totemic Might
class EX1_244:
	action = [Buff(FRIENDLY_MINIONS + TOTEM, "EX1_244e")]


# Hex
class EX1_246:
	action = [Morph(TARGET, "hexfrog")]


# Feral Spirit
class EX1_248:
	action = [Summon(CONTROLLER, "EX1_tk11"), Summon("EX1_tk11")]


# Forked Lightning
class EX1_251:
	action = [Hit(RANDOM_ENEMY_MINION * 2, 2)]


# Earth Shock
class EX1_245:
	action = [Silence(TARGET), Hit(TARGET, 1)]


# Lightning Storm
class EX1_259:
	# TODO
	def action(self):
		for target in self.controller.opponent.field:
			self.hit(target, random.choice((2, 3)))
