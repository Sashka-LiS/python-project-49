#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import brain_gcd


def main():
    engine.main(brain_gcd.RULE, brain_gcd.question_and_answer)


if __name__ == '__main__':
    main()
