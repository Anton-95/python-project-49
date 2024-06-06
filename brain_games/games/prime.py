from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    number = randint(5, 50)
    half_number = number // 2
    for divider in range(2, half_number):
        if number % divider == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return (number, correct_answer)
