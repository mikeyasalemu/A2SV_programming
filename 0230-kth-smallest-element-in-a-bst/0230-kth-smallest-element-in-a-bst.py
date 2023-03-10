# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.helper(root)
        self.arr.sort()
        return self.arr[k -1]
    def helper(self,root):
        if root:
            self.arr.append(root.val)
            self.helper(root.left)
            self.helper(root.right)
            return 
        return