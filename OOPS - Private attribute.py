#.Create a class Employee with private attributes and getter and setter methods.
from cohere.utils import get_id


class Employee:
    def __init__(self, name, ID):
        self.__name = name
        self.__ID = ID
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_id(self):
        return self.__ID
    def set_id(self, ID):
        self.__ID = ID
employee = Employee("Jahnavi", 123)
print(f"Name: {employee.get_name()}")
print(f"ID: {employee.get_id()}")
employee.set_name("Janu")
employee.set_id(456)
print(f"Updated Name : {employee.get_name()}")
print(f"Updated Id : {employee.get_id()}")