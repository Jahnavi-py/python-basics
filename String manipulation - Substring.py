#Write a program to find all substrings of a string.
def substring(input_string):
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substrings.append(input_string[i:j])
    return substrings
input_string = "python"
all_substrings =substring(input_string)
print(f"All substrings of '{input_string}': {all_substrings}")