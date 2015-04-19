"""
Targeting logic
"""

from enum import IntEnum
from .enums import Affiliation, CardType, PlayReq, Race, Zone


# Requirements-based targeting
def isValidTarget(self, target, requirements=None):
	if target.type == CardType.MINION:
		if target.dead:
			return False
		if target.stealthed and self.controller != target.controller:
			return False
		if target.immune and self.controller != target.controller:
			return False
		if self.type == CardType.SPELL and target.cantBeTargetedByAbilities:
			return False
		if self.type == CardType.HERO_POWER and target.cantBeTargetedByHeroPowers:
			return False

	if requirements is None:
		requirements = self.requirements

	for req, param in requirements.items():
		if req == PlayReq.REQ_MINION_TARGET:
			if target.type != CardType.MINION:
				return False
		elif req == PlayReq.REQ_FRIENDLY_TARGET:
			if target.controller != self.controller:
				return False
		elif req == PlayReq.REQ_ENEMY_TARGET:
			if target.controller == self.controller:
				return False
		elif req == PlayReq.REQ_DAMAGED_TARGET:
			if not target.damage:
				return False
		elif req == PlayReq.REQ_TARGET_MAX_ATTACK:
			if target.atk > param or 0:
				return False
		elif req == PlayReq.REQ_NONSELF_TARGET:
			if target is self:
				return False
		elif req == PlayReq.REQ_TARGET_WITH_RACE:
			if target.type != CardType.MINION or target.race != param:
				return False
		elif req == PlayReq.REQ_HERO_TARGET:
			if target.type != CardType.HERO:
				return False
		elif req == PlayReq.REQ_TARGET_MIN_ATTACK:
			if target.atk < param or 0:
				return False
		elif req == PlayReq.REQ_MUST_TARGET_TAUNTER:
			if not target.taunt:
				return False
		elif req == PlayReq.REQ_UNDAMAGED_TARGET:
			if target.damage:
				return False

		# fireplace reqs
		elif req == PlayReq.REQ_SPELL_TARGET:
			if target.type != CardType.SPELL:
				return False
		elif req == PlayReq.REQ_WEAPON_TARGET:
			if target.type != CardType.WEAPON:
				return False
		elif req == PlayReq.REQ_NO_MINIONS_PLAYED_THIS_TURN:
			if self.controller.minionsPlayedThisTurn:
				return False
		elif req == PlayReq.REQ_TARGET_HAS_BATTLECRY:
			if not target.hasBattlecry:
				return False
		elif req == PlayReq.REQ_SOURCE_IS_ENRAGED:
			if not self.enraged:
				return False
	return True


class Selector:
	"""
	A Forth-like program consisting of methods of Selector and members of
	IntEnum classes. The IntEnums must have appropriate test() methods
	    def test(self, entity)
	returning a boolean, true if entity matches the condition.
	"""
	class BreakLabel:
		# no-op:
		def __init__(self, selector, stack):
			pass

	def __init__(self, *args):
		self.program = []
		first = True
		for arg in args:
			self.program.append(arg)
			if not first:
				self.program.append(Selector._or)
			first = False

	def __repr__(self):
		prog = []
		for op in self.program:
			name = ""
			if hasattr(op, "__name__"):
				name = op.__name__
			elif isinstance(op, IntEnum):
				name = op.name
			else:
				name = repr(op)
			# breaks are just optimization -- filter them
			if "break" not in name.lower():
				prog.append(name.lstrip("_"))
		return "<{}: {}>".format(self.__class__.__name__, " ".join(prog))

	def __or__(self, other):
		result = Selector()
		result.program = self.program + [Selector._break_true] + other.program
		result.program += [Selector._or, Selector.BreakLabel]
		return result

	def __add__(self, other):
		result = Selector()
		result.program = self.program + [Selector._break_false] + other.program
		result.program += [Selector._and, Selector.BreakLabel]
		return result

	def __sub__(self, other):
		result = Selector()
		result.program = self.program + [Selector._break_false] + other.program
		result.program += [Selector._not, Selector._and, Selector.BreakLabel]
		return result

	def eval(self, entities, source):
		return [e for e in entities if self.test(e, source)]

	def test(self, entity, source):
		stack = []
		self.pc = 0
		while self.pc < len(self.program):
			op = self.program[self.pc]
			self.pc += 1
			if callable(op):
				op(self, stack)
			else:
				val = type(op).test(op, entity, source)
				stack.append(val)
		return stack[-1]

	# if stack has false, skips to the appropriate BreakLabel
	def _break_false(self, stack):
		if stack[-1] == False:
			self._break(stack)

	# same as _break_false, but if stack has true
	def _break_true(self, stack):
		if stack[-1] == True:
			self._break(stack)

	def _break(self, stack):
		depth = 1
		while self.pc < len(self.program):
			op = self.program[self.pc]
			if op == Selector._break_true or op == Selector._break_false:
				depth += 1
			if op == self.BreakLabel:
				depth -= 1
			self.pc += 1
			if depth == 0:
				break

	# boolean ops:
	def _and(self, stack):
		a = stack.pop()
		b = stack.pop()
		stack.append(a and b)

	def _or(self, stack):
		a = stack.pop()
		b = stack.pop()
		stack.append(a or b)

	def _not(self, stack):
		stack.append(not stack.pop())


