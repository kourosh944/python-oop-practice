class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

s1 = Student("kourosh",14,9213)
print(s1.name,s1.age,s1.student_id)