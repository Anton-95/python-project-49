from random import randint
from brain_games.cli import welcome_user
from brain_games.games.general import question_answer, checking_answer, final


def defenition_number():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    for _ in range(3):
        sequence = []
        start = randint(1, 60)
        step = randint(2, 6)
        for _ in range(10):
            start += step
            sequence.append(start)
        index_del = randint(1, 9)
        correct_answer = sequence[index_del]
        sequence[index_del] = '..'
        check = checking_answer(question_answer(' '.join(map(str, sequence))),
                                str(correct_answer),
                                user_name)
        if check == 'wrong':
            break
    else:
        final(user_name)
