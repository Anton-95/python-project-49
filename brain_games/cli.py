import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ', empty=False)
    print(f'Hello, {user_name}!')
    return user_name
