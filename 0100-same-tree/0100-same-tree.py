# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p,q)
    def check(self, p,q):
        if not q and not p:
            return True
        elif q and not p or p and not q:
            return False
        if  p.val == q.val:
            check1 = self.check(p.left,q.left)
            check2 = self.check(p.right,q.right)
            return check1 and check2