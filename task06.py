class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def malumot(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade} - sinf o'quvchi")

student1 = Student("Ali", 20, "A")
student2 = Student("Vali", 22, "B")
student3 = Student("Hasan", 21, "C")

student1.malumot()
student2.malumot()
student3.malumot()