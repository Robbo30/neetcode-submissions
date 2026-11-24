# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # placeholder node 
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            sum = val1 + val2 + carry
            carry = sum // 10
            remainder = sum % 10

            current.next = ListNode(remainder)  # points the arrow of the previous node to the new node that holds the remainder
            current = current.next
        
        return dummy.next

        