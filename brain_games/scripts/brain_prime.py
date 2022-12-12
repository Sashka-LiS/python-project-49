#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import brain_prime


def main():
    engine.main(brain_prime.RULE, brain_prime.question_and_answer)


if __name__ == '__main__':
    main()
