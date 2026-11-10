"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = {None : None} # makes hash map and adds edge case

        current = head
        while current:  # goes through and adds each node to the copy list with the value showing what old node they belonged to
            copy = Node(current.val)
            old[current] = copy
            current = current.next

        current = head
        while current:  # goes through and assigns the next and random pointers to each copied node
            copy = old[current]
            copy.next = old[current.next]
            copy.random = old[current.random]
            current = current.next

        return old[head]    # returns the head of the new copied list
