# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:    # whilst either has a value left we still need to add together
            if l1:  # if l1 has a value left set val to it
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2:  # if l2 has a value left set val2 to it 
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            sum = val1 + val2 + carry   # work out the carry and leftover amount
            carry = sum // 10
            leftover = sum % 10

            current.next = ListNode(leftover)   # make a new node with the leftover value and make current point to it
            current = current.next  # then increment current pointer

        return dummy.next

        