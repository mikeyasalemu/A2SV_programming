# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        string = []
        self.helper(root,ans,string)
        return ans
    def helper(self,root,ans,string):
        if not root:
            return
        
        string.append(str(root.val))
        
        if not root.right and not root.left:
            ans.append("".join(string))
        string.append("->")
        self.helper(root.left,ans,string)
        self.helper(root.right,ans,string)
        string.pop()
        string.pop()
        return