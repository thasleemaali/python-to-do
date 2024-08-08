def print_vowels(string):
    vowels = "aeiouAEIOU"
    for char in string:
        if char == " ":
            continue
        if char in vowels:
            print(char)
string = "Hello World, this is an example string!"
print_vowels(string)