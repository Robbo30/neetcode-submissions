# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # nodes = []
        # curr = head
        
        # while curr: # add all the nodes to an array to make them easier to swap
        #     nodes.append(curr)
        #     curr = curr.next

        # left = 0
        # right = len(nodes) - 1
        # while right > left: # loop through all nodes
        #     nodes[left].next = nodes[right] # make first node point to last node
        #     left += 1   # move left forward so now on next node
        #     nodes[right].next = nodes[left] # make the old last node point to the next node
        #     right -= 1  # move right inwards 
        
        # nodes[left].next = None # make last node point to nothing



        # Real Solution
        slow = head
        fast = head.next

        while fast and fast.next:   # while fast and fast.next arent the last nodes
            slow = slow.next    # slow will end up on the mid point of the list
            fast = fast.next.next

        second = slow.next  # get node after mid point and disconnect it making 2 seperate lists
        slow.next = None

        prev = None
        while second:   # now reverse the 2nd half list 
            temp = second.next  
            second.next = prev  # move the nodes pointer backwards  
            prev = second   # move prev forward onto current node, ready for next loop
            second = temp   # move second forward to next node
        
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        
        


