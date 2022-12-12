import random
import math


RULE = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    '''вернуть вопрос и правильный ответ'''

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f'Question: {num1} {num2}'
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
