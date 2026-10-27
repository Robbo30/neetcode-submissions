# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # prev = None # set up pointers

        # while curr: # while curr isnt "None" means there is nodes left
        #     nxt = curr.next # gets the next node after curr and stores it
        #     curr.next = prev    # flip the nodes
        #     prev = curr # updates previous to the current node so the next loop has the correct previous value
        #     curr = nxt  # move forward in list

        # return prev



        # Real Solution
        if not head:    # if head is empty return None
            return None
        
        newHead = head
        if head.next:   # if the head has a node
            newHead = self.reverseList(head.next)   # recurisvely call the function to reverse the next head
            head.next.next = head   # update the next pointer
        head.next = None

        return newHead
