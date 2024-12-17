#Implement a program that exits only when the user inputs "quit".
while True:
    user_input = input("Enter something (type 'quit' to exit): ")
    if user_input.lower() == "quit":  # Check if the input is 'quit' (case-insensitive)
        print("Exiting the program.")
        break
    else:
        print(f"You entered: {user_input}")

