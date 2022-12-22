# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor.
# The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
import re
from lesson_16.task_1 import Person


class EmailAddress:
    __pattern = r'\b[0-9a-zA-Z._-]+@[0-9a-zA-Z.-]+\.[a-zA-Z.]{2,}\b'  # регулярное выражение для проверки валидности

    @classmethod
    def check_email(cls, email):
        try:
            if re.fullmatch(cls.__pattern, email) is None:
                raise Exception
            print('Email address format is CORRECT!!!')
            return True
        except:
            print('Wrong email address format')
            return False



    def __init__(self, person, email):
        email_correct = EmailAddress.check_email(email)
        self.person = person
        self.email = email.strip() if email_correct else ''


if __name__ == '__main__':
    test1 = EmailAddress(Person('Anna', 'Samon', 'female', 25), 'test@eee.com')
    test2 = EmailAddress(Person('Anna', 'Samon', 'female', 25), 'testeee.com')
    test3 = EmailAddress(Person('Anna', 'Samon', 'female', 25), 'test@eee.ccc.com')
    test4 = EmailAddress(Person('Anna', 'Samon', 'female', 25), 'te[st@eee.ccc.com')
