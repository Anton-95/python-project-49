import prompt
import random
from brain_games.cli import welcome_user


def parity_cheking():
    user_name = welcome_user()
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
