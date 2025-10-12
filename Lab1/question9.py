# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.


n = input("Enter a string: ")

if len(n) < 2:
    result = n 
else:
    result = n[-1] + n[1:-1] + n[0]

print("Result:", result)
