import logging
import random
from itertools import chain
from .card import Card, THE_COIN
from .entity import Entity
from .enums import CardType, PowSubType, Step, Zone
from .managers import GameManager
from .utils import CardList


class Game(Entity):
	MAX_MINIONS_ON_FIELD = 8
	Manager = GameManager

	def __init__(self, players):
		super().__init__()
		self.players = players
		for player in players:
			player.game = self
		self.step = Step.BEGIN_FIRST
		self.turn = 0
		self.currentPlayer = None
		self.auras = []

	def __repr__(self):
		return "<%s %s>" % (self.__class__.__name__, self)

	def __str__(self):
		if not hasattr(self, "players"):
			return "Uninitialized Game"
		return "%r vs %r" % (self.players[0], self.players[1])

	@property
	def board(self):
		return CardList(self.player1.field + self.player2.field)

	@property
	def characters(self):
		return chain(self.player1.characters, self.player2.characters)

	@property
	def entities(self):
		return chain([self], self.player1.entities, self.player2.entities)

	@property
	def liveEntities(self):
		return chain(self.player1.liveEntities, self.player2.liveEntities)

	def action(self, type, *args):
		self.manager.action(type, *args)
		if type == PowSubType.ATTACK:
			self._attack(*args)
		elif type == PowSubType.PLAY:
			args[0]._play(*args[1:])
		elif type == PowSubType.DEATHS:
			self._processDeaths()
		else:
			raise NotImplementedError
		self.manager.action_end(type, *args)
		self._processDeaths()

	def attack(self, source, target):
		return self.action(PowSubType.ATTACK, source, target)

	def _attack(self, source, target):
		"""
		Process an attack between \a source and \a target
		"""
		logging.info("%r attacks %r" % (source, target))
		# See https://github.com/jleclanche/fireplace/wiki/Combat
		# for information on how attacking works
		self.proposedAttacker = source
		self.proposedDefender = target
		self.broadcast("BEFORE_ATTACK", source, target)
		attacker = self.proposedAttacker
		defender = self.proposedDefender
		self.proposedAttacker = None
		self.proposedDefender = None
		attacker.attacking = True
		defender.defending = True
		self.broadcast("ATTACK", attacker, defender)
		if attacker.shouldExitCombat:
			logging.info("Attack has been interrupted.")
			attacker.shouldExitCombat = False
			attacker.attacking = False
			defender.defending = False
			return
		# Save the attacker/defender atk values in case they change during the attack
		# (eg. in case of Enrage)
		attAtk = attacker.atk
		defAtk = defender.atk
		attacker.hit(defender, attAtk)
		if defAtk:
			defender.hit(attacker, defAtk)
		attacker.attacking = False
		defender.defending = False
		attacker.numAttacks += 1

	def card(self, id):
		card = Card(id)
		self.manager.new_entity(card)
		return card

	def processDeaths(self):
		return self.action(PowSubType.DEATHS)

	def _processDeaths(self):
		for card in self.liveEntities:
			if card.toBeDestroyed:
				card.destroy()

	def tossCoin(self):
		outcome = random.randint(0, 1)
		# player who wins the outcome is the index
		winner = self.players[outcome]
		loser = winner.opponent
		logging.info("Tossing the coin... %s wins!" % (winner))
		return winner, loser

	def start(self):
		logging.info("Starting game: %r" % (self))
		self.player1, self.player2 = self.tossCoin()
		self.manager.new_entity(self.player1)
		self.manager.new_entity(self.player2)
		self.currentPlayer = self.player1
		# XXX: Mulligan events should handle the following, but unimplemented for now
		self.player1.cardsDrawnThisTurn = 0
		self.player2.cardsDrawnThisTurn = 0
		for player in self.players:
			player.summon(player.originalDeck.hero)
			for card in player.originalDeck:
				card.controller = player
				card.zone = Zone.DECK
			player.shuffleDeck()

		self.player1.draw(3)
		self.player2.draw(4)
		self.beginMulligan()
		self.player1.firstPlayer = True
		self.player2.firstPlayer = False

	def beginMulligan(self):
		logging.info("Entering mulligan phase")
		self.step = Step.BEGIN_MULLIGAN
		self.nextStep = Step.MAIN_READY
		logging.info("%s gets The Coin (%s)" % (self.player2, THE_COIN))
		self.player2.give(THE_COIN)
		self.broadcast("TURN_BEGIN", self.player1)

	def endTurn(self):
		logging.info("%s ends turn" % (self.currentPlayer))
		self.step, self.nextStep = self.nextStep, Step.MAIN_CLEANUP
		self.broadcast("TURN_END", self.currentPlayer)
		self.step, self.nextStep = self.nextStep, Step.MAIN_NEXT
		self.broadcast("TURN_BEGIN", self.currentPlayer.opponent)

	##
	# Events

	events = [
		"UPDATE",
		"BEFORE_ATTACK", "ATTACK",
		"DRAW", "MILL",
		"TURN_BEGIN", "TURN_END",
		"DAMAGE", "HEAL",
		"CARD_DESTROYED", "MINION_DESTROY",
		"SECRET_REVEAL",
	]

	def broadcast(self, event, *args):
		# Broadcast things to the players' hands if requested
		for player in self.players:
			for entity in player.hand:
				for f in entity._eventListeners.get(event, []):
					if getattr(f, "zone", Zone.PLAY) == Zone.HAND:
						f(*args)
		super().broadcast(event, *args)

	def UPDATE(self):
		for aura in self.auras:
			aura.update()

	def BEFORE_ATTACK(self, source, target):
		source.controller.broadcast("BEFORE_OWN_ATTACK", source, target)

	def ATTACK(self, source, target):
		source.controller.broadcast("OWN_ATTACK", source, target)

	def DRAW(self, player, card):
		player.broadcast("OWN_DRAW", card)

	def MILL(self, player, card):
		card.destroy()

	def TURN_BEGIN(self, player):
		self.step, self.nextStep = self.nextStep, Step.MAIN_START_TRIGGERS
		self.step, self.nextStep = self.nextStep, Step.MAIN_START
		self.turn += 1
		logging.info("%s begins turn %i" % (player, self.turn))
		if self.currentPlayer:
			self.currentPlayer.currentPlayer = False
		self.step, self.nextStep = self.nextStep, Step.MAIN_ACTION
		self.currentPlayer = player
		self.currentPlayer.currentPlayer = True
		self.minionsKilledThisTurn = 0
		player.broadcast("OWN_TURN_BEGIN")

	def TURN_END(self, player):
		player.broadcast("OWN_TURN_END")

	def DAMAGE(self, source, target, amount):
		target.controller.broadcast("OWN_DAMAGE", source, target, amount)

	def HEAL(self, source, target, amount):
		source.controller.broadcast("OWN_HEAL", source, target, amount)

	def MINION_DESTROY(self, minion):
		minion.controller.broadcast("OWN_MINION_DESTROY", minion)
		self.minionsKilledThisTurn += 1

	def CARD_DESTROYED(self, card):
		card.controller.broadcast("OWN_CARD_DESTROYED", card)
		card.broadcast("SELF_CARD_DESTROYED")
		if card.type == CardType.MINION:
			self.broadcast("MINION_DESTROY", card)

	def SECRET_REVEAL(self, secret, player):
		assert secret.secret
		player.broadcast("OWN_SECRET_REVEAL", secret)
