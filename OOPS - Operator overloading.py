#Write a program to demonstrate operator overloading for a custom ComplexNumber class.
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def __sub__(self, other):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)
    def __str__(self):
        sign = '+' if self.imaginary >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imaginary)}i"
if __name__ == "__main__":
    complex1 = ComplexNumber(3, 4)
    complex2 = ComplexNumber(1, 2)
    print(f"ComplexNumber1: {complex1}")
    print(f"ComplexNumber2: {complex2}")
    result_add = complex1 + complex2
    print(f"For complex numbers : {complex1}, {complex2} : Addition is : {result_add}")
    result_sub = complex1 - complex2
    print(f"For complex numbers : {complex1}, {complex2} : Subtraction is : {result_sub}")
    result_mul = complex1 * complex2
    print(f"For complex numbers : {complex1}, {complex2} : Multiplication is : {result_mul}")