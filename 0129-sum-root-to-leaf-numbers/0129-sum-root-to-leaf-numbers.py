# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = []
        self.dfs(root,[])
        val = 0
        for num in self.ans:
            val+= int(num)
        return val
    def dfs(self,root,arr):
        if not root:
            return 
        arr.append(str(root.val))
        if root.left:
            self.dfs(root.left,arr[:])
        if not root.left and not root.right:
            self.ans.append("".join(arr))
            return
        if root.right:
            self.dfs(root.right,arr[:])