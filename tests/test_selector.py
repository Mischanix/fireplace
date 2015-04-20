#!/usr/bin/env python
import sys; sys.path.append("..")
from fireplace.enums import Race, CardType, Zone
from fireplace.targeting import Affiliation, Selector
from test_main import prepare_game


def test_selector():
	game = prepare_game()
	game.player1.discardHand()
	alex = game.player1.give("EX1_561")
	selector = Selector(Race.PIRATE, Race.DRAGON) + Selector(CardType.MINION)
	assert len(selector.eval(game.player1.hand, game.player1)) >= 1

	in_hand = Selector(Zone.HAND)
	selector = in_hand + Selector(Race.DRAGON) + Selector(Affiliation.FRIENDLY)
	targets = selector.eval(game, game.player1)
	assert len(targets) == 1
	assert targets[0] == alex


def main():
	for name, f in globals().items():
		if name.startswith("test_") and hasattr(f, "__call__"):
			f()
	print("All tests ran OK")


if __name__ == "__main__":
	main()
