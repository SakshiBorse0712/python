#Write a Python program to find the list of words that are longer than n from a given list of words. (Use mystr.split()) 

mystr = input("Enter a sentence :")

words = mystr.split()

n = int(input("Enter a number:"))

result = [i for i in words if len(i)>n]

print(f"Words that is/are longer than n is/are {result}")