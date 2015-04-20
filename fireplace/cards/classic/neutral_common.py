from ..utils import *


##
# Free basic minions


# Frostwolf Warlord
class CS2_226:
	def action(self):
		count = len(self.controller.field) - 1
		return [Buff(SELF, "CS2_226e") * count]


# Voodoo Doctor
class EX1_011:
	action = [Heal(TARGET, 2)]


# Novice Engineer
class EX1_015:
	action = [Draw(CONTROLLER, 1)]


# Mad Bomber
class EX1_082:
	action = [Hit(RANDOM_CHARACTER, 1) * 3]


# Demolisher
class EX1_102:
	OWN_TURN_BEGIN = [Hit(RANDOM_ENEMY_CHARACTER, 2)]


# Arathi Weaponsmith
class EX1_398:
	action = [Summon(CONTROLLER, "EX1_398t")]


# Gurubashi Berserker
class EX1_399:
	SELF_DAMAGE = [Buff(SELF, "EX1_399e")]


# Nightblade
class EX1_593:
	action = [Hit(ENEMY_HERO, 3)]


# Cult Master
class EX1_595:
	OWN_MINION_DESTROY = [Draw(CONTROLLER, 1)]


##
# Common basic minions

# Earthen Ring Farseer
class CS2_117:
	action = [Heal(TARGET, 3)]


# Ironforge Rifleman
class CS2_141:
	action = [Hit(TARGET, 1)]


# Southsea Deckhand
class CS2_146:
	charge = lambda self, i: i or bool(self.controller.weapon)


# Gnomish Inventor
class CS2_147:
	action = [Draw(CONTROLLER, 1)]


# Stormpike Commando
class CS2_150:
	action = [Hit(TARGET, 2)]


# Silver Hand Knight
class CS2_151:
	action = [Summon("CS2_152")]


# Elven Archer
class CS2_189:
	action = [Hit(TARGET, 1)]


# Abusive Sergeant
class CS2_188:
	action = [Buff(TARGET, "CS2_188o")]


# Razorfen Hunter
class CS2_196:
	action = [Summon(CONTROLLER, "CS2_boar")]


# Darkscale Healer
class DS1_055:
	action = [Heal(FRIENDLY_CHARACTERS, 2)]


# Acolyte of Pain
class EX1_007:
	SELF_DAMAGE = [Draw(CONTROLLER, 1)]


# Shattered Sun Cleric
class EX1_019:
	action = [Buff(TARGET, "EX1_019e")]


# Dragonling Mechanic
class EX1_025:
	action = [Summon(CONTROLLER, "EX1_025t")]


# Leper Gnome
class EX1_029:
	deathrattle = [Hit(ENEMY_HERO, 2)]


# Dark Iron Dwarf
class EX1_046:
	action = [Buff(TARGET, "EX1_046e")]


# Spellbreaker
class EX1_048:
	action = [Silence(TARGET)]


# Youthful Brewmaster
class EX1_049:
	action = [Bounce(TARGET)]


# Ancient Brewmaster
class EX1_057:
	action = [Bounce(TARGET)]


# Acidic Swamp Ooze
class EX1_066:
	action = [Destroy(ENEMY_WEAPON)]


# Loot Hoarder
class EX1_096:
	deathrattle = [Draw(CONTROLLER, 1)]


# Frost Elemental
class EX1_283:
	action = [Freeze(TARGET)]


# Murloc Tidehunter
class EX1_506:
	action = [Summon(CONTROLLER, "EX1_506a")]


# Harvest Golem
class EX1_556:
	deathrattle = [Summon(CONTROLLER, "skele21")]


# Priestess of Elune
class EX1_583:
	action = [Heal(FRIENDLY_HERO, 4)]


# Bloodsail Raider
class NEW1_018:
	# TODO
	def action(self):
		if self.controller.weapon:
			self.buff(self, "NEW1_018e", atk=self.controller.weapon.atk)


# Dread Corsair
class NEW1_022:
	def cost(self, value):
		if self.controller.weapon:
			value -= self.controller.weapon.atk
		return value


# Flesheating Ghoul
class tt_004:
	MINION_DESTROY = [Buff(SELF, "tt_004o")]
