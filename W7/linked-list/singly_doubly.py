# SINGLY LINKED LIST
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
a = SinglyNode(3)
b = SinglyNode(4)
c = SinglyNode(7)

Head.next = a
a.next = b
b.next = c

# print(Head)

# Traverse linked list - O(n) due to visiting all nodes
curr = Head

while curr:
    print(curr)
    curr = curr.next

# Display singly linked list - O(n)
def display_singly(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

display_singly(Head)

# Search for node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

print(search(Head, 7))

# DOUBLY LINKED LIST
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    
head = tail = DoublyNode(1)
print(tail)

# Display doubly linked list - O(n)
def display_doubly(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))

display_doubly(head)

# Insert at beginning - O(1)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display_doubly(head)

# Insert at end - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display_doubly(head)