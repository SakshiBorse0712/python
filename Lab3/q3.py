s = input("Enter the original string: ")
old = input("Enter the substring to replace: ")
new = input("Enter the new substring: ")

result = ""
i = 0
n = len(s)
m = len(old)

while i < n:
    if i + m <= n and s[i:i+m] == old:
        result += new
        i += m
    else:
        result += s[i]
        i += 1

print("Result:", result)    