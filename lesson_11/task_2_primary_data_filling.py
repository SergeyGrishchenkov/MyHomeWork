import json as j
ask = input('Do you really want to fill primary data?\nAll previous data will be cleared!!!\nInput Y if you agree or wny symbol if not\n')
l_states = ['Kiev', 'Lviv', 'Vinniza', 'Chernigiv']
l_scities = {'Kiev': ['Kiev', 'Chabany', 'Gatne'], 'Lviv': ['Lviv', 'Stry'], 'Vinniza': ['Vinniza'], 'Chernigiv': ['Chernigiv']}
persona_dict = dict(first_name='', last_name='', full_name='', phone_numbers=[], state=-1, city=-1)

if ask == 'Y':
    # We fill in the primary data of dictionaries states and cities
    with open('PB.json', 'w', encoding='ASCII') as f:
       my_phonebook = {'states': l_states, 'cities': l_scities, 'persons': [persona_dict]}
       j.dump(my_phonebook, f)




