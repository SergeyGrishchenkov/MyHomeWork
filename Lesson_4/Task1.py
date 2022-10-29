# task: Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.

# Full testcase

test_string_1 = 'I am studying Python'
test_string_2 = 'test'
test_string_3 = 'two'
test_string_4 = 'is'
test_string_5 = 'I'

output_mask = 'This is the result - '

test_list = [test_string_1, test_string_2, test_string_3, test_string_4, test_string_5]

for item in test_list:
    if len(item) < 2:
        print(f'{output_mask }')
        break
    print(f'{output_mask }{item[0]}{item[1]}{item[-2]}{item[-1]}')