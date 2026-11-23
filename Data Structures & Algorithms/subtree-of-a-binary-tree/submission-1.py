# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:    # cant have a subtree of nothing
            return False

        if self.isSameTree(root, subRoot):  # if are same then its a Subtree
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)  # if the root and subRoot arent the same, then we see if either of the roots children would work instead
    
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:    # if both are empty then counts as a Subtree
            return True
        
        if root and subRoot and root.val == subRoot.val:    # if values are the same and both not empty, then recursively see if their children are also the same
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        else:
            return False
            


        