#Implement Run-Length Encoding (RLE) for strings: "aaabbcddd" → "a3b2c1d3".Implement both compression and decompression methods.

text = input("Enter a string :")

compressed=""
c=1

for i in range(1,len(text)):
    if text[i] == text[i-1]:
        c = c+1
    else :
        compressed += text[i-1] + str(c)
        c = 1
compressed += text[-1] + str(c)
print("Original:", text)
print("Compressed:", compressed)

compressed_text = compressed
depressed = ""

for i in range(0,len(compressed_text),2):
    char = compressed_text[i]
    c = int(compressed_text[i+1])
    depressed += char * c

print("Depressed:",depressed)