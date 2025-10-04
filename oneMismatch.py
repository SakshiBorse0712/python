text = input("Enter text:")
substring = input("Enter substring:")

found = False  

for i in range(len(text) - len(substring) + 1):
    mismatches = 0
    for j in range(len(substring)):
        if text[i + j] != substring[j]:
            mismatches += 1
        if mismatches > 1:   
            break
    if mismatches <= 1:
        found = True
        break

if found:
    print("Substring found with at most 1 mismatch.")
else:
    print("Substring not found.")
