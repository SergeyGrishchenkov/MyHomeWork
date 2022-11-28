import json as j
import sys

# ----
def add_new(item: dict):
    new_fname = inpup('Type on the keyboard the first name:\n')
    new_lname = inpup('Type on the keyboard the last name:\n')
    new_phone_number = inpup('Type on the keyboard the phone number:\n')
    new_state = inpup('Type on the keyboard the State:\n')
    new_city = inpup('Type on the keyboard the City:\n')
    new_person = {'first_name': new_fname,
                  'last_name': new_lname,
                  'full_name': new_fname + ' ' + new_lname,
                  'phone_numbers': [new_phone_number],
                  'state': new_state,
                  'city': new_city}
    item.update(new_person)

def find_by_first_name(name: str, book: list):
    #book.
    print('')

def find_by_last_name():
    print('')

def find_by_full_name():
    print('')

def find_by_phonenumber():
    print('')

def find_by_city_state():
    print('')

def delete_by_phonenumber():
    print('')

def update_by_phonenumber():
        print('')

t_activity = (('Add new entries', 'Search by first name'), ('Add', 'fn'), ('Add new entries',add_new, find_by_first_name))

possible_activity = {'add': ['Add new entries', add_new], 'fn': ['Search by first name', find_by_first_name]}

def start():
    choise = input("Would you like to work with the phone book?\nType Y - to start work or any key - to refuse:\n")
    match choise:
        case "Y":
            return True
        case "y":
            return True
        case _:
            return False

def secect_action(actions: dict):
    options_list = 'What do you want to do?\nPossible options:\n'
    for k, v in actions.items():
        options_list += v[0] + ' , to use, type on the keyboard : ' + k + '\n'
    client_choice = input(options_list)
    return client_choice

#def main():
start_working = start()
if not start_working:
    sys.exit()
name = input("Input Phone book name:\n")
try:
    with open(name + ".json", "r", encoding='UTF-8') as book:
        our_pb = j.load(book)
        #choise of activity
        type_activity = secect_action(possible_activity)

        print(type(possible_activity[type_activity][1](our_pb)))

            #print(type(j.load(book)))
            #book_dic = j.load(book)
            #activity = choise_activity()
except FileNotFoundError:
    print('Unfortunately, there are not such file!')
    print(FileNotFoundError.__doc__)
except:
    print(Exception.__doc__)


if __name__ == '__main__':
    print('1')

