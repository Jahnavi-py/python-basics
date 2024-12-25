# Count and print the frequency of each word in a string.
from collections import Counter
def count_frequency(string):
    frequency =  Counter(string)
    return frequency
string = "Python Programming"
frequency = count_frequency(string)
print(f"The string '{string}' character frequency is '{frequency}'")