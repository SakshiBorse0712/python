#Encrypt and decrypt a message using the Caesar Cipher with a given shift.

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypt = ""
for char in message:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        encrypt += chr((ord(char) - base + shift) % 26 + base)
    else :
        encrypt += char


decrypt = ""
for char in message:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        decrypt += chr((ord(char) - base - shift) % 26 + base)
    else:
        decrypt += char


print("Original message:", message)
print("Encrypted message:", encrypt)
print("Decrypted message:", decrypt)