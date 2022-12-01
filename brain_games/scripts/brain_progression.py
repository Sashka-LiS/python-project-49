#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import brain_progression


def main():
    engine.main(brain_progression.rule, brain_progression.question_and_answer)


if __name__ == '__main__':
    main()