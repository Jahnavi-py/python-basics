#Remove all occurrences of a specific word from a string
input_string = "Python is easy to read and write."
word_remove = "and write"
result_string = input_string.replace(word_remove, "")
print(f"The string '{input_string}'\nthe word removed from string '{word_remove}'\n"
      f"and results in '{result_string}'")

#for removing space
input_string1 = "Python is easy to read and write."
word_remove1 = "and write"
result_string1 = input_string1.replace(word_remove1, "").strip()
result_string1 = " ".join(result_string1.split())

print(f"The string '{input_string1}' with the word removed '{word_remove1}' "
      f"results in: '{result_string1}'")
