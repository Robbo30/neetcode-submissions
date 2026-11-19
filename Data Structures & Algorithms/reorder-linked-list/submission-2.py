# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # curr = head
        # nodes = []

        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # left = 0
        # right = len(nodes) - 1

        # while right > left:
        #     nodes[left].next = nodes[right]
        #     left += 1
        #     nodes[right].next = nodes[left]
        #     right -= 1

        # nodes[left].next = None # removes last pointer 



        # Real Solution
        slow = head
        fast = head.next
        while fast and fast.next:   # when fast reaches the end, slow will be at midpoint as it travelled half the distance
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None    # cuts after slow to make 2 halfs of the list
        prev = None
        
        while second:   # using second has the head of the 2nd list, we reverse the entire 2nd list
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
            # ends with head for 1st half, and prev for the 2nd half

        first = head    # prevents actually moving head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2



