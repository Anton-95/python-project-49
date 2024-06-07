from brain_games.cli import welcome_user
from prompt import string


def game_launch(game_module):
    user_name = welcome_user()
    print(game_module.GAME_RULES)
    for _ in range(3):
        question, correct_answer = game_module.generate_question_answer()
        print(f'Question: {question}')
        result_cheking_answer = checking_answer(enter_answer(),
                                                correct_answer,
                                                user_name)
        if result_cheking_answer == 'wrong':
            break
    else:
        print(f'Congratulations, {user_name}!')


def enter_answer():
    user_answer = string('Your answer: ', empty=False)
    return user_answer


def checking_answer(user_answer, correct_answer, user_name):
    if user_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was \
'{correct_answer}'. Let's try again, {user_name}!")
        return 'wrong'
