class College:
    collegeName = 'KNM Inter College' 

class Student(College):
    studentName = None 


student1 = Student()
print(student1.studentName)
print(student1.collegeName)