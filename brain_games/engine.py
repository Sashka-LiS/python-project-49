import prompt


MAX_SCORE = 3


def main(rule, question_answer):

    score = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rule)
    while score != MAX_SCORE:
        question, correct_answer = question_answer()
        print(question)
        answer = (prompt.string('Your answer: ')).lower()
        if answer == str(correct_answer):
            score += 1
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break
    if score == MAX_SCORE:
        print(f'Congratulations, {name}!')
