from brain_games.games.engine import round
from brain_games.cli import welcome_user
from random import randint
from math import gcd


def search_gcd():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    round(question_and_correct_answer, user_name)


def question_and_correct_answer():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    numbers = f'{number_1} {number_2}'
    correct_answer = gcd(number_1, number_2)
    return (numbers, str(correct_answer))
