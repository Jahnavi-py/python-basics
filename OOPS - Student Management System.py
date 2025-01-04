#.Build a StudentManagement system to add, delete, and search student records using OOP principles
class Student:
    def __init__(self, name,age, student_id):
        self.__name = name
        self.__age = age
        self.__student_id = student_id
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_student_id(self):
        return self.__student_id
    def display_info(self):
        print(f"Student ID: {self.__student_id}, Name: {self.__name}, Age: {self.__age}")
class StudentManagementSystem:
    def __init__(self):
        self.__Students = []
    def add_student(self, student):
        self.__Students.append(student)
        print(f"Student {student.get_name()} added successfully.")
    def delete_student(self, student_id):
        for student in self.__Students:
            if student.get_student_id() == student_id:
                self.__Students.remove(student)
                print(f"Student with ID {student_id} deleted successfully.")
                return
        print(f"Student with ID {student_id} not found.")
    def search_student(self, search_term):
        for student in self.__Students:
            if student.get_name().lower() == search_term.lower() or student.get_student_id() == search_term:
                student.display_info()
                return
        print(f"Student with name/ID '{search_term}' not found.")
    def  display_all_students(self):
        if not self.__Students:
            print("No students found.")
        else:
            print("\n--- List of Students ---")
            for student in self.__Students:
                student.display_info()
if __name__ == "__main__":
    # Create the StudentManagementSystem instance
    sms = StudentManagementSystem()
    student1 = Student("Alice", 20, "S001")
    student2 = Student("Bob", 22, "S002")
    student3 = Student("Charlie", 19, "S003")
    sms.add_student(student1)
    sms.add_student(student2)
    sms.add_student(student3)
    sms.display_all_students()
    print("\nSearching for student 'Bob':")
    sms.search_student("Bob")
    print("\nSearching for student ID 'S003':")
    sms.search_student("S003")
    print("\nDeleting student with ID 'S002':")
    sms.delete_student("S002")
    sms.display_all_students()
    print("\nAttempting to delete a non-existent student with ID 'S005':")
    sms.delete_student("S005")