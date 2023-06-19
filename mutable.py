from typing import List, Optional

# mutability python are mutable except for tuples, strings, integers, floats, and booleans

a = {"id": 456}
b = {"id": 456}

print(id(a))

print(id(b))

c = "test"
d = c

print(id(c))
print(id(d))


# Mutable Default parameters and why there are bad idea

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        print("grades", grades)
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)



