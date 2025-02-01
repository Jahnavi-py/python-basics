#Write a program that uses nested try blocks to handle different exceptions (e.g., IndexError, KeyError).
my_list = [1,2,3]
my_dict = {'name': 'J', 'age': 25}
def handle_exception():
    try:
        print("Trying to access an element in the list:")
        try:
            print(my_list[5])  # This will raise an IndexError
        except IndexError:
            print("Error: Index out of range in the list!")
        print("\nTrying to access a key in the dictionary:")
        try:
            print(my_dict['address'])  # This will raise a KeyError
        except KeyError:
            print("Error: Key not found in the dictionary!")
    except Exception as e:
            print(f"An unexpected error occurred: {e}")
handle_exception()