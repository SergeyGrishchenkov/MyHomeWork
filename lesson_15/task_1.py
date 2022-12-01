# Make a class called Person.
# Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing, for example like this:
# “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')

test_person = Person('Ilon', 'Max', 40)
test_person.talk()