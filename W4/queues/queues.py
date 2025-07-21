# FIFO

from collections import deque

q = deque()
print(q)

# Enqueue, add to right - O(1)
q.append(1)
q.append(2)
q.append(3)
print(q)

# Dequeue, remove from left - O(1)
q.popleft()
print(q)

# Peek, left - O(1)
print(q[0])

# Peek, right - O(1)
print(q[-1])