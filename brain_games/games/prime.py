from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    number = randint(5, 50)
    half_number = number // 2
    for divider in range(2, half_number):
        if check_prime_number(number, divider):
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return (number, correct_answer)


def check_prime_number(num, divider):
    if num % divider == 0:
        return True
    return False
