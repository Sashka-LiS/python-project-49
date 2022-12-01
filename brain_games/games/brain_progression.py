import random


rule = 'What number is missing in the progression?'


def question_and_answer():
    '''вернуть вопрос и правильный ответ'''

    first_num = random.randint(1, 200)
    step_progression = random.randint(1, 15)
    progression = [str(first_num)]
    rand_index = random.randint(0, 9)

    for i in range(9):
        next_num = first_num + step_progression
        progression.append(str(next_num))
        first_num = next_num

    correct_answer = progression[rand_index]
    progression[rand_index] = '..'
    progression = ' '.join(progression)
    question = f'Question: {progression}'

    return question, correct_answer
