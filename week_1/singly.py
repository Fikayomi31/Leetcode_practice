"""Basic implementation of singly linked list
"""

class ListNode:
    """Defining listNode"""

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


#create Node
node1 = ListNode(6)
node2 = ListNode(4)
node3 = ListNode(7)

nod1 = ListNode(3)
nod2 = ListNode(2)
nod3 = ListNode(5)

#Link nodes
node1.next = node2
node2.next = node3

nod1.next = nod2
nod2.next = nod3

#traversal
current = node1
while current:
    print(current.value, end=" -> ")
    current = current.next
