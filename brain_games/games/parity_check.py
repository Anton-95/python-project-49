from random import randint
from brain_games.cli import welcome_user
from brain_games.games.general import question_answer, wrong_answer, final


def parity_cheking():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(1, 100)
        answer = question_answer(number)
        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('Correct!')
        elif answer == 'yes':
            wrong_answer(answer, 'no', user_name)
            break
        else:
            wrong_answer(answer, 'yes', user_name)
            break
    else:
        final(user_name)
