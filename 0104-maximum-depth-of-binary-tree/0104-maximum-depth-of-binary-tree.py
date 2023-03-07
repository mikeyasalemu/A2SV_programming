# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,0)
    def helper(self,root,count):
        if not root:
            return count
        right = self.helper(root.right,count+1)
        left  = self.helper(root.left,count+1)
        
        return max(right,left)