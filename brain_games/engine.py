from brain_games.cli import welcome_user
from prompt import string


def game_launch(game_module):
    user_name = welcome_user()
    print(game_module.GAME_RULES)
    looping_rounds(game_module.GENERATE_QUESTION_ANSWER, user_name)


def looping_rounds(question, user_name):
    for _ in range(3):
        correct_answer_user = question()
        result_cheking_answer = checking_answer(output_question_enter_answer
                                                (correct_answer_user[0]),
                                                correct_answer_user[1],
                                                user_name)
        if result_cheking_answer == 'wrong':
            break
    else:
        print(f'Congratulations, {user_name}!')


def output_question_enter_answer(question):
    user_answer = string(f'Question: {question}\nYour answer: ', empty=False)
    return user_answer


def checking_answer(user_answer, correct_answer, user_name):
    if user_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was \
'{correct_answer}'. Let's try again, {user_name}!")
        return 'wrong'
