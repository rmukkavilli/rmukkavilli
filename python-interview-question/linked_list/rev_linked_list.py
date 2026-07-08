class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def reverse_linkedlist(head):
#     prev = None
#     curr = head

#     while curr:
#         curr_next = curr.next      # Save next node
#         curr.next = prev           # Reverse pointer
#         prev = curr                # Move prev
#         curr = curr_next           # Move curr

#     return prev

def cycle_list(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if slow == fast:
        return True
    return False


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Create Linked List
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
#head.next.next.next.next = Node(5)

print("Original:")
print_list(head)

#head = reverse_linkedlist(head)
print(cycle_list(head))

print("Reversed:")
print_list(head)