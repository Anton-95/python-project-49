from prompt import string


def round(question, user_name):
    for _ in range(3):
        correct_answer_user = question()
        result_cheking_answer = checking_answer(question_and_user_answer
                                                (correct_answer_user[0]),
                                                correct_answer_user[1],
                                                user_name)
        if result_cheking_answer == 'wrong':
            break
    else:
        final(user_name)


def question_and_user_answer(question):
    user_answer = string(f'Question: {question}\nYour answer: ', empty=False)
    return user_answer


def checking_answer(user_answer, correct_answer, user_name):
    if user_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was \
'{correct_answer}'. Let's try again, {user_name}!")
        return 'wrong'


def final(user_name):
    print(f'Congratulations, {user_name}!')
