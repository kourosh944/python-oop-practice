class Employee:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Name: {self.name}")

class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def introduce(self):
        super().introduce()
        print(f"Language: {self.language}")

p1 = Programmer("kourosh","python")
p1.introduce()
