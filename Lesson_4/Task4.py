# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return


my_name = 'sergey'

test_name1 = 'Sergey'
test_name2 = 'sergey'
test_name3 = 'SERGEY'
test_name4 = 'serg'

test_list = [test_name1, test_name2, test_name3, test_name4]

output_mask_wrong = 'You have just inputed wrong name!'
output_mask_ok = 'The name is correct.'

for item in test_list:

    if item.lower() == my_name:
        print(f'{output_mask_ok}')
    else:
        print(f'{output_mask_wrong} - {item}')

