import logging
from .enums import CardType
from .entity import Entity


class Action: # Lawsuit
	args = ()
	def __init__(self, target, *args, **kwargs):
		self.target = target
		self.times = 1
		self._args = args
		for k, v in zip(self.args, args):
			setattr(self, k, v)

	def __repr__(self):
		args = ["%s=%r" % (k, v) for k, v in zip(self.args, self._args)]
		return "<Action: %s(%s)>" % (self.__class__.__name__, ", ".join(args))

	def __mul__(self, value):
		self.times *= value
		return self

	def eval(self, selector, source, game):
		if isinstance(selector, Entity):
			return [selector]
		else:
			return selector.eval(game, source)

	def trigger(self, source, game):
		targets = self.eval(self.target, source, game)
		for i in range(self.times):
			logging.info("%r triggering %r targeting %r", source, self, targets)
			for target in targets:
				self.do(source, target, game)

class Buff(Action):
	args = ("id", )
	def do(self, source, target, game):
		source.buff(target, self.id)

class Bounce(Action):
	def do(self, source, target, game):
		target.bounce()

class Destroy(Action):
	def do(self, source, target, game):
		target.destroy()

class Discard(Action):
	def do(self, source, target, game):
		target.discard()

class Draw(Action):
	args = ("count", )
	def do(self, source, target, game):
		target.draw(self.count)

class ForceDraw(Action):
	args = ("cards", )
	def do(self, source, target, game):
		cards = self.eval(self.cards, source, game)
		for card in cards:
			target.draw(card)


class ForcePlay(Action):
	args = ("cards", )
	def do(self, source, target, game):
		cards = self.eval(self.cards, source, game)
		for card in cards:
			target.summon(card)


class FullHeal(Action):
	def do(self, source, target, game):
		source.heal(target, target.health)

class GainArmor(Action):
	args = ("amount", )
	def do(self, source, target, game):
		target.armor += self.amount

class Give(Action):
	args = ("id", )
	def do(self, source, target, game):
		target.give(self.id)

class GiveCharge(Action):
	def do(self, source, target, game):
		target.charge = True

class GiveDivineShield(Action):
	def do(self, source, target, game):
		target.divineShield = True

class GiveMana(Action):
	args = ("amount", )
	def do(self, source, target, game):
		target.maxMana += self.amount

class GiveStealth(Action):
	def do(self, source, target, game):
		target.stealthed = True

class GiveSparePart(Action):
	...

class GiveTaunt(Action):
	def do(self, source, target, game):
		target.taunt = True

class GiveWindfury(Action):
	def do(self, source, target, game):
		target.windfury = True

class Hit(Action):
	args = ("amount", )
	def do(self, source, target, game):
		if target.type == CardType.WEAPON:
			target.durability -= self.amount
		else:
			source.hit(target, self.amount)

class Heal(Action):
	args = ("amount", )
	def do(self, source, target, game):
		source.heal(target, self.amount)

class ManaThisTurn(Action):
	args = ("amount", )
	def do(self, source, target, game):
		target.tempMana += self.amount

class Mill(Action):
	args = ("count", )
	def do(self, source, target, game):
		target.mill(self.count)

class Morph(Action):
	args = ("id", )
	def do(self, source, target, game):
		target.morph(self.id)

class Freeze(Action):
	def do(self, source, target, game):
		target.freeze = True

class RemoveDivineShield(Action):
	def do(self, source, target, game):
		target.divineShield = False

class Reveal(Action):
	def do(self, source, target, game):
		target.reveal()

class Silence(Action):
	def do(self, source, target, game):
		target.silence()

class Summon(Action):
	args = ("id", )
	def do(self, source, target, game):
		target.summon(self.id)

class Swap(Action):
	args = ("other", )
	def do(self, source, target, game):
		other = self.eval(self.other, source, game)
		if other:
			assert len(other) == 1
			other = other[0]
			orig = target.zone
			target.zone = other.zone
			other.zone = orig

class TakeControl(Action):
	def do(self, source, target, game):
		source.controller.takeControl(target)

class Unstealth(Action):
	def do(self, source, target, game):
		target.stealthed = False
