class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    pass

s1 = Student("kourosh",14)
print(s1.name, s1.age)