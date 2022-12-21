# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor.
# The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.

from lesson_16.task_1 import Person


class EmailAddress:

    @classmethod
    def check_email(cls, email):
        if not isinstance(email, str):
            raise Exception("Wrong type of email, should be string")
        # далее проверяем на 5 признаков
        # 1. наличие @
        # 2. после символа @ есть символ .
        # 3. после символа @ блоки, разделенные ".", имеют только сиволы буквы и цифры
        # 4. последний блок после "." имеет только буквенное представление
        state = True
        s = email.strip().partition('@')
        if s[1] != '@':
            state = False
        else:
            s1 = s[2].split('.')
            if len(s1) <= 1:
                state = False
            else:
                counter = 0
                while counter < len(s1):
                    if counter == len(s1) - 1:
                        state = s1[counter].isalnum()
                    else:
                        state = s1[counter].isalpha()
                    counter += 1
        if not state:
            raise Exception("Wrong FORMAT of email!")

    def __init__(self, person, email):
        EmailAddress.check_email(email)
        self.person = person
        self.email = email.strip()


if __name__ == '__main__':
    test1 = EmailAddress(Person('Anna', 'Samon', 'female', 25), 'test@eee.com')
    test2 = EmailAddress(Person('Anna', 'Samon', 'female', 25), 'testeee.com')
