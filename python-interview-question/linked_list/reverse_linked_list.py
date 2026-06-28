def reverseList(head):
    prev = None
    curr = head

    while curr:
        # Save
        next_node = curr.next
        
        

        # Reverse
        curr.next = prev

        # Advance
        prev = curr
        curr = next_node
        next_node = nextnode.next()

    return prev