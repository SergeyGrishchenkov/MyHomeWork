# School
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# nd keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    __slots__ = ('first_name', 'last_name', 'gender', 'age')

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def personal_inf(self):
        print(f'First name:{self.first_name}\nLast name:{self.last_name}\nGender:{self.gender}Age:{self.age}\n')

    def __str__(self):
        return f'{self.__class__.__name__} with name: {self.first_name}'


class Teacher(Person):
    def __init__(self, first_name, last_name, gender, age, subjects: [], salary):
        super().__init__(first_name, last_name, gender, age)
        self.subjects = subjects
        self.salary = salary

    def get_salary(self):
        return self.salary

    def subjects_list(self):
        sb = '\n'.join(self.subjects)
        print(f'Teacher {self.first_name} {self.last_name} conducts the following subjects:\n{sb}')


class Student(Person):
    def __init__(self, first_name, last_name, gender, age, faculty, specialization):
        super().__init__(first_name, last_name, gender, age)
        self.faculty = faculty
        self.specialization = specialization

    def print_study(self):
        print(
            f'Student: {self.first_name} {self.last_name}\nFaculty: {self.faculty}\nSpecialization: {self.specialization}')


if __name__ == '__main__':
    t1 = Teacher('Anna', 'Samon', 'female', 25, ['History', 'Philosophy'], 100000)
    print(t1)
    print(f'Salary: {t1.get_salary()}')
    t1.subjects_list()
    print('*' * 20)
    s1 = Student('Roman', 'Kl', 'male', 20, 'Historical', 'Ukraine')
    print(s1)
    s1.print_study()
