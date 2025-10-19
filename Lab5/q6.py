class BadHash:
    def __init__(self, value):
        self.value = value
    def __hash__(self):
        return 42
    def __eq__(self, other):
        return isinstance(other, BadHash) and self.value == other.value
    def __repr__(self):
        return f"BadHash({self.value})"

import time
data = {}
start = time.time()
for i in range(100000):
    data[BadHash(i)] = i
end = time.time()
print("Inserted 100000 items in:", round(end - start, 3), "seconds")
