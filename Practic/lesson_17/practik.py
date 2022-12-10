# Task 1. /* Chicken factory
# Write Factory (Factory) for the production of chickens (Hen)
# 1. Create class Chicken
# 1.2. Add a method getNumberOfEggs() to the class
# 1.3. Add a method getDescription() to the class that returns the string "I'm a chicken."
# 2. Create a KyivChiken class that inherits from Chicken
# 3. Create a LvivChicken class that inherits from Chicken
# 4. Create a OdessaChicken class that inherits from Chicken
# 5. In each of the classes, write your own implementation of the getNumberOfEggs() method.
# Methods must return the number of eggs per month from a given type of hen.
# 6. In each of the classes, write your own implementation of the getDescription method.
# Methods should return a string like:
# <getDescription() of the parent class> + <"My City is ******. I lay N eggs a month.">
# 7. Move all classes that you created to a separate modules
# class Chiken:
#
#     def getNumberOfEggs(self):
#         raise NotImplemented("method is not defined!!!")
#
#     def getDescription(self):
#         return "Chicken factory "
#
#
# class KyivChicken(Chiken):
#     def getNumberOfEggs(self):
#         return 100_000
#     def getDescription(self):
#         return f"{super().getDescription()} . My City is {self.__class__.__name__.replace('Chicken', '')}. I lay {self.getNumberOfEggs()} eggs a month."
#
# class LvivChicken(Chiken):
#     def getNumberOfEggs(self):
#         return 200_000
#
#     def getDescription(self):
#         return f"{super().getDescription()} . My City is {self.__class__.__name__.replace('Chicken', '')}. I lay {self.getNumberOfEggs()} eggs a month."
#
#
# class OdessaChicken(Chiken):
#     def getNumberOfEggs(self):
#         return 50_000
#
#     def getDescription(self):
#         return f"{super().getDescription()} . My City is {self.__class__.__name__.replace('Chicken', '')}. I lay {self.getNumberOfEggs()} eggs a month."
#
#
# c_k = KyivChicken()
# print(c_k.getNumberOfEggs())
# print(c_k.getDescription())
import self


# Task 2.
# 1. You have a class Person:
# class Person:
#   def __init__(self, name, job=None, pay=0, part_time=1):
#     self.name = name
#     self.job = job
#     self.base_pay = pay
#     self.part_time = part_time
#   def pay(self):
#     return int(self.base_pay * self.part_time)
# 2.Add 2 child classes: Teacher and Student. Create their own pay() methods
# 3.Add __str__ methods to classes that displays the name of the Person and its salary (result from pay() method)
# 4.Create one Teacher and 10 Students
# 5.Calculate sum of all money spent on salaries
#
# class Person:
#     def __init__(self, name, job=None, pay=0, part_time=1):
#         self.name = name
#         self.job = job
#         self.base_pay = pay
#         self.part_time = part_time
#
#     def pay(self):
#         return int(self.base_pay * self.part_time)
#
# class Teacher(Person):
#     def pay(self):
#         if self.part_time <= 1:
#             return super().pay()
#         else:
#             return super().pay() + (self.part_time - 1) * 0.5 * self.base_pay
#
#     def __str__(self):
#         print(f'Teacher Name is: {self.name}\nSalary for job {self.job} is:{self.pay()}')
#
# class Student(Person):
#     def pay(self):
#         return 1000
#     def __str__(self):
#         print(f'Student Name is: {self.name}\nSalary is:{self.pay()}')
#
# list = [Teacher('Vika', 'Teacher', 300000, 1.5),
#         Student('Roman'),
#         Student('Sergey')
#         ]
# FOT = 0
# for item in list:
#     item.__str__()
#     FOT += item.pay()
#
# print(f'Common FOT is: {FOT}')
# 1.Create classes House, Private House and Apartment House.
# 2.In the parent class (in our case, the House class), an empty method is created (for example, the build() method).
# 3.In child classes, methods of the same name are created, but with the corresponding implementation.
# For example, for the construction of an apartment building, it is necessary to use a tower crane,
# and a private house can be built on its own.
# 4.Add decorator to build method, that will calculate how long the build process oh the house took.
class House:
    def __init__(self, floores):
        self.floores = floores

    def build(self):
        pass

class PrivateHouse(House):

    def __init__(self, floores, crane_necessary=False):
        super().__init__(floores)
        self.crane_necessary = crane_necessary

    def dec_build(func):
        def warp(self):
            result = func(self)
            print(f'For building we need {result}')
        return warp

    @dec_build
    def build(self):
        return self.floores * 30 + ((self.floores * 3) if self.crane_necessary else 0)


class ApartmentHouse(House):

    def __init__(self, floores, crane_necessary=True):
        super().__init__(floores)
        self.crane_necessary = crane_necessary

    def build(self):
        return self.floores * 40 + ((self.floores * 3) if self.crane_necessary else 0)


pr = PrivateHouse(3, True)

ap = ApartmentHouse(16)

print(pr.build())
print('*'*20)

def dec2(f):
    def wr():
        r = f()
        print(f'dfbdsnb {r}')
    return wr

print(ap.build())
print('*'*20)

test = dec2(ap.build())
