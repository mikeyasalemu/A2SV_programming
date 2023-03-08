
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return  self.helper(root.right,root.left)
    
    def helper(self,root1,root2):
        if  root1 and root2:

            if root1.val != root2.val:
                return False

            left = self.helper(root1.left,root2.right)
            right = self.helper(root1.right,root2.left)
            return left and right
        
        if root1 == root2:
            return True
       
        