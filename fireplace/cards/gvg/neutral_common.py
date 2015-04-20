from ..utils import *


##
# Minions

# Cogmaster
class GVG_013:
	def atk(self, i):
		if self.controller.field.filter(race=Race.MECHANICAL):
			return i + 2
		return i


# Stonesplinter Trogg
class GVG_067:
	def CARD_PLAYED(self, player, card):
		if player is not self.controller and card.type == CardType.SPELL:
			return [Buff(SELF, "GVG_067a")]


# Burly Rockjaw Trogg
class GVG_068:
	def CARD_PLAYED(self, player, card):
		if player is not self.controller and card.type == CardType.SPELL:
			return [Buff(SELF, "GVG_068a")]


# Antique Healbot
class GVG_069:
	action = [Heal(FRIENDLY_HERO, 8)]


# Ship's Cannon
class GVG_075:
	def OWN_MINION_SUMMON(self, minion):
		if minion.race == Race.PIRATE:
			return [Hit(RANDOM_ENEMY_CHARACTER, 2)]


# Explosive Sheep
class GVG_076:
	deathrattle = [Hit(ALL_MINIONS, 2)]


# Mechanical Yeti
class GVG_078:
	deathrattle = [GiveSparePart(ALL_PLAYERS)]


# Clockwork Gnome
class GVG_082:
	deathrattle = [GiveSparePart(CONTROLLER)]


# Micro Machine
class GVG_103:
	# That card ID is not a mistake
	TURN_BEGIN = [Buff(SELF, "GVG_076a")]
