from math import gcd
from random import randint
from brain_games.cli import welcome_user
from brain_games.games.general import question_answer, checking_answer, final


def search_gcd():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        correct_answer = gcd(number_1, number_2)
        chek = checking_answer(question_answer(f'{number_1} {number_2}'),
                               str(correct_answer),
                               user_name)
        if chek == 'wrong':
            break
    else:
        final(user_name)
