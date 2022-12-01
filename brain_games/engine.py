import prompt


def welcome_user(rule):
    '''приветсвие, объяснение правил, получение имени'''

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rule)
    return name


def main(rule, question_answer):

    score = 0

    name = welcome_user(rule)
    while score != 3:
        question, correct_answer = question_answer()
        print(question)
        answer = (prompt.string('Your answer: ')).lower()
        if answer == str(correct_answer):
            score += 1
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break
    if score == 3:
        print(f'Congratulations, {name}!')
