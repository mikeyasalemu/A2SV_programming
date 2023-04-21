# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = []
        self.dfs(root)
        
        return "".join(self.ans)
    def dfs(self,root):
        if not root:
            return ""
        self.ans.append(str(root.val))
        if root.left:
            self.ans.append("(")
            self.dfs(root.left)
            self.ans.append(")")
        if not root.left and root.right:
            self.ans.append("(")
            self.ans.append(")")
        if root.right:
            self.ans.append("(")
            self.dfs(root.right)
            self.ans.append(")")
            
        return root.val
        