# The birthday greeting program.
#
# Write a program that takes your name as input, and then your age as input and greets you with the following:
#
# “Hello <name>, on your next birthday you’ll be <age+1> years”

user_name = input('Input your first name:\n')
user_age = input('Input your age, range from 5 to 99:\n')
wrong_user_age = input('You inputed wrong age.\n')

#проверяем возраст на корректность
if not user_age.isdigit() or int(user_age) < 5 or int(user_age) > 99:
    print(f'{user_name} {wrong_user_age}')
else:
    next_age = int(user_age)
    print(f'Hello {user_name}, on your next birthday you’ll be {next_age} years.\n')

