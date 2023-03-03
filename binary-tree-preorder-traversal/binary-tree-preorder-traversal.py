# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr= []
        self.helper(root)
        return self.arr
    def helper(self,curr):
        if not curr:
            return
        self.arr.append(curr.val)
        self.helper(curr.left)
        self.helper(curr.right)
        
        