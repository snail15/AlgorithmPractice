def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

    preHead = ListNode(0)
    prev = preHead

    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        
        prev = prev.next

    prev.next = l1 if l1 else l2

    return preHead.next