# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        self.val = 0
        self.check = False
        self.helper(root,p,q)
        return self.val
    
    def helper(self,root,p,q):
        if not root:
            return ""
        if root and not self.check:
            if q.val < root.val and p.val < root.val:
                self.helper(root.left,p,q)
            elif q.val > root.val and p.val > root.val:
                self.helper(root.right,p,q)
            else:
                self.val = root
                self.check = True
