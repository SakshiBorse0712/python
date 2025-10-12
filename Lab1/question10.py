# Use sys.getsizeof() to print their memory sizes.

import sys

a = 42
b = "Hello"

print(f"Size of integer a: {sys.getsizeof(a)} bytes")
print(f"Size of string b: {sys.getsizeof(b)} bytes")