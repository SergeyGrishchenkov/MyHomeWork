import json as j
import sys

# ----
def add_new(item: dict):
    try:
        new_fname = input('Type on the keyboard the first name:\n')
        new_lname = input('Type on the keyboard the last name:\n')
        new_phone_number = input('Type on the keyboard the phone number:\n')
        new_state = input('Type on the keyboard the State:\n')
        new_city = input('Type on the keyboard the City:\n')
        new_person = {'first_name': new_fname,
                      'last_name': new_lname,
                      'full_name': new_fname + ' ' + new_lname,
                      'phone_numbers': [new_phone_number],
                      'state': new_state,
                      'city': new_city}
        item['persons'].append(new_person)
        print('Information was successfully added!')
        return True
    except Exception:
        ptint(f'Something was wrong with adding information\n{Exception.__doc__}')
        return False
def find_by_first_name(book: list):
    first_name = input('Type on the keyboard the first name to find:\n')
    print('1')
    return True

def find_by_last_name(book: list):
    print('1')
    return True

def find_by_full_name(book: list):
    print('1')
    return True

def find_by_phonenumber(book: list):
    print('1')
    return True

def find_by_city_state(book: list):
    print('1')
    return True

def delete_by_phonenumber(book: list):
    print('1')
    return True

def update_by_phonenumber('', book: list):
    print('1')
    return True

def exist_pb(file_name, book: dict):
    with open(file_name, 'w') as f:
        j.dump(book, f)
    sys.exit()

possible_activity = {'add': ['Add new entries', add_new],
                    'fn': ['Search by first name', find_by_first_name],
                    'fln': ['Search by last name', find_by_last_name],
                    'ffn': ['Search by full name', find_by_full_name],
                    'phone': ['Search by telephone number', find_by_phonenumber],
                    'city': ['Search by city or state', find_by_city_state],
                    'del': ['Delete a record for a given telephone number', delete_by_phonenumber],
                    'upd': ['Update a record for a given telephone number', update_by_phonenumber],
                    'ext': ['Exist the program', exist_pb]}

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

def main():
    start_working = start()
    if not start_working:
        sys.exit()
    name = input("Input Phone book name:\n")
    try:
        status = True
        while status:
            file_name = name + ".json"
            with open(file_name, "r", encoding='UTF-8') as book:
                our_pb = j.load(book)
            #choise of activity
            type_activity = secect_action(possible_activity)

            status = possible_activity[type_activity][1](our_pb)
            #print(type(j.load(book)))
            #book_dic = j.load(book)
            #activity = choise_activity()
    except FileNotFoundError:
        print('Unfortunately, there are not such file!')
        print(FileNotFoundError.__doc__)
    except:
        print(Exception.__doc__)


if __name__ == '__main__':
    main()

