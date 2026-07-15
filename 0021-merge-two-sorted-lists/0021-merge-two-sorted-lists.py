class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (handling the head)
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # If one list is not empty, attach the rest of it to the tail
        # (We don't need a loop here because the rest of the list is already connected and sorted)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # Return the next node after dummy, which is the actual head
        return dummy.next