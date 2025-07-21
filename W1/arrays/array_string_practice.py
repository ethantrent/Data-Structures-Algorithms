# ARRAYS aka LISTS
a = [1, 2, 3]
print(a)

# Append - Insert element at end of array - Usually O(1)
a.append(5)
print(a)

# Pop - Delete element at end of array - O(1)
a.pop()
print(a)

# Insert (not end of array) - O(n) due to shifting of elements
a.insert(2, 5)
print(a)

# Modify element - O(1)
a[0] = 7
print(a)

# Accessing element with index - O(1)
print(a[2])

# Check if array has element - O(n) due to searching whole array
if 7 in a:
    print(True)

# Check length - O(1)
print(len(a))

# STRINGS
s = "hello"

# Append to end of string - O(n) due to shifting (immutable)
b = s + 'z'
print(b)

# Check if in string - O(n) due to searching whole string
if 'e' in s:
    print(True)

# Access positions
print(s[2])

# Check length
print(len(s))