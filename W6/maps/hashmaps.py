# aka Dictionary
d = {'ethan': 1, 'bob': 2, 'sue': 3}
print(d)

# Add key:val - O(1)
d['tim'] = 4
print(d)

# Check if key exists - O(1)
if 'ethan' in d:
    print(True)

# Check if value exists with key - O(1)
print(d['ethan'])

# Loop over key:val pairs - O(n)
for key, val in d.items():
    print(f"key: {key} -> val: {val}")


# ADDITIONAL DICTIONARY OPERATIONS

# Defaultdict - O(1) for getting default value
from collections import defaultdict

default = defaultdict(int)
default[2]
default[3]
default[4]
print(default)

# Counter - O(n) to count occurrences
from collections import Counter

string = 'hello world'
counter = Counter(string)
print(counter)
