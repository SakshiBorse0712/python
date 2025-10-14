temp = input("Enter temperature (e.g. 45F or 102C): ")

degree = int(temp[:-1])   
unit = temp[-1].upper()   

if unit == "C":
    result = (degree * 9/5) + 32
    print(f"{degree}C is {result:.2f}F")
elif unit == "F":
    result = (degree - 32) * 5/9
    print(f"{degree}F is {result:.2f}C")
else:
    print("Invalid input")
