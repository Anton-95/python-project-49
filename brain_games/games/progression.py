from random import randint


GAME_RULES = 'What number is missing in the progression?'


def generate_question_answer():
    progression = []
    start = randint(1, 60)
    step = randint(2, 6)
    progression = generate_progression(start, step)
    index_del = randint(1, 9)
    correct_answer = progression[index_del]
    progression[index_del] = '..'
    return ((' '.join(map(str, progression))), (str(correct_answer)))


def generate_progression(start, step):
    stop = start + (step * 10)
    progression = list(range(start, stop, step))
    return progression
