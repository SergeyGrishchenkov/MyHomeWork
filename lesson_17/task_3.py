# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
# Also, create a simple generic function, which takes as input instance of a
# Cat or Dog classes and performs talk method on input parameter.

class Animal:
    def __init__(self, name):
        self.name = name

    #Abctract method
    def talk(self):
        raise NotImplementedError("You must implement the method in Subclass")

class Dog(Animal):
    def talk(self):
        return "woof woof"

    def __str__(self):
        return "Dog"

class Cat(Animal):
    def talk(self):
        return "meow meow"

    def __str__(self):
        return "Cat"

def what_animals_say(creature):
    return creature.talk()

test_case = [Cat('Kisa'), Cat('Murka'), Cat('Yula'), Dog('Polkan'), Dog('Vulkan'), Dog('Snup')]

for item in test_case:
    print(f'Animal {item.__str__()}, which named {item.name}, talk in such way {item.talk()}')
