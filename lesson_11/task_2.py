import json as j
import sys

# ----
def add_new(item: dict):
    print('')

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
possible_activity = {'add': ['Add new entries', add_new]}

def start():
    choise = input("Would you like to work with the phone book?\nType Y - to start work or any key - to refuse:\n")
    match choise:
        case "Y":
            return True
        case "y":
            return True
        case _:
            return False

def choise_activity():
    print('-------')

#def main():
start_working = start()
if not start_working:
    sys.exit()
name = input("Input Phone book name:\n")
try:
    with open(name + ".json", "r", encoding='UTF-8') as book:
        our_pb = j.load(book)
        #choise of activity
        print(type(our_pb))

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

