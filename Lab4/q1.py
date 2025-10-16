#Write a Python program to find all the values in a list are greater than a specified number. 

num = [10, 20, 30, 40, 50]
n = int(input("Enter a number to compare: "))

if all(i > n for i in num):
    print(f"All the values in the list are greater than {n}.")
else:
    print(f"Not all values in the list are greater than {n}.")
