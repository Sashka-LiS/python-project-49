#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import brain_even


def main():
    engine.main(brain_even.rule, brain_even.question_and_answer)


if __name__ == '__main__':
    main()
