class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reorder_list(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second_head = slow.next
    print(second_head.val)
    slow.next = None
    return second_head
    
    
# reversing from secound head
def reverse_list(second_head):
    prev = None
    curr = second_head
    while curr:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev

def merge_lists(head, second_head):
    # 1-> 2-> 3
    # 5-> 4
    first_curr = head
    second_curr = second_head

    while first_curr and second_curr:
         # Save first curr next
        first_next = first_curr.next
        # link first_curr to second_curr
        first_curr.next = second_curr
        #save second curr next
        second_next = second_curr.next
        # link second curr next to firstcurr.next
        second_curr.next = first_next

        # move to next node
        first_curr = first_next
        second_curr = second_next
    return head

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
head.next.next.next.next = Node(5)

print("Original:")
second_head = reorder_list(head)
reversed_second = reverse_list(second_head)
print_list(head)
print_list(reversed_second)
merge_lists(head, second_head)
print(head)
