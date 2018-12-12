""" Inheritance in python enables developers to reuse code :: shorter code """


class Student:
    def __init__(self, name, campus):
        self.name = name
        self.campus = campus
        self.grades = []

    def average(self):
        return sum(self.grades) / (len(self.grades))


# Extend the student class to access the data in the class
class WorkingStudent(Student):
    def __init__(self, name, campus, salary):
        super().__init__(name, campus)
        self.salary = salary


print('')
# Create objects of the class
student_one = Student('vick', 'MIT')
student_one.grades.append(89)
student_one.grades.append(90)
student_one.grades.append(89)
student_one.grades.append(98)
student_one.grades.append(99)
print(student_one.name, student_one.campus, student_one.grades)
print(f'{student_one.name}s Average grade is {student_one.average()} ')

print('')

student_two = WorkingStudent('Roseline', 'Harvard', 760000)
student_two.grades.append(89)
student_two.grades.append(99)
student_two.grades.append(87)
student_two.grades.append(96)
student_two.grades.append(100)
print(student_two.name, student_two.campus, student_two.salary, student_two.grades)
print(f'{student_two.name}s Average grade is {student_two.average()} ')
