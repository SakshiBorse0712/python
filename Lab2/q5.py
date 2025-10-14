s = input("Enter a string: ")
letters = digits = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)
