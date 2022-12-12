import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_num(num):
    '''проверка простоты числа'''

    dividers = []
    divider = 1
    max_len_dividers = 2

    while divider <= num:
        if num % divider == 0:
            dividers.append(divider)
        divider += 1

    if len(dividers) > max_len_dividers:
        return False
    else:
        return True


def question_and_answer():
    '''вернуть вопрос и правильный ответ'''

    num = random.randint(2, 200)
    question = f'Question: {num}'

    if is_prime_num(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
