#Write a function to count the occurrences of a specific character in a string
def string_occurrence(input_string, char_to_count):
        count = 0
        for char in input_string:
            if char == char_to_count:
                count += 1
        return count
string = "hello world"
char = "l"
count = string_occurrence(string, char)
print(f"The character '{char}' appears {count} times in the string.")