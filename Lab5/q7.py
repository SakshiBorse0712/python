result = {x: (x**2 if x % 2 == 0 else x**3) for x in range(1, 21) if (x**2 if x % 2 == 0 else x**3) % 4 != 0}
print(result)
