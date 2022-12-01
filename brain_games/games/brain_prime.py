import random


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    '''вернуть вопрос и правильный ответ'''

    dividers = []
    divider = 1
    num = random.randint(2, 100)
    question = f'Question: {num}'

    while divider <= num:
        if num % divider == 0:
            dividers.append(divider)
        divider += 1

    if len(dividers) > 2:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return question, correct_answer
