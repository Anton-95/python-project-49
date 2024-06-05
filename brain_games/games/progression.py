from random import randint


GAME_RULES = 'What number is missing in the progression?'


def GENERATE_QUESTION_ANSWER():
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
