"""Creating a class of Linked list
"""


class ListNode:
    """Defining ListNode"""

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    """Printing in Travserse"""
    @staticmethod
    def print_traverse(head):
        current = head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print(None)

    @staticmethod
    def print_reverse(node):
        if node is None:
            return
        ListNode.print_reverse(node.next)
        print(node.value, end=" -> ")


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    # Link the Node
    node1.next = node2
    node2.next = node3
    node3.next = node4

    #print in about traverse and reverse
    ListNode.print_traverse(node1)
    ListNode.print_reverse(node1)
    print()
