from brain_games.games.general import question_answer, checking_answer, final
from brain_games.cli import welcome_user
from random import randint


def prime_number_definition():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = randint(2, 50)
        half_number = number // 2
        for divider in range(2, half_number):
            if number % divider == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
        check = checking_answer(question_answer(number),
                                correct_answer,
                                user_name)
        if check == 'wrong':
            break
    else:
        final(user_name)
