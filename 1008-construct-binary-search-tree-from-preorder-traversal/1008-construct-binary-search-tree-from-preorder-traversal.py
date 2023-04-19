# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        
        for val in preorder:
            root = self.BST(root,val)
            
        return root
    
    
    def BST(self,root,val):
        if not root:
            return TreeNode(val,None,None)
        
        if root.val < val:
            root.right = self.BST(root.right,val)
            
        else:
            root.left = self.BST(root.left,val)
        
        return root