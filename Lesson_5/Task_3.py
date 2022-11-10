# Words combination
#
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
from random import randint

test_case_tuple = ('always', 'forget', 'carefully', 'analyse', 'tasks')

for item in test_case_tuple:
    if len(item) < 5:
        print('Your word is not correct!')
    else:
        # тут рандомно генерим символы из диапазона 0 - len(word_for_combination) -1
        # самая большая сложность - отслеживать повторную генерацию символа
        # Применим алгоритм контроля использованных индексов символов в списке
        # Проверку на совпадение текущего и сгенерированного символа не делаем. В принципе, это не сдложно, конструкция if будет выглядеть так:
        # 'if random_index not in list_used_symbols and random_index != index'
        #list_used_symbols = [] # BETTER WAY TO USE TUPLE
        list_used_symbols = []
        word_result = ''
        index = 0
        while index < len(item):
            random_index = randint(0, len(item) - 1)
            if random_index not in list_used_symbols:
                word_result += item[random_index]
                list_used_symbols.append(random_index)
                index += 1
        print(f'For word: {item}, We have such result: {word_result}')
