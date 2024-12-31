#Write a program to check if two strings are anagrams.
string1 =  "listen"
string2 = "silent"
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
if sorted(string1) == sorted(string2) :
    print(f"'{string1} 'and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
string3 = "Pen"
string4 = "Python"
string3 = string3.replace(" ", "").lower()
string4 = string4.replace(" ", "").lower()
if sorted(string3) == sorted(string4) :
    print(f"'{string3} 'and '{string4}' are anagrams.")
else:
    print(f"'{string3}' and '{string4}' are not anagrams.")