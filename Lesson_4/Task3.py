# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong,
# and then responds with a message accordingly.

var1 = 4
var2 = 3

answer = 1

mask_question = 'Input your answer for expression '

output_mask_wrong = 'You answer is wrong!'
output_mask_ok = 'You answer is correct.'


list_expressions = ['+', '-', '*', '/', '**']

for item in list_expressions:
    print(f'{mask_question}{var1} {item} {var2}')
    if item == '+' and answer == var1 + var2:
        print(f'{answer}  {output_mask_ok}')
    elif item == '-' and answer == var1 - var2:
        print(f'{answer}  {output_mask_ok}')
    else:
        print(f'{answer}  {output_mask_wrong}')
    # elif item == '+':
