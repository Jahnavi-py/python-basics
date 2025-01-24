#Write a Python program to demonstrate exception chaining by raising a TypeError during the handling of a ValueError.
def raise_value_error():
    raise ValueError("This is the initial ValueError.")
def handle_exceptions():
    try:
        raise_value_error()
    except ValueError as e:
        print(f"Caught an exception: {e}")
        raise TypeError("A TypeError occurred while handling ValueError.") from e
try:
    handle_exceptions()
except TypeError as e:
    print(f"Exception Chained: {e}")
    print(f"Original Exception: {e.__cause__}")
