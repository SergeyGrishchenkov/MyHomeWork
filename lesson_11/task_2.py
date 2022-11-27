import json as j
import sys

# ----
book_dic = {}

def start():
    choise = input("Would you like to work with the phone book?\nType Y - to start work or N - to refuse:\n")
    match choise:
        case "Y":
            return True
        case "N":
            return False
        case _:
            return False

def choise_activity():
    print('-------')

def main():
    global book_dic
    print(book_dic)
    start_working = start()
    if not start_working:
        sys.exit()
    name = input("Input Phone book name:\n")
    try:
        with open(name + ".json", "r", encoding='UTF-8') as book:
            print(book)
            return j.load(book)
            #print(type(j.load(book)))
            #book_dic = j.load(book)
            #activity = choise_activity()
            print('q')
    except FileNotFoundError:
        print(FileNotFoundError.__doc__)
        return

if __name__ == '__main__':
    main()

    print(book_dic)