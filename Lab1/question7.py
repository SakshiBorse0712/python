# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

n = input("Enter first string: ")
m = input("Enter second string: ")

if len(n) >= 2 and len(m) >= 2:
    new_str1 = m[:2] + n[2:]
    new_str2 = n[:2] + m[2:]
    result = new_str1 + " " + new_str2
else:
    result = n + " " + m 


print("Result:", result)