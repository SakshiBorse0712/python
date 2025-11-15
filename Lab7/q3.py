mapping = {
    'a':'q','b':'w','c':'e','d':'r','e':'t','f':'y','g':'u','h':'i',
    'i':'o','j':'p','k':'a','l':'s','m':'d','n':'f','o':'g','p':'h',
    'q':'j','r':'k','s':'l','t':'z','u':'x','v':'c','w':'v','x':'b',
    'y':'n','z':'m'
}
def substitution_encrypt(text, mapping):
    encrypted = ""
    for ch in text:
        lower = ch.lower()
        if lower in mapping:
            new_char = mapping[lower]
            encrypted += new_char.upper() if ch.isupper() else new_char
        else:
            encrypted += ch
    return encrypted

def substitution_decrypt(text, mapping):
    reverse_map = {v: k for k, v in mapping.items()}
    decrypted = ""
    for ch in text:
        lower = ch.lower()
        if lower in reverse_map:
            new_char = reverse_map[lower]
            decrypted += new_char.upper() if ch.isupper() else new_char
        else:
            decrypted += ch
    return decrypted


text = input("Enter a String: ")
enc = substitution_encrypt(text, mapping)
dec = substitution_decrypt(enc, mapping)

print("Encrypted:", enc)
print("Decrypted:", dec)