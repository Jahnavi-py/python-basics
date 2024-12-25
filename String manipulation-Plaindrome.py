#Check if a string is a palindrome.
input_string = "No lemon, no melon"
input_string1 = "Python is easy to read and write"
is_palindrome = input_string.replace(" ", "").lower()
is_palindrome1 = input_string1.replace(" ", "").lower()
if is_palindrome == is_palindrome[::-1]:
    print(f"The first string '{input_string}' is a palindrome.")
else:
    print(f"The first string '{input_string}' is not a palindrome.")
if is_palindrome1 == is_palindrome1[::-1]:
    print(f"The first string '{input_string1}' is a palindrome.")
else:
    print(f"The first string '{input_string1}' is not a palindrome.")