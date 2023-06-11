
# class
# Magic Method : __str__ and __repr__

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    #call direct class instance then response
    # debugger
    def __str__(self):
        return f"Student name {self.name}"

    # debugger
    def __repr__(self):
        return f"<Student('{self.name}')>"

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Rony", (100, 53, 65))
student2 = Student("Rahman", (80, 60, 65))

print(student)
print(student2.average_grade)