class SelfSelector(Selector):
	...

SELF = SelfSelector()


class TargetSelector(Selector):
	...


class AdjacentSelector(Selector):
	...


class FilterSelector(Selector):
	def __init__(self, *args, **kwargs):
		super().__init__(*args)

FILTER = FilterSelector


class ZoneSelector(Selector):
	def __call__(self, *args):
		return self


class RandomSelector(Selector):
	def __call__(self, *args):
		return self

	def __mul__(self, other):
		return self

RANDOM = RandomSelector


SELF = SelfSelector()
TARGET = TargetSelector()
IN_PLAY = ZoneSelector(Zone.PLAY)
IN_DECK = ZoneSelector(Zone.DECK)
IN_HAND = ZoneSelector(Zone.HAND)
SELF_ADJACENT = AdjacentSelector(SELF)
TARGET_ADJACENT = AdjacentSelector(TARGET)

FRIENDLY = Selector(Affiliation.FRIENDLY)
ENEMY = Selector(Affiliation.HOSTILE)
CONTROLLED_BY_TARGET = Selector(Affiliation.TARGET)

ALL_PLAYERS = PLAYER = Selector(CardType.PLAYER)
CONTROLLER = ALL_PLAYERS + FRIENDLY
OPPONENT = ALL_PLAYERS + ENEMY

HERO = Selector(CardType.HERO)
MINION = Selector(CardType.MINION)
CHARACTER = MINION | HERO
WEAPON = Selector(CardType.WEAPON)
SPELL = Selector(CardType.SPELL)
SECRET = SPELL # TODO

DEMON = Selector(Race.DEMON)
MECH = Selector(Race.MECHANICAL)
MURLOC = Selector(Race.MURLOC)
PIRATE = Selector(Race.PIRATE)
TOTEM = Selector(Race.TOTEM)

CONTROLLER_HAND = IN_HAND(FRIENDLY)
CONTROLLER_DECK = IN_DECK(FRIENDLY)
OPPONENT_HAND = IN_HAND(ENEMY)
OPPONENT_DECK = IN_DECK(OPPONENT)

ALL_HEROES = IN_PLAY(HERO)
ALL_MINIONS = IN_PLAY(MINION)
ALL_CHARACTERS = IN_PLAY(CHARACTER)
ALL_WEAPONS = IN_PLAY(WEAPON)
ALL_SECRETS = IN_PLAY(SECRET)

FRIENDLY_HERO = IN_PLAY(FRIENDLY + HERO)
FRIENDLY_MINIONS = IN_PLAY(FRIENDLY + MINION)
FRIENDLY_CHARACTERS = IN_PLAY(FRIENDLY + CHARACTER)
FRIENDLY_WEAPON = IN_PLAY(FRIENDLY + WEAPON)
ENEMY_HERO = IN_PLAY(ENEMY + HERO)
ENEMY_MINIONS = IN_PLAY(ENEMY + MINION)
ENEMY_CHARACTERS = IN_PLAY(ENEMY + CHARACTER)
ENEMY_WEAPON = IN_PLAY(ENEMY + WEAPON)
ENEMY_SECRETS = ...

RANDOM_MINION = RANDOM(ALL_MINIONS)
RANDOM_CHARACTER = RANDOM(ALL_CHARACTERS)
RANDOM_FRIENDLY_MINION = RANDOM(FRIENDLY_MINIONS)
RANDOM_FRIENDLY_CHARACTER = RANDOM(FRIENDLY_CHARACTERS)
RANDOM_ENEMY_MINION = RANDOM(ENEMY_MINIONS)
RANDOM_ENEMY_CHARACTER = RANDOM(ENEMY_CHARACTERS)

DAMAGED_CHARACTERS = ...
