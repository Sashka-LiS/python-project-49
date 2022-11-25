#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import brain_calc

def main():
    engine.main(brain_calc.rule, brain_calc.question_and_answer)

if __name__ == '__main__':
    main()

