#Create a class Student with attributes for name and age. Add a method to display student details.
class Student:
    def __init__(self, name, age):
        self. name = name
        self.age = age
    def Student_Details(self):
        print(f"Student Name '{self.name}'")
        print(f"Student Age {self.age}")
student = Student("Jahnavi", 27)
Student.Student_Details()