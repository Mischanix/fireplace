#!/usr/bin/env python
import sys; sys.path.append("..")
from fireplace.enums import Race, CardType, Zone
from fireplace.targeting import Selector
from test_main import prepare_game


def test_selector():
	game = prepare_game()
	alex = game.player1.give("EX1_561")
	selector = Selector(Race.PIRATE, Race.DRAGON) + Selector(CardType.MINION)
	assert len(game.select(selector + Selector(Zone.HAND), game.player1)) >= 1
	selector = selector + Selector(Zone.PLAY)
	assert len(game.select(selector, game.player1)) == 0
	alex.play(target=game.player2)
	assert len(game.select(selector, game.player1)) == 1


def main():
	for name, f in globals().items():
		if name.startswith("test_") and hasattr(f, "__call__"):
			f()
	print("All tests ran OK")


if __name__ == "__main__":
	main()
