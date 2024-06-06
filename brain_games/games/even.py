from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    number = randint(1, 100)
    if cheсk_parity_number(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number, correct_answer)


def cheсk_parity_number(num):
    if num % 2 == 0:
        return True
    return False
