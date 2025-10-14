total = 0
count = 0

while True:
    n = int(input("Enter number (0 to stop): "))
    if n == 0:
        break
    total += n
    count += 1

if count > 0:
    avg = total / count
    print("Sum:", total)
    print("Average:", avg)
else:
    print("No numbers entered.")
