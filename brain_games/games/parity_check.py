from brain_games.games.engine import round
from brain_games.cli import welcome_user
from random import randint


def parity_cheking():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    round(question_and_correct_answer, user_name)


def question_and_correct_answer():
    number = randint(1, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number, correct_answer)
