import datetime

greeting_mask1 = 'Good day'

greeting_mask2 = 'is a perfect day to learn some python'

my_name = 'Sergey'

this_day = datetime.datetime.today().weekday()

print(greeting_mask1 + ' ' + my_name + '! ' + str(this_day) + ' ' + greeting_mask2, end='.')
