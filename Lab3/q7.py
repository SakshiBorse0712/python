s = input("Enter a string: ")

longest = 0
current = ""
for char in s:
    if char not in current:
        current += char
        longest = max(longest, len(current))
    else:
        index = current.index(char)
        current = current[index + 1:] + char

print("Length of longest substring without repeating characters:", longest)
