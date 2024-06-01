from random import randint
from brain_games.cli import welcome_user
from brain_games.games.general import question_answer, checking_answer, final


def parity_cheking():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        num = randint(1, 100)
        if num % 2 == 0:
            correct_answer = 'yes'
        elif num % 2 != 0:
            correct_answer = 'no'
        check = checking_answer(question_answer(num), correct_answer, user_name)
        if check == 'wrong':
            break
    else:
        final(user_name)
