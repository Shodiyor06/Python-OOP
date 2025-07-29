class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def show_info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade} - sinf o'quvchi")

student1 = Student("Ali", 20, "A")
student2 = Student("Vali", 22, "B")
student3 = Student("Hasan", 21, "C")
student4 = Student("Olim", 19, "D")
student5 = Student("Zarina", 23, "E")

student1.show_info()
student2.show_info()
student3.show_info()
student4.show_info()
student5.show_info()

students = [student1, student2, student3, student4, student5]

oldest = max(students, key=lambda s: s.age)
print("Eng katta yoshdagi talaba:")
oldest.show_info()
