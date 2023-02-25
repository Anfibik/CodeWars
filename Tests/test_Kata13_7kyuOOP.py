from py import test
from OOP_Kata.Kata_13_7kyuOOP import Student

test.describe("Last semester. Everything was going fine.")

# Last semester
# Everything is working fine, no angry emails
matthewConnorGrades = [44, 53, 27, 60]
chloeMadisonGrades = [79, 58, 30, 66]
studentGrades = matthewConnorGrades, chloeMadisonGrades
matthewConnor = Student('Matthew', 'Connor', matthewConnorGrades)
chloeMadison = Student('Chloe', 'Madison', chloeMadisonGrades)
students = matthewConnor, chloeMadison

for i, student in enumerate(students):
    test.assert_equals(student.grades, studentGrades[i])

test.describe("New semester. Something is wrong, can you fix it?")

# Very beginning of the semester
# Initialize students, so they can log in to the online report card
johnDoe = Student('John', 'Doe')
janeDoe = Student('Jane', 'Doe')
jamesSmith = Student('James', 'Smith')
jennaSmith = Student('Jenna', 'Smith')
students = johnDoe, janeDoe, jamesSmith, jennaSmith

# First graded assessment
# Update students' grades, so they can see them on the online report card
firstAssessmentGrades = [63, 92, 82, 75]
for i, student in enumerate(students):
    student.add_grade(firstAssessmentGrades[i])

# And then the angry emails started coming in...
for i, student in enumerate(students):
    test.assert_equals(student.grades[0], firstAssessmentGrades[i])