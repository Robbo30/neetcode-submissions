# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next # save referance to rest of the list
            curr.next = prev    # reverse the current nodes pointer
            prev = curr # move prev one step forward
            curr = nxt  # move curr one step forward
        
        return prev # return prev (the new head of the list)
