# Ask the user for a string containing lowercase letters, uppercase letters, digits or underscores or combination of all. Write a Python program to check whether the string is a valid identifier.

import keyword

n = input("Enter a string: ")

if n.isidentifier():
    if keyword.iskeyword(n):
        print(f"'{n}' is a Python keyword, so it is NOT a valid identifier.")
    else:
        print(f"'{n}' is a valid Python identifier.")
else:
    print(f"'{n}' is NOT a valid Python identifier.")
