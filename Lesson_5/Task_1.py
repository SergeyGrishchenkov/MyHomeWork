from random import randint

#Report's masks

greeting        = 'Hello, do you want to play? You need to guess what the number is. Type Y or N:\n'
suggestion      = 'We have just chosen a number from 1 to 10. \nYou should guess, what the number is! \nInput a number: \n:'
bad_input       = 'You should select a number from 1 to 10!\nSorry, you  lost the game!\n'
bad_choice      = 'You choice is BAD!\nSorry, You  lost the game!\n'
good_choice     = 'Congratulations!!! You have done THE RIGHT CHOICE!\n'


def choice_random_int():
    rand_int = randint(1, 10)
    user_choice = input(suggestion)
    if not user_choice.isdigit():
        return [bad_input, -1, False]
    elif int(user_choice) > 10 and int(user_choice) < 0:
        return [bad_input, -1, False]
    else:
        if int(user_choice) == rand_int:
            return [good_choice, user_choice, True]
        else:
            return [bad_choice, rand_int, False]


if __name__ == "__main__":
    greeting_answer = input(greeting)
    if greeting_answer == 'Y':
        player_name = input('Input your name:  ')
        result = choice_random_int()
        add_report = '' if result[2] else ('Correct choice is ' + str(result[1]))
        print(f'{player_name}, {result[0]} {add_report}')
    elif greeting_answer == 'N':
        print(f'See you next time!')
    else:
        print(f'You have inputed wrong item.')