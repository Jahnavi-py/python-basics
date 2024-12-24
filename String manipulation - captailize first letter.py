#Capitalize the first letter of each word in a string (similar to title()).
string = "python is easy to learn"
Capitalize_first_word= " ".join(word.capitalize() for word in string.split())
print(f"The string capitalize first word is :  {Capitalize_first_word}")