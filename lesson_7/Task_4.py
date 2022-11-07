# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

dict_first = {item[0]+1: item[1] for item in enumerate(week_list)}

print(dict_first)

dict_second = {item[1]: item[0]+1 for item in enumerate(week_list)}

print(dict_second)
