from brain_games.games.engine import round
from brain_games.cli import welcome_user
from random import randint


def prime_number_definition():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    round(question_and_correct_answer, user_name)


def question_and_correct_answer():
    number = randint(2, 50)
    half_number = number // 2
    for divider in range(2, half_number):
        if number % divider == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return (number, correct_answer)
