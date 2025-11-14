message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

def encryptfun():
    encrypt = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypt += chr((ord(char) - base + shift) % 26 + base)
        else :
            encrypt += char
    return encrypt

def decryptfun():
    decrypt = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypt += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypt += char
    return decrypt

print("Original message:", message)
print("Encrypted message:", encryptfun())
print("Decrypted message:", decryptfun())