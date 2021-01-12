#!/usr/bin/env python3
import sys
import argparse
import random
from game import Game

def main(args):
    Game.intro()
    game = Game(args)
    while game.ongoing:
        game.turn()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-ne",
        "--no-expansion",
        action="store_true",
        help="The expansion pack will not be used"
    )

    parser.add_argument(
        "-ol",
        "--one-loser",
        action="store_true",
        help="The game will continue until there is only one loser, as opposed to ending once one person has won"
    )

    parser.add_argument(
        "--seed",
        action="store",
        type=int,
        help="Set the random() seed"
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-ws",
        "--winner-starts",
        action="store_true",
        help="The winner will start from the second game onwards"
    )

    group.add_argument(
        "-rs",
        "--random-starts",
        action="store_true",
        help="A random player will start from the second game onwards"
    )

    args = parser.parse_args("".split())

    if args.seed is not None:
        random.seed(args.seed)
    try:
        main(args)
    except KeyboardInterrupt:
        sys.exit(0)
