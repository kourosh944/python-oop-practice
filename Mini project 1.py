class User:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def show_profile(self):
        print(f"Name: {self.name} | Phone: {self.phone}")

class Student(User):
    def __init__(self, name, phone, course, score):
        super().__init__(name, phone)
        self.course = course
        self.score = score

    def show_profile(self):
        super().show_profile()
        print(f"Course: {self.course} | Score: {self.score}")

    def status(self):
        if self.score >= 70:
            return "Accepted"
        else:
            return "Need for greater effort"

class Teacher(User):
    def __init__(self, name, phone, specialty, hourly_rate):
        super().__init__(name, phone)
        self.specialty = specialty
        self.hourly_rate = hourly_rate
    
    def show_profile(self):
        super().show_profile()
        print(f"Specialty: {self.specialty} | Hourly rate: {self.hourly_rate}")
    
    def calculate_salary(self, hours):
        return self.hourly_rate * hours

class OnlineStudent(Student):
    def __init__(self, name, phone, course, score, platform):
        super().__init__(name, phone, course, score)
        self.platform = platform

s1 = Student("kourosh", "09126572345", "Math", 86)
s2 = Student("sara", "09216562345", "Physics", 60)
t1 = Teacher("Reza", "09143879870", "Chemistry", 200000)

print("----------------")

s1.show_profile()
print(s1.status())

print("----------------")

s2.show_profile()
print(s2.status())

print("----------------")

t1.show_profile()
print(t1.calculate_salary(10))

print("----------------")

os1 = OnlineStudent("Mina", "09121234567", "English", 75, "Udemy")
os1.show_profile()
print(os1.status())

print("----------------")