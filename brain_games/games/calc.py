from random import choice, randint
from operator import add, sub, mul


GAME_RULES = 'What is the result of the expression?'


def generate_question_answer():
    operators = ('+', '-', '*')
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operator = choice(operators)
    correct_answer = calculate(number_1, number_2, operator)
    expression = f'{number_1} {operator} {number_2}'
    return (expression, str(correct_answer))


def calculate(num1, num2, operator):
    match operator:
        case '+':
            correct_answer = add(num1, num2)
        case '-':
            correct_answer = sub(num1, num2)
        case '*':
            correct_answer = mul(num1, num2)
    return correct_answer
