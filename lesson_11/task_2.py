import json as j
import sys


# ----
def print_result(item: dict, ind, condition):
    p1 = ''
    for key in item:
        p1 += key + ': ' + item[key] + '\n'
    print(f'Searching by indication: {ind}\nBy condition: {condition} \nResult is:\n{p1}')


def print_delete():
    print(f'The record was successfully deleted\n')


def print_non_result(ind, condition):
    print(f"For searching by indication: {ind}\nby condition: {condition} \nThere are not results!")


def add_new(item: dict, *args):
    try:
        new_fname = input('Type on the keyboard the first name:\n')
        new_lname = input('Type on the keyboard the last name:\n')
        new_phone_number = input('Type on the keyboard the phone number:\n')
        new_state = input('Type on the keyboard the State:\n')
        new_city = input('Type on the keyboard the City:\n')
        new_person = {'first_name': new_fname,
                      'last_name': new_lname,
                      'full_name': new_fname + ' ' + new_lname,
                      'phone_numbers': new_phone_number,
                      'state': new_state,
                      'city': new_city}
        item['persons'].append(new_person)
        print('Information was successfully added!')
        return True
    except Exception:
        print(f'Something was wrong with adding information\n{Exception.__doc__}')
        return False


def find_by(book: list, *args):
    name_search = input('Type on the keyboard the ' + name_dict[args[0]] + ' to find:\n')
    result = list(filter(lambda item: item[args[0]] == name_search, book['persons']))
    if len(result) > 0:
        print_result(result[0], name_dict[args[0]], name_search)
    else:
        print_non_result(name_dict[args[0]], name_search)
    return True


def delete_by(book: list, *args):
    name_search = input('Type on the keyboard the ' + name_dict[args[0]] + ' to find:\n')
    result = list(filter(lambda item: item[args[0]] == name_search, book['persons']))
    if len(result) > 0:
        choise = input('The record was found! Do you really want to delete them?\nType - Y or a key to refuse:\n')
        if choise.lower() == 'y':
            print(book['persons'])
            print(result[0])
            book['persons'].remove(result[0])
            print(book['persons'])
            print_delete()
    else:
        print_non_result(name_dict[args[0]], name_search)
    return True


def update_by(book: list, *args):
    print('1')
    return True


def exist_pb(book: dict, act='', file_name=''):
    with open(file_name, 'w') as f:
        j.dump(book, f)
        print('Information was successfully saved in File!')
    sys.exit()


possible_activity = {1: ['Add new entries', add_new, ''],
                     2: ['Search by first name', find_by, 'first_name'],
                     3: ['Search by last name', find_by, 'last_name'],
                     4: ['Search by full name', find_by, 'full_name'],
                     5: ['Search by telephone number', find_by, 'phone_numbers'],
                     6: ['Search by city or state', find_by, ['state', 'city']],
                     7: ['Delete a record for a given telephone number', delete_by, 'phone_numbers'],
                     8: ['Update a record for a given telephone number', update_by, 'phone_numbers'],
                     0: ['Exist the program', exist_pb, '']}

name_dict = dict(first_name='First Name',
                 last_name='Last Name',
                 full_name='Full Name',
                 phone_numbers='Phone Number',
                 state='State',
                 city='City')


def start(act: bool):
    if act:
        choice = input("Would you like to work with the phone book?\nType Y - to start work or any key - to refuse:\n")
    else:
        choice = input("Do you want to continue?\nType Y - to continue or any key - to stop working with program:\n")
    match choice:
        case "Y":
            return True
        case "y":
            return True
        case _:
            return False


def secect_action(actions: dict):
    options_list = 'What do you want to do?\nPossible options:\n'
    for k, v in actions.items():
        options_list += v[0] + ' , to use, type on the keyboard : ' + str(k) + '\n'
    client_choice = input(options_list)
    return client_choice


def main():
    start_working = start(True)
    if not start_working:
        sys.exit()
    try:
        status = True
        name: str = input("Input Phone book name:\n")
        file_name = name + ".json"
        with open(name + ".json", "r", encoding='UTF-8') as book:
            our_pb = j.load(book)
        while status:
            type_activity = secect_action(possible_activity)
            status = possible_activity[int(type_activity)][1](our_pb, possible_activity[int(type_activity)][2],
                                                              file_name)
            if status:
                status = start(False)
        ch = input('Do you want to save changes?\nType Y - or any key - to refuse:\n')
        if ch:
            exist_pb(our_pb, '', file_name)
    except FileNotFoundError:
        print('Unfortunately, there are not such file!')
        print(FileNotFoundError.__doc__)
    except Exception:
        print(Exception.__doc__)


if __name__ == '__main__':
    main()
    # status = True
    # name: str = input("Input Phone book name:\n")
    # file_name = name + ".json"
    # with open(name + ".json", "r", encoding='UTF-8') as book:
    #     our_pb = j.load(book)
    # while status:
    #     type_activity = secect_action(possible_activity)
    #     status = possible_activity[int(type_activity)][1](our_pb, possible_activity[int(type_activity)][2], file_name)
    #     if status:
    #         status = start(False)
    # ch = input('Do you want to save changes?\nType Y - or any key - to refuse:\n')
    # if ch:
    #     exist_pb(our_pb, '', file_name)
