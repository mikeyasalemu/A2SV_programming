# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.summ = 0
        self.helper(root)
        return self.summ
    def helper(self,root):
         if root:
            
            if root.val % 2 == 0:
                self.adder(root.right,root.left)
                
            self.helper(root.left)
            self.helper(root.right)
    def adder(self,root1,root2):
        if root1:
            if root1.right:
                self.summ+= root1.right.val
            if root1.left:
                self.summ+= root1.left.val
        if root2:
            if root2.right:
                self.summ+= root2.right.val
            if root2.left:
                self.summ+= root2.left.val