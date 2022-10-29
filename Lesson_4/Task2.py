# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

# Full testcase
phone_number_1 = '9161111111' #suitable number
phone_number_2 = '79161111111' #wrong length
phone_number_3 = '+161111111' #not digital symbol
phone_number_4 = '+79161111111' #not digital symbol and wrong length

test_list = [phone_number_1, phone_number_2, phone_number_3, phone_number_4]

output_mask_wrong = 'Phone number is wrong.'
output_mask_ok = 'Phone number is OK!'
mistakes_list = ['Your phone number should contains 10 symbols.', 'Your phone number should contains only digital symbols.']

for item in test_list:
    if len(item) != 10:
        print(f'{item} {output_mask_wrong} {mistakes_list[0]}')
        continue
    else:
        suit = True
        for each in item:
            if not each.isdigit():
                print(f'{item} {output_mask_wrong} {mistakes_list[1]}')
                suit = False
                break
        if suit:
            print(f'{item} {output_mask_ok}')




