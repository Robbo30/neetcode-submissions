class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:  # while both lists still have nodes
            if list1.val <= list2.val:  # we want to add the smallest next node from the 2 lists
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2  # point tail towards next node in list
                list2 = list2.next  # update the next node in list
                tail = tail.next    # update tail pointer 
        
        if list1:   # if list1 has any nodes left, point towards it
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next



