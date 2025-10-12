# Check whether 0.1+0.2 = 0.3 holds true in Python? If not find the ways to make it true.

n = 0.1 + 0.2
m = 0.3

if m==n :
    print(f"{m} and {n} are same")
else :
    print(f"{m} and {n} are not same")


from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.3')

print(a + b == c) 