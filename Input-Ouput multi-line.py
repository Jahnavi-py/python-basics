#Take a multi-line input and display it with line numbers.
print("Enter multiple lines of text (Press Enter on an empty line to stop):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("\nText with line numbers:")
for index, line in enumerate(lines, start=1):
    print(f"{index}: {line}")
