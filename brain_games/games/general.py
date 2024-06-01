from prompt import string


def welcome_to_game():
    print('Welcome to the Brain Games!')


def question_answer(question):
    answer = string(f'Question: {question}\nYour answer: ', empty=False)
    return answer


def final(user_name):
    print(f'Congratulations, {user_name}!')


def checking_answer(answer, correct_answer, user_name):
    if answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was \
'{correct_answer}'. Let's try again, {user_name}!")
        return 'wrong'
