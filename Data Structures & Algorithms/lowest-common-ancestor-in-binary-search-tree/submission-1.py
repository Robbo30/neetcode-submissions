# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if not root or (root == p) or (root == q):
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)   # finds LCA of left
        # right = self.lowestCommonAncestor(root.right, p, q) # finda LCA of right

        # if left and right:  # both have values but are on opposite sides of the tree, meaning the only node that can be valid for it, is the root
        #     return root
        # elif left:  # if left have LCA then we return left
        #     return left
        # elif right: # if right have LCA then we return right
        #     return right
        # else:
        #     return None



        # BST Version
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr # the first node where the paths are seperate (as p or q is on different sides)
