from collections import defaultdict
import time

s = "programming in python"

start = time.time()
freq1 = {}
for ch in s:
    freq1.setdefault(ch, 0)
    freq1[ch] += 1
end = time.time()
print("Using setdefault():", freq1, "Time:", round(end - start, 6))

start = time.time()
freq2 = defaultdict(int)
for ch in s:
    freq2[ch] += 1
end = time.time()
print("Using defaultdict():", dict(freq2), "Time:", round(end - start, 6))
