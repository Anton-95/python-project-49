from prompt import string


def question_answer(question):
    answer = string(f'Question: {question}\nYour answer: ', empty=False)
    return answer


def wrong_answer(answer, correct_result, user_name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was \
'{correct_result}'. Let's try again, {user_name}!")


def final(user_name):
    print(f'Congratulations, {user_name}!')
