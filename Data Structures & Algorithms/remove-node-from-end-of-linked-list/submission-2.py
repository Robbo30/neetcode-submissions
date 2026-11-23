# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:    # moves right forward n times, so the gap between right and left is now n
            right = right.next
            n -= 1
        
        while right:    # then moves both of the pointers forward until right == None
            left = left.next
            right = right.next

        # so right is now at the end of the list, and left is n + 1 nodes away from the end (as it started on dummy)

        left.next = left.next.next  # removes the node after left (the nth node)
        return dummy.next

