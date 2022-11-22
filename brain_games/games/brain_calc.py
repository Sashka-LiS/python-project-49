import random
import operator


num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
oper = random.choice(['+', '-', '*'])
rule = 'What is the result of the expression?'
question = f'Question: {num1} {oper} {num2}'


def get_correct_answer(oper):
    '''получить правильный ответ'''

    if oper == '+':
        correct_answer = operator.add(num1, num2)
    elif oper == '-':
        correct_answer = operator.sub(num1, num2)
    elif oper == '*':
        correct_answer = operator.mul(num1, num2)
    return str(correct_answer)


correct_answer = get_correct_answer(oper)