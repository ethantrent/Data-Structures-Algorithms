s = set()
print(s)

# Add item - O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

# Lookup if item exists - O(1)
if 1 in s:
    print(True)

# Remove item - O(1)
s.remove(3)
print(s)

string = 'aaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccceeeeeeeeeee'
sett = set(string) # O(S) where S is the size of the string
print(sett)

# Iterate through set - O(n)
for x in s:
    print(x)