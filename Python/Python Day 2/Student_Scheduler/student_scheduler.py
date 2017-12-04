from student import *

class student_scheduler:

    students = list()

    def addStudent(self,name, rollnumber, courses):
        s = student()
        s.setName(name)
        s.setRollNumber(rollnumber)
        s.setCourseNames(courses)
        self.students.append(s)



    def showAllStudents(self):
        for st in self.students:
           print (st.getRollNumber)

