from math import gcd
from random import randint
from brain_games.cli import welcome_user
from brain_games.games.general import question_answer, wrong_answer, final


def search_gcd():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        result = gcd(number_1, number_2)
        answer = question_answer((number_1, number_2))
        if answer == str(result):
            print('Correct!')
        else:
            wrong_answer(answer, result, user_name)
            break
    else:
        final(user_name)
