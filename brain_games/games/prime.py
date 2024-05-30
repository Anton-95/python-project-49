from brain_games.games.general import question_answer, wrong_answer, final
from brain_games.cli import welcome_user
from random import randint


def prime_number_definition():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = randint(2, 50)
        half_number = number // 2
        for divider in range(2, half_number):
            result = number % divider
            if result == 0:
                result = 'no'
                break
        else:
            result = 'yes'
        answer = question_answer(number)
        if answer == result:
            print('Correct!')
        else:
            wrong_answer(answer, result, user_name)
            break
    else:
        final(user_name)
