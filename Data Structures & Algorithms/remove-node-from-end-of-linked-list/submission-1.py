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

        while n > 0:    # moves right forward n times
            right = right.next
            n -= 1

        while right:    # go forward until right is none, meaning that left is on the node before the one to be removed
            left = left.next
            right = right.next
        
        left.next = left.next.next  # skip over the target node by linking node before it to the node after it (essentialy removing all links to target node)

        return dummy.next   # return dummy as it keeps oringal list 