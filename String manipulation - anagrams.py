#Write a program to check if two strings are anagrams.
string1 =  "listen"
string2 = "silent"
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
#are_anagrams = (sorted(string1) == sorted(string2))
if sorted(string1) == sorted(string2) :
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")