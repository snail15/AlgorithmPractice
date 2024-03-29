def oddEvenList(self, head: ListNode) -> ListNode:

    if not head:
        return head
    
    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    
    odd.next = evenHead

    return head