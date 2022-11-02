# Words combination
#
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
from random import randint

word_for_combination = input('Input any word. Pay attention, your word have to contain, at least, five characters.\n')

if len(word_for_combination) < 5:
    print('Your word is not correct!')
else:
    # тут рандомно генерим символы из диапазона 0 - len(word_for_combination) -1
    # самая большая сложность - отслеживать повторную генерацию символа
    # Применим алгоритм контроля использованных символов в списке
    list_used_symbols = []
    word_result = ''
    index = 0
    while index < len(word_for_combination):
        random_index = randint(0, len(word_for_combination) - 1)
        if random_index not in list_used_symbols:
            word_result += word_for_combination[random_index]
            list_used_symbols.append(random_index)
            index += 1
    print(f'We have such result: {word_result}')
