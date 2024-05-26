import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ',  empty=False)
    print(f'Hello, {user_name}!')