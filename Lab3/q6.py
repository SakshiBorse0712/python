paragraph = input("Enter a paragraph: ")

punctuation = '''!()-[]{};:'"\\<>./?@#$%^&*_~,'''
clean_text = ""
for char in paragraph:
    if char not in punctuation:
        clean_text += char

clean_text = clean_text.lower()
print(clean_text)

words = clean_text.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for word, freq in word_freq.items():
    print(f"{word}: {freq}")