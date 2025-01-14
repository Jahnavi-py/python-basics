#Create a module with a function to reverse a string 'mstring_utils.py 'and import it into another program.
import mstring_utils
Original_string = "Welcome to Python Programming"
Reversed_string = mstring_utils.reverse_string(Original_string)
print(f"Original String : '{Original_string}', Reverse String : '{Reversed_string}'")