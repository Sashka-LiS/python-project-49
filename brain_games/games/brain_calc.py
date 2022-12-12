import random
import operator


RULE = 'What is the result of the expression?'


def question_and_answer():
    '''вернуть вопрос и правильный ответ'''

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    oper = random.choice(['+', '-', '*'])

    question = f'Question: {num1} {oper} {num2}'

    if oper == '+':
        correct_answer = operator.add(num1, num2)
    elif oper == '-':
        correct_answer = operator.sub(num1, num2)
    elif oper == '*':
        correct_answer = operator.mul(num1, num2)
    return question, correct_answer
