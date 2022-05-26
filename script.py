import random


def obtain_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('Well done, perfect guess!')
            return True
        else:
            print('Please try again')
            return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number from 1~10:  '))
            if obtain_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue


