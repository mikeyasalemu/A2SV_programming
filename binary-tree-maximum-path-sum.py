# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max=root.val
        self.currentsum(root)
        return self.max
    
    def currentsum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = max(0,self.currentsum(root.left))
            right = max(0,self.currentsum(root.right))
            
            self.max=max(self.max,root.val+left+right)
            
            return root.val+max(right, left)