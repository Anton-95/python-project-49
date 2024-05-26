import prompt
import random


def welcome_user():
    user_name = prompt.string('May I have your name? ', empty=False)
    print(f'Hello, {user_name}!')
    return user_name


user_name = welcome_user()


def parity_cheking():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(1, 100)
        answer = prompt.string(f'Question: {number}\nYour answer: ', empty=False)
        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('Correct!')
        elif answer == 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'. Let's try again, {user_name}!")
            break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
