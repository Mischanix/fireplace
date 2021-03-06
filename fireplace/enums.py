from enum import IntEnum


class CardClass(IntEnum):
	INVALID = 0
	DEATHKNIGHT = 1
	DRUID = 2
	HUNTER = 3
	MAGE = 4
	PALADIN = 5
	PRIEST = 6
	ROGUE = 7
	SHAMAN = 8
	WARLOCK = 9
	WARRIOR = 10
	DREAM = 11
	COUNT = 12


class CardType(IntEnum):
	INVALID = 0
	GAME = 1
	PLAYER = 2
	HERO = 3
	MINION = 4
	SPELL = 5
	ENCHANTMENT = 6
	WEAPON = 7
	ITEM = 8
	TOKEN = 9
	HERO_POWER = 10


class Faction(IntEnum):
	INVALID = 0
	HORDE = 1
	ALLIANCE = 2
	NEUTRAL = 3


class Race(IntEnum):
	INVALID = 0
	BLOODELF = 1
	DRAENEI = 2
	DWARF = 3
	GNOME = 4
	GOBLIN = 5
	HUMAN = 6
	NIGHTELF = 7
	ORC = 8
	TAUREN = 9
	TROLL = 10
	UNDEAD = 11
	WORGEN = 12
	GOBLIN2 = 13
	MURLOC = 14
	DEMON = 15
	SCOURGE = 16
	MECHANICAL = 17
	ELEMENTAL = 18
	OGRE = 19
	PET = 20
	TOTEM = 21
	NERUBIAN = 22
	PIRATE = 23
	DRAGON = 24

	# Alias for PET
	BEAST = 20


class GameTag(IntEnum):
	TIMEOUT = 7
	TURN_START = 8
	STEP = 19
	TURN = 20
	FATIGUE = 22
	CURRENT_PLAYER = 23
	FIRST_PLAYER = 24
	RESOURCES_USED = 25
	RESOURCES = 26
	HERO_ENTITY = 27
	MAXHANDSIZE = 28
	STARTHANDSIZE = 29
	DEFENDING = 36
	PROPOSED_DEFENDER = 37
	ATTACKING = 38
	PROPOSED_ATTACKER = 39
	ATTACHED = 40
	EXHAUSTED = 43
	DAMAGE = 44
	HEALTH = 45
	ATK = 47
	COST = 48
	ZONE = 49
	CONTROLLER = 50
	OWNER = 51
	MAXRESOURCES = 176
	CARD_ID = 186
	DURABILITY = 187
	SILENCED = 188
	WINDFURY = 189
	TAUNT = 190
	STEALTH = 191
	SPELLPOWER = 192
	DIVINE_SHIELD = 194
	CHARGE = 197
	NEXT_STEP = 198
	CARDRACE = 200
	FACTION = 201
	CARDTYPE = 202
	FREEZE = 208
	ENRAGED = 212
	RECALL = 215
	DEATHRATTLE = 217
	BATTLECRY = 218
	SECRET = 219
	COMBO = 220
	CANT_ATTACK = 227
	CANT_BE_DAMAGED = 240
	FROZEN = 260
	COMBO_ACTIVE = 266
	CARD_TARGET = 267
	NUM_CARDS_PLAYED_THIS_TURN = 269
	OUTGOING_HEALING_ADJUSTMENT = 277
	ARMOR = 292
	MORPH = 293
	TEMP_RESOURCES = 295
	RECALL_OWED = 296
	NUM_ATTACKS_THIS_TURN = 297
	CURRENT_SPELLPOWER = 298
	CANT_BE_TARGETED_BY_ABILITIES = 311
	SHOULDEXITCOMBAT = 312
	CREATOR = 313
	NUM_MINIONS_PLAYED_THIS_TURN = 317
	CANT_BE_TARGETED_BY_HERO_POWERS = 332
	HEALTH_MINIMUM = 337
	OneTurnEffect = 338
	SILENCE = 339
	ImmuneToSpellpower = 349
	ADJACENT_BUFF = 350
	AURA = 362
	POISONOUS = 363
	TAG_AI_MUST_PLAY = 367
	NUM_MINIONS_PLAYER_KILLED_THIS_TURN = 368
	NUM_MINIONS_KILLED_THIS_TURN = 369
	AFFECTED_BY_SPELL_POWER = 370
	EXTRA_DEATHRATTLES = 371
	TOPDECK = 377
	SHOWN_HERO_POWER = 380
	POWERED_UP = 386
	FORGETFUL = 389
	NUM_TIMES_HERO_POWER_USED_THIS_GAME = 394
	LAST_CARD_PLAYED = 397
	NUM_CARDS_DRAWN_THIS_TURN = 399
	EVIL_GLOW = 401
	HIDE_COST = 402

	# flavor
	ELITE = 114
	CARD_SET = 183
	CLASS = 199
	RARITY = 203
	Collectible = 321

	# unused
	SUMMONED = 205
	AttackVisualType = 251
	DevState = 268
	ENCHANTMENT_BIRTH_VISUAL = 330
	ENCHANTMENT_IDLE_VISUAL = 331
	InvisibleDeathrattle = 335  # Hack for Bigglesworth/Worshipper
	GrantCharge = 355  # RFG
	HealTarget = 361  # Northshire Cleric

	# strings
	TRIGGER_VISUAL = 32
	CARDTEXT_INHAND = 184
	CARDNAME = 185
	CardTextInPlay = 252
	TARGETING_ARROW_TEXT = 325
	ARTISTNAME = 342
	FLAVORTEXT = 351
	HOW_TO_EARN = 364
	HOW_TO_EARN_GOLDEN = 365

	# Renamed
	DEATH_RATTLE = 217
	OVERKILL = 380


