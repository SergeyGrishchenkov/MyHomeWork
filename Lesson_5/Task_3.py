import random

greeting = 'Hello, do you want to play? You need to guess what the number is. Type Y or N'
greeting_answer = input(greeting)
if greeting_answer == 'Y':
    player_name = input('Input your name:  ')
elif greeting_answer == 'N':
    print('See you next time!')
else:
    print('You have inputed wrong item. Would you like to try again?')

