def digit_letter(input_string):
    digits = 0
    letters = 0
    for char in input_string:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    return  digits,letters
input_string = input("Enter the string: ")
digits, letters = digit_letter(input_string)
print("Number of digits : ", digits)
print("Number of letters : ", letters)