class PlayReq(IntEnum):
	REQ_MINION_TARGET = 1
	REQ_FRIENDLY_TARGET = 2
	REQ_ENEMY_TARGET = 3
	REQ_DAMAGED_TARGET = 4
	REQ_ENCHANTED_TARGET = 5
	REQ_FROZEN_TARGET = 6
	REQ_CHARGE_TARGET = 7
	REQ_TARGET_MAX_ATTACK = 8
	REQ_NONSELF_TARGET = 9
	REQ_TARGET_WITH_RACE = 10
	REQ_TARGET_TO_PLAY = 11
	REQ_NUM_MINION_SLOTS = 12
	REQ_WEAPON_EQUIPPED = 13
	REQ_ENOUGH_MANA = 14
	REQ_YOUR_TURN = 15
	REQ_NONSTEALTH_ENEMY_TARGET = 16
	REQ_HERO_TARGET = 17
	REQ_SECRET_CAP = 18
	REQ_MINION_CAP_IF_TARGET_AVAILABLE = 19
	REQ_MINION_CAP = 20
	REQ_TARGET_ATTACKED_THIS_TURN = 21
	REQ_TARGET_IF_AVAILABLE = 22
	REQ_MINIMUM_ENEMY_MINIONS = 23
	REQ_TARGET_FOR_COMBO = 24
	REQ_NOT_EXHAUSTED_ACTIVATE = 25
	REQ_UNIQUE_SECRET = 26
	REQ_TARGET_TAUNTER = 27
	REQ_CAN_BE_ATTACKED = 28
	REQ_ACTION_PWR_IS_MASTER_PWR = 29
	REQ_TARGET_MAGNET = 30
	REQ_ATTACK_GREATER_THAN_0 = 31
	REQ_ATTACKER_NOT_FROZEN = 32
	REQ_HERO_OR_MINION_TARGET = 33
	REQ_CAN_BE_TARGETED_BY_SPELLS = 34
	REQ_SUBCARD_IS_PLAYABLE = 35
	REQ_TARGET_FOR_NO_COMBO = 36
	REQ_NOT_MINION_JUST_PLAYED = 37
	REQ_NOT_EXHAUSTED_HERO_POWER = 38
	REQ_CAN_BE_TARGETED_BY_OPPONENTS = 39
	REQ_ATTACKER_CAN_ATTACK = 40
	REQ_TARGET_MIN_ATTACK = 41
	REQ_CAN_BE_TARGETED_BY_HERO_POWERS = 42
	REQ_ENEMY_TARGET_NOT_IMMUNE = 43
	REQ_ENTIRE_ENTOURAGE_NOT_IN_PLAY = 44
	REQ_MINIMUM_TOTAL_MINIONS = 45
	REQ_MUST_TARGET_TAUNTER = 46
	REQ_UNDAMAGED_TARGET = 47
	REQ_CAN_BE_TARGETED_BY_BATTLECRIES = 48
	REQ_STEADY_SHOT = 49
	REQ_MINION_OR_ENEMY_HERO = 50
	REQ_TARGET_IF_AVAILABLE_AND_DRAGON_IN_HAND = 51
	REQ_LEGENDARY_TARGET = 52
	REQ_FRIENDLY_MINION_DIED_THIS_TURN = 53
	REQ_DRAG_TO_PLAY = 54

	# Fireplace-specific
	REQ_SPELL_TARGET = -1
	REQ_WEAPON_TARGET = -2
	REQ_NO_MINIONS_PLAYED_THIS_TURN = -3
	REQ_TARGET_HAS_BATTLECRY = -4
	REQ_SOURCE_IS_ENRAGED = -5


class OptionType(IntEnum):
	PASS = 1
	END_TURN = 2
	POWER = 3


class PowType(IntEnum):
	FULL_ENTITY = 1
	SHOW_ENTITY = 2
	HIDE_ENTITY = 3
	TAG_CHANGE = 4
	ACTION_START = 5
	ACTION_END = 6
	CREATE_GAME = 7
	META_DATA = 8


class PowSubType(IntEnum):
	ATTACK = 1
	CONTINUOUS = 2
	POWER = 3
	SCRIPT = 4
	TRIGGER = 5
	DEATHS = 6
	PLAY = 7
	FATIGUE = 8
	ACTION = 99


class Step(IntEnum):
	INVALID = 0
	BEGIN_FIRST = 1
	BEGIN_SHUFFLE = 2
	BEGIN_DRAW = 3
	BEGIN_MULLIGAN = 4
	MAIN_BEGIN = 5
	MAIN_READY = 6
	MAIN_RESOURCE = 7
	MAIN_DRAW = 8
	MAIN_START = 9
	MAIN_ACTION = 10
	MAIN_COMBAT = 11
	MAIN_END = 12
	MAIN_NEXT = 13
	FINAL_WRAPUP = 14
	FINAL_GAMEOVER = 15
	MAIN_CLEANUP = 16
	MAIN_START_TRIGGERS = 17


class AuraType(IntEnum):
	PLAY_AURA = 1
	HAND_AURA = 2
	PLAYER_AURA = 3


class Rarity(IntEnum):
	INVALID = 0
	COMMON = 1
	FREE = 2
	RARE = 3
	EPIC = 4
	LEGENDARY = 5


class Zone(IntEnum):
	INVALID = 0
	PLAY = 1
	DECK = 2
	HAND = 3
	GRAVEYARD = 4
	REMOVEDFROMGAME = 5
	SETASIDE = 6
	SECRET = 7
