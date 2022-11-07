# Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys and the number of occurrences as values.

our_string = input('Input any string :\n') #интерактивный ввод предложения
our_list = our_string.split(sep=' ') #строку в список
our_set = set(our_list) #спиок в множество, уникальные значения, фактически наши ключи
our_dict = {} #создаем пустой словарь

for item in our_set:
    print(item)
    our_dict.update([(item, our_list.count(item))])

print(our_dict)