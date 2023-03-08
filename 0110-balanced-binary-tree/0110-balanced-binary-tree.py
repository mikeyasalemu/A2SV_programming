# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check =  True  
        self.helper(root,0)
        return self.check
    
    def helper(self,root,count):
        if not root:
            return count
        right = self.helper(root.right,count+1)
        left  = self.helper(root.left,count+1)
        if abs(right - left) > 1:
            self.check = False
        return max(right,left)