#!/usr/bin/env python3
import prompt
import random


answers = ['yes', 'no']


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = (prompt.string('Your answer: ')).lower()
        if (num % 2 == 0 and answer == 'yes') or (num % 2 != 0 and answer == 'no'):
            count += 1
            print('Correct!')
        else:
            if num % 2 == 0:
                print(f'"{answer}" is wrong answer ;(. Correct answer was "{answers[0]}".')
                print(f"Let's try again, {name}!")
                break
            elif num % 2 != 0:
                print(f'"{answer}" is wrong answer ;(. Correct answer was "{answers[1]}".')
                print(f"Let's try again, {name}!")
                break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
