import random

answer = random.randint(1,10)

def obtain_guess(guess):
    if 0 < guess < 11:
        if guess == answer:
            print('Well done, perfect guess!')
            break
        else:
            print('Please try again')




# import random
#
# answer = random.randint(1, 10)
# while True:
#     try:
#         guess = int(input('guess a number from 1~10:  '))
#         if 0 < guess < 11:
#             if guess == answer:
#                 print('Well done, perfect guess!')
#                 break
#             else:
#                 print('Please try again')
#     except ValueError:
#         print('please enter a number')
#         continue


