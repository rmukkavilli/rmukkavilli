class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def cycle_detect(head):
    slow = head
    fast = head
    if head is None:
        return False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("slow", slow.data, "fast", fast.data)
            return True
    return False

head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)
head.next.next.next.next = head.next

print(cycle_detect(head))