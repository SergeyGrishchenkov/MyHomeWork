# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor

my_dog = Dog(5)
print(f'My dog\'s age is {my_dog.age}.\nHuman age of my dog is {my_dog.human_age()}')