import random
import fireplace.cards
from ..actions import *
from ..enums import CardType, Race, Zone
from ..targeting import *


def hand(func):
	"""
	@hand helper decorator
	The decorated event listener will only listen while in the HAND Zone
	"""
	func.zone = Zone.HAND
	return func

def randomCollectible(**kwargs):
	return random.choice(fireplace.cards.filter(collectible=True, **kwargs))
