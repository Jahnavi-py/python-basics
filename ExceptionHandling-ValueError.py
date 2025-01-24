#Create a program that handles a ValueError when trying to convert user input to an integer.
def get_integer():
    try:
        user_input = input("Enter the number:")
        user_number = int(user_input)
        print(f"You entered the number: {user_number}")
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
get_integer()