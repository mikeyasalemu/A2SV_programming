# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root,None)
        return self.ans
    def helper(self,root,par):
        
        if root:
            if not root.left and not root.right :
                if  par and root.val == par.val:
                    return 1 
                else:
                    return 0
            
            count1 = self.helper(root.left,root)
            count2= self.helper(root.right,root)

            self.ans = max(self.ans,count1+count2)
            if par and root.val == par.val:
                return max(count1,count2) + 1
            else:
                return 0
        return 0
        
       
        