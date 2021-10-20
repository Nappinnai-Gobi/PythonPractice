class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks #0 to 100

    def get_marks(self):
        return self.marks
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            
    def get_average_marks(self):
        value = 0
        for student in self.students:
            value += student.get_marks()
        return value / len(self.students)


s1 = Student("Nikhil", 14, 80)
s2 = Student("Sarvesh", 14, 70)
s3 = Student("Tom", 14, 60)

c1 = Course("Science",3)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
print(c1.get_average_marks())

