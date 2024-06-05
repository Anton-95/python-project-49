from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def GENERATE_QUESTION_ANSWER():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    numbers = f'{number_1} {number_2}'
    correct_answer = gcd(number_1, number_2)
    return (numbers, str(correct_answer))
