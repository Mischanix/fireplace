from ..utils import *


##
# Minions

# Attack Mode (Anodized Robo Cub)
class GVG_030a:
	action = [Buff(SELF, "GVG_030ae")]

# Tank Mode (Anodized Robo Cub)
class GVG_030b:
	action = [Buff(SELF, "GVG_030be")]


# Gift of Mana (Grove Tender)
class GVG_032a:
	# TODO
	def action(self):
		for player in self.game.players:
			player.maxMana += 1
			player.usedMana -= 1

# Gift of Cards (Grove Tender)
class GVG_032b:
	action = [Draw(ALL_PLAYERS, 1)]


# Druid of the Fang
class GVG_080:
	def action(self):
		if self.poweredUp:
			return [Morph(SELF, "GVG_080t")]


##
# Spells

# Tree of Life
class GVG_033:
	action = [FullHeal(ALL_CHARACTERS)]
