# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.check = False
        self.check = self.helper(root,subRoot,False)
        return self.check
    
    def helper(self,root,subRoot,check):
        # if not root:
        #     return False
        if root:
            # print(root)
            # print(subRoot)
            # print("........")
            if subRoot.val == root.val:
                print("yes")
                
                if self.isSame(root,subRoot):
                    return True
            
            check1 = self.helper(root.left,subRoot,check)
            check2 = self.helper(root.right,subRoot,check)
            
            return check1 or check2
        
    def isSame(self,root,subRoot):
        
        if root and subRoot:
            if root.val != subRoot.val:
                return False
            left = self.isSame(root.left,subRoot.left)
            right = self.isSame(root.right,subRoot.right)
            
            return left and right
        if root == subRoot:
            return True