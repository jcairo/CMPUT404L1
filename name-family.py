import unittest

class Student(object):
    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.course_marks = {} 

    def addCourseMark(self, course, mark):
        self.course_marks[course] = mark

    def average(self):
        marks_total = 0
        for mark in self.course_marks.values():
            marks_total += mark
        if len(self.course_marks) > 0:
            return marks_total/len(self.course_marks)
        else:
            return None

class StudentTests(unittest.TestCase):

    def setUp(self):
        self.student = Student('Jon', 'Cairo')

    def testCreateStudent(self):
        self.assertTrue(isinstance(self.student, Student), "Not instance of student")
    
    def testAddCourseGrade(self):
        self.student.addCourseMark('CMPUT391', 4)
        self.student.addCourseMark('CMPUT301', 4)
        self.assertTrue(self.student.average() == 4, "Average should be 4")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
