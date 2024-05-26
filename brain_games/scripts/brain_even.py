#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greeting_game
from brain_games.parity_check import parity_cheking


def main():
    greeting_game()
    parity_cheking()


if __name__ == '__main__':
    main()
