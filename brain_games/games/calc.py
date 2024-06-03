from engine import round
from brain_games.cli import welcome_user
from random import choice, randint
from operator import add, sub, mul


def calculate():
    user_name = welcome_user()
    print('What is the result of the expression?')
    round(question_and_correct_answer, user_name)


def question_and_correct_answer():
    operators = '+-*'
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operator = choice(operators)
    match operator:
        case '+':
            correct_answer = add(number_1, number_2)
        case '-':
            correct_answer = sub(number_1, number_2)
        case '*':
            correct_answer = mul(number_1, number_2)
    expression = f'{number_1} {operator} {number_2}'
    return (expression, str(correct_answer))
