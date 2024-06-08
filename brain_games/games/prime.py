from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    number = randint(5, 50)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number, correct_answer)


def is_prime(number):
    half_number = number // 2
    for divider in range(2, half_number):
        if number % divider == 0:
            return False
    return True
