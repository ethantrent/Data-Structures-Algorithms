# LIFO

stk = []
print(stk)

# Append to top of stack - O(1)
stk.append(1)
stk.append(2)
stk.append(3)
print(stk)

# Pop from top of stack - O(1)
x = stk.pop()
print(x)
print(stk)

# Peek at top of stack - O(1)
x = stk[-1]
print(x)

# Check if stack is empty - O(1)
is_empty = len(stk) == 0
print(is_empty)

if stk:
    print(True)
