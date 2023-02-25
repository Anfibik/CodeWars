"""https://www.codewars.com/kata/5956d127a817c7c51b000026/train/python"""


class Student:

    def __init__(self, first_name, last_name, grades=None):
        if grades is None:
            grades = []
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def grades(self):
        return self.get_average()
#
#
# someStudent = Student('Matthew', 'Connor')
# someOtherStudent = Student('Chloe', 'Madison')
# someStudent.add_grade(98)
# someOtherStudent.add_grade(77)
# print(someStudent.grades)
# print(someOtherStudent.grades)