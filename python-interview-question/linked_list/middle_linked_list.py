class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mid_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)
    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(mid_node(head))