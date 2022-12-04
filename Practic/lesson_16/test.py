# Write a program, to create a child class Teacher (attributes: name, age)
# that will inherit the properties of Parent class Staff (attributes: role, dept, salary).
# Create show_details method in Base class to show role, dept, salary. Create a method totalSalary
# in Teacher class that will calculate total salary for Teacher.

# class Staff:
#     def __init__(self, role, dept, salary):
#         self.salary = salary
#         self.dept = dept
#         self.role = role
#
#     def show_roles(self):
#         print(f'salary is:{self.salary}\ndept is:{self.dept}\nrole is:{self.role}\n')
#
# class Teacher(Staff):
#     def __init__(self, role, dept, salary, name, age):
#         super().__init__(role, dept, salary)
#         self.name = name
#         self.age = age
#
#     def totalSalary(self):
#         return self.salary + (self.age / 100) * self.salary
#
#
# t = Teacher('teacher', 'math', 100_000, 'Marichka', 40)
# t.show_roles()
# print(f'Total salary for {t.name} is: {t.totalSalary()}')

# Statement of student performance in school
# (2 classes: basic - student; derivative - student with a certificate of achievement)
# Basic class (student):
# Variables: name, age, higher education institution.
# Methods: assignments of higher education institution; name change;
# input-output of age information; output of all data.
# Derivative class: a student with a certificate of achievement - an array of grades
# class Student:
#     def __init__(self, name, age=0, higher_education=''):
#         self.name = name
#         self.age = age
#         self.higher_education = higher_education
#
#     def assign_h_edu(self, name):
#         self.higher_education = name
#
#     def change_name(self, new_name):
#         self.higher_education = new_name
#
#     def input_age(self, new_age):
#         self.age = new_age
#
#     def output_age(self):
#         print(f'The age of {self.name} is: {self.age}')
#
#     def output_all(self):
#         print(f'Student name is: {self.name}\nStudent age is: {self.age}\nStudent education is: {self.higher_education}')
#
# class StudentFull(Student):
#     def __init__(self, name, age=0, higher_education='', grades=[]):
#         super().__init__(name, age=0, higher_education='')
#         self.grades = grades
#
#     def add_grades(self, grades_list):
#         self.grades = grades_list
#
#     def output_all(self):
#         print(f'Student name is: {self.name}\nStudent age is: {self.age}'
#               f'\nStudent education is: {self.higher_education}\nGrades are: {self.grades}')
#
#
# st = StudentFull('Artur')
# st.input_age(19)
# st.output_age()
# st.output_all()
# l = [100, 100, 100, 100, 99]
# st.add_grades(l)
# 3. Write a program by creating a Person and Employee classes having the following methods and print the final salary.
# 1 - getInfo() in Person class which prints the info of Person
# 2 - getEmpInfo() - takes the salary, number of hours of work per day of employee as parameter
# 3 - 'AddSal()'   which   adds   $10   to   salary   of   the   employee   if   it   is   less   than   $500.
# 4 - 'AddWork()' which adds $5 to salary of employee if the number of hours of work per day is more than 6 hours

# class Person:
#     def __init__(self, name, age, prof):
#         self.name = name
#         self.age = age
#         self.prof = prof
#
#     def get_info(self):
#         print(f'Name is:{self.name}\nAge is:{self.age}\nPrifession is:{self.prof}')
#
# class Emplotee(Person):
#     def __init__(self, name, age, prof, hours_per_day, salary):
#         super().__init__(name, age, prof)
#         self.hours_per_day = hours_per_day
#         self.salary = salary
#
#     def getEmpInfo(self):
#         super().get_info()
#         print(f'Hours oer week is:{self.hours_per_day}\nSalary is:{self.salary}')
#
#     def add_salary(self):
#         self.salary = self.salary + 10 if self.salary < 500 else self.salary
#
#     def add_work(self):
#         self.hours_per_day = self.hours_per_day + 5 if self.hours_per_day < 6 else self.hours_per_day
#
# em = Emplotee('Igor', 20, 'Programmer', 50, 400)
# em.getEmpInfo()
# print('\n\n---------------')
# em.add_salary()
# em.getEmpInfo()
# print('\n\n---------------')
# em.add_work()
# em.getEmpInfo()

# 4. Add implementation to BankAccount class methods.
# class BankAccount:
#   """Bank Account protected by a pin number."""
#   def __init__(self, pin):
#     """Initial account balance is 0 and pin is 'pin'."""
#   def deposit(self, pin, amount):
#     """Increment account balance by amount and return new balance."""
#   def withdraw(self, pin, amount):
#     """Decrement account balance by amount and return amount withdrawn."""
#   def get_balance(self, pin):
#     """Return account balance."""
#   def change_pin(self, oldpin, newpin):
#     """Change pin from oldpin to newpin."""
# Create a subclass called Savings Account Class:
# Function Members:
# A constructor function to initialize the Savings account data members
# A function that will credit interest to the account
# A function that will debit the account for a withdrawal
# Data Members:
# An annual interest rate value that is credited to the account balance on a monthly basis (edited)
class BankAccount:
    """Bank Account protected by a pin number."""
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        """Initial account balance is 0 and pin is 'pin'."""
    def deposit(self, pin, amount):
        if self.pin == pin:
            self.balance += amount

    def withdraw(self, pin, amount):
        if self.pin == pin:
            self.balance -= amount

    def get_balance(self, pin):
        if self.pin == pin:
            return self.balance

    def change_pin(self, oldpin, newpin):
        if self.pin == oldpin:
            self.pin = newpin

class SavingsAccount(BankAccount):
    pass


test = SavingsAccount(1234, 500)








