#Compress a string using the counts of repeated characters (e.g., aaabb → a3b2).
def compress_string(input_string):
    compressed = ""
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed += input_string[i-1] + str(count)
            count = 1
    compressed += input_string[-1] + str(count)
    return compressed
string = "aaabb"
compressed_string = compress_string(string)
print(f"The string '{string}' compresses string is '{compressed_string}'")