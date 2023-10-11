# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.last= -float('inf')
        return self.helper(root)
    def helper(self,root):
        if not root:
            return True
       
        
        left = self.helper(root.left)
        if self.last >= root.val:
            return False
        self.last = root.val
        right = self.helper(root.right)
        
        return left and right