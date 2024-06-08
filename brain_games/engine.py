from brain_games.cli import welcome_user
from prompt import string


def game_launch(game_module):
    user_name = welcome_user()
    print(game_module.GAME_RULES)
    for _ in range(3):
        question, correct_answer = game_module.generate_question_answer()
        print(f'Question: {question}')
        user_answer = enter_answer()
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was \
'{correct_answer}'. Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


def enter_answer():
    user_answer = string('Your answer: ', empty=False)
    return user_answer
