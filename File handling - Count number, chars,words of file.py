#Count the number of lines, words, and characters in a file.
def count_lines_words_chars(filename):
  lines = 0
  words = 0
  chars = 0
  with open(filename, 'r') as file:
    for line in file:
      lines += 1
      words += len(line.split())
      chars += len(line)
  return lines, words, chars
filename = "files.txt"
lines, words, chars = count_lines_words_chars(filename)
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
print(f"Number of characters: {chars}")