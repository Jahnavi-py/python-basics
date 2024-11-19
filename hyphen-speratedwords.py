def sort():
    input_string = input("Enter the hyphen-separated word :")
    words = input_string.split('-')
    words.sort()
    result = '-'.join(words)
    print("Sorted words :" ,result)
sort()