def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')
def reverse_string(text):
    return text[::-1]
