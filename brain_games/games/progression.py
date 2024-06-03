from engine import round
from brain_games.cli import welcome_user
from random import randint


def defenition_number():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    round(question_and_correct_answer, user_name)


def question_and_correct_answer():
    sequence = []
    start = randint(1, 60)
    step = randint(2, 6)
    for _ in range(10):
        start += step
        sequence.append(start)
    index_del = randint(1, 9)
    correct_answer = sequence[index_del]
    sequence[index_del] = '..'
    return ((' '.join(map(str, sequence))), (str(correct_answer)))
