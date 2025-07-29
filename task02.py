class Student:
    def __init__(self, name, age, grade):
        self.name = name       
        self.age = age 
        self.grade = grade  

    def malumot(self):
        print(f"{self.name}, {self.age} yosh, {self.grade}")

student1 = Student("Aliyev Vali", 15, "9-sinf")
student2 = Student("Karimova Malika", 14, "8-sinf")
student3 = Student("Toxtayev Diyor", 16, "10-sinf")

student1.malumot()
student2.malumot()
student3.malumot()
