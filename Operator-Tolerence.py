# #Check whether two floating-point numbers are approximately equal using a tolerance value.
# tolerance  = 1e-5 #small tolerance  value
# num = float(input("Enter the number : "))
# num1 = float(input("Enter the number1 : "))
# if abs(num - num1) < tolerance :
#     print("num and num1 are approximately equal.")
# else:
#     print("num and num1 are not equal.")




tolerance = 1e-6  # Adjusted tolerance value
num = float(input("Enter the number: "))
num1 = float(input("Enter the number1: "))
if abs(num - num1) < tolerance:
    print("num and num1 are approximately equal.")
else:
    print("num and num1 are not equal.")
