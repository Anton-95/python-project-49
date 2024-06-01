from random import choice
from random import randint
from brain_games.cli import welcome_user
from brain_games.games.general import question_answer, checking_answer, final


def calculate():
    user_name = welcome_user()
    print('What is the result of the expression?')
    operators = '+-*'
    for _ in range(3):
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        operator = choice(operators)
        expression = f'{number_1} {operator} {number_2}'
        correct_answer = eval(expression)
        check = checking_answer(question_answer(expression),
                                str(correct_answer),
                                user_name)
        if check == 'wrong':
            break
    else:
        final(user_name)
