#Write a program to demonstrate multiple inheritance.
class Inheritance:
    def greet(self):
        print("Hello world!")
class Inheritance1:
    def greet1(self):
        print("Hi")
class Inheritance2(Inheritance, Inheritance1):
    def greet2(self):
        print("success")
obj = Inheritance2()
obj.greet()
obj.greet1()
obj.greet2()