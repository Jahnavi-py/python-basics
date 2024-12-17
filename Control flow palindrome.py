#Write a program to check if a number is a palindrome.
input_string = input("Enter a string: ")
is_palindrome = input_string.replace(" ", "").lower()
if is_palindrome == is_palindrome[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')