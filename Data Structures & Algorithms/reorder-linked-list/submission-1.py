# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next

        left = 0
        right = len(nodes) - 1

        while right > left:
            nodes[left].next = nodes[right]
            left += 1
            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None # removes last pointer 